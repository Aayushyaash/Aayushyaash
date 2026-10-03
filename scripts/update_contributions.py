#!/usr/bin/env python3
"""Regenerate the open-source contribution ledger in README.md for @Aayushyaash.

Pulls public pull requests authored by @Aayushyaash in upstream repositories
and updates the section between <!-- CONTRIB:START --> and <!-- CONTRIB:END -->.
"""
from __future__ import annotations

import contextlib
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

USER = "Aayushyaash"
README = Path(__file__).resolve().parent.parent / "README.md"
START = "<!-- CONTRIB:START -->"
END = "<!-- CONTRIB:END -->"

# -----------------------------------------------------------------------------
# Configuration Settings (pr-showcase engine)
# -----------------------------------------------------------------------------
CONFIG = {
    # Alignment of the headline metric badges: "center" | "left" | "right"
    "badge_alignment": "center",
    # Alignment of the "Contributed to" repository badges: "center" | "left" | "right"
    "contributed_to_alignment": "left",
    # Whether to show live GitHub star counts on badges (True) or only repository names (False)
    "show_stars": True,
    # Maximum merged PRs to display in the main Featured section before putting older ones in drawer
    "max_featured_merged": 5,
    # Whether the "In review" drawer is collapsed by default (<details> vs <details open>)
    "collapse_in_review": True,
    # Whether the "More merged upstream" drawer is collapsed by default
    "collapse_more_merged": True,
    # Description display style per section:
    #   "inline"   -> Render description as text sub-caption: <sub>...</sub>
    #   "tooltip"  -> Embed in link title tooltip; hide visible text for compact layout
    #   "both"     -> Render inline text AND embed hover tooltip
    #   "none"     -> Omit description completely
    "descriptions": {
        "featured_merged": "both",
        "more_merged": "tooltip",
        "in_review": "tooltip",
        "star_badges": "tooltip",
    },
}


def gh(url: str) -> dict:
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": f"{USER}-profile-updater",
        },
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_prs() -> list[dict]:
    q = urllib.parse.quote(f"author:{USER} is:pr -user:{USER} is:public")
    items: list[dict] = []
    page = 1
    while True:
        data = gh(
            f"https://api.github.com/search/issues?q={q}&per_page=100&page={page}&sort=created&order=desc"
        )
        batch = data.get("items", [])
        items.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    prs = []
    for it in items:
        repo = "/".join(it["repository_url"].split("/")[-2:])
        pr_info = it.get("pull_request") or {}
        merged = bool(pr_info.get("merged_at"))
        if not merged and it["state"] == "closed":
            # For search issue items, merged_at can sometimes be null even if merged.
            # Double-check specific PR details if closed
            with contextlib.suppress(urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError):
                detail = gh(pr_info.get("url") or it["url"])
                merged = bool(detail.get("merged"))

        state = "merged" if merged else ("open" if it["state"] == "open" else "closed")
        prs.append({
            "repo": repo,
            "number": it["number"],
            "title": it["title"].rstrip("…").strip(),
            "url": it["html_url"],
            "state": state,
            "created": it["created_at"][:10],
        })

    # Discard unmerged closed PRs: only count merged and active in-review PRs
    return [p for p in prs if p["state"] in ("merged", "open")]


def fetch_repo_descriptions(repos: set[str]) -> dict[str, str]:
    descriptions = {}
    for repo in sorted(repos):
        try:
            data = gh(f"https://api.github.com/repos/{repo}")
            desc = data.get("description") or repo
            descriptions[repo] = desc
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, KeyError):
            descriptions[repo] = repo
    return descriptions


def escape_attr(text: str) -> str:
    """Escape quotes and special characters for HTML/Markdown title attributes."""
    return text.replace('"', "&quot;").replace("\n", " ").strip()


def format_repo_header(repo: str, desc: str, mode: str) -> str:
    """Format repository header with avatar, link, and optional tooltip / inline description."""
    owner = repo.split("/")[0]
    avatar = f'<img src="https://github.com/{owner}.png?size=32" width="16" height="16" valign="middle" alt="{owner}" />'
    clean_desc = escape_attr(desc) if desc else repo

    if mode in ("tooltip", "both"):
        link = f'[`{repo}`](https://github.com/{repo} "{clean_desc}")'
    else:
        link = f'[`{repo}`](https://github.com/{repo})'

    header = f"**{avatar} {link}**"
    if mode in ("inline", "both") and desc and desc != repo:
        header += f"<br/><sub>{desc}</sub>"
    return header


def render_grouped_prs(prs: list[dict], descriptions: dict[str, str], mode: str) -> list[str]:
    """Render a list of PRs grouped by repository with avatars and links."""
    by_repo: dict[str, list[dict]] = defaultdict(list)
    for p in prs:
        by_repo[p["repo"]].append(p)

    lines: list[str] = []
    for repo in sorted(by_repo, key=lambda r: (-len(by_repo[r]), r.lower())):
        desc = descriptions.get(repo, repo)
        lines.append(format_repo_header(repo, desc, mode))
        for p in sorted(by_repo[repo], key=lambda x: x["number"], reverse=True):
            lines.append(f"- [#{p['number']}]({p['url']}) {p['title']}")
        lines.append("")
    return lines


def render(prs: list[dict], descriptions: dict[str, str]) -> str:
    merged = [p for p in prs if p["state"] == "merged"]
    open_ = [p for p in prs if p["state"] == "open"]
    projects = sorted({p["repo"] for p in prs})
    out: list[str] = []

    # 1. Headline Metric Badges with configurable alignment
    align = CONFIG.get("badge_alignment", "center")
    align_attr = f' align="{align}"' if align in ("center", "left", "right") else ""
    out.append(f"<p{align_attr}>")
    out.append(f'  <img src="https://img.shields.io/badge/pull_requests-{len(prs)}-1f6feb?style=flat-square&labelColor=161b22&logo=git&logoColor=white" alt="PRs" />')
    out.append(f'  <img src="https://img.shields.io/badge/merged-{len(merged)}-8957e5?style=flat-square&labelColor=161b22&logo=github&logoColor=white" alt="Merged" />')
    out.append(f'  <img src="https://img.shields.io/badge/in_review-{len(open_)}-2da44e?style=flat-square&labelColor=161b22&logo=githubactions&logoColor=white" alt="In Review" />')
    out.append(f'  <img src="https://img.shields.io/badge/projects-{len(projects)}-f78166?style=flat-square&labelColor=161b22&logo=opensourceinitiative&logoColor=white" alt="Projects" />')
    out.append("</p>\n")

    # 2. Merged Upstream (Featured + Optional Overflow Drawer)
    if merged:
        sorted_merged = sorted(merged, key=lambda x: x["created"], reverse=True)
        max_featured = CONFIG.get("max_featured_merged", 5)
        featured_prs = sorted_merged[:max_featured]
        overflow_prs = sorted_merged[max_featured:]

        out.append("### Merged upstream\n")
        featured_mode = CONFIG.get("descriptions", {}).get("featured_merged", "both")
        out.extend(render_grouped_prs(featured_prs, descriptions, featured_mode))

        # Drawer for older merged PRs if exceeding threshold
        if overflow_prs:
            collapse_attr = "" if CONFIG.get("collapse_more_merged", True) else " open"
            out.append(f"<details{collapse_attr}>")
            out.append(f"<summary><b>View {len(overflow_prs)} more merged pull requests</b></summary>\n")
            more_mode = CONFIG.get("descriptions", {}).get("more_merged", "tooltip")
            out.extend(render_grouped_prs(overflow_prs, descriptions, more_mode))
            out.append("</details>\n")

    # 3. In Review Drawer (Grouped by Repo)
    if open_:
        out.append("### In review\n")
        collapse_attr = "" if CONFIG.get("collapse_in_review", True) else " open"
        out.append(f"<details{collapse_attr}>")
        out.append(f"<summary><b>{len(open_)} open pull requests across {len({p['repo'] for p in open_})} repositories</b></summary>\n")
        in_review_mode = CONFIG.get("descriptions", {}).get("in_review", "tooltip")
        out.extend(render_grouped_prs(open_, descriptions, in_review_mode))
        out.append("</details>\n")

    # 4. Contributed to Badge Cloud with Configurable Alignment & Optional Stars
    out.append("### Contributed to\n")
    contrib_align = CONFIG.get("contributed_to_alignment", "left")
    contrib_align_attr = f' align="{contrib_align}"' if contrib_align in ("center", "left", "right") else ""
    out.append(f"<p{contrib_align_attr}>")
    badge_mode = CONFIG.get("descriptions", {}).get("star_badges", "tooltip")
    show_stars = CONFIG.get("show_stars", True)
    for repo in projects:
        desc = descriptions.get(repo, repo)
        title_attr = f' title="{escape_attr(desc)}"' if badge_mode == "tooltip" and desc else ""
        encoded_repo = urllib.parse.quote(repo)
        if show_stars:
            badge_url = f"https://img.shields.io/github/stars/{repo}?style=flat-square&logo=github&label={encoded_repo}&color=1f6feb&labelColor=0d1117"
            badge_alt = f"{repo} stars"
        else:
            badge_url = f"https://img.shields.io/badge/{encoded_repo}-1f6feb?style=flat-square&logo=github&logoColor=white&labelColor=0d1117"
            badge_alt = repo
        out.append(f'  <a href="https://github.com/{repo}"{title_attr}><img alt="{badge_alt}" src="{badge_url}" /></a>')
    out.append("</p>")
    return "\n".join(out)


def main() -> int:
    prs = fetch_prs()
    if not prs:
        print("No PRs returned; leaving README untouched.", file=sys.stderr)
        return 0

    if not README.exists():
        print(f"README not found at {README}", file=sys.stderr)
        return 1

    repos = {p["repo"] for p in prs}
    descriptions = fetch_repo_descriptions(repos)

    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        print("Markers not found in README.md; printing rendered output instead:\n")
        print(f"{START}\n{render(prs, descriptions)}\n{END}")
        return 0

    new_block = f"{START}\n{render(prs, descriptions)}\n{END}"
    updated = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: new_block, text, flags=re.S)
    if updated != text:
        README.write_text(updated, encoding="utf-8")
        print(f"README updated: {len(prs)} PRs, {sum(p['state']=='merged' for p in prs)} merged.")
    else:
        print("README already up to date.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
