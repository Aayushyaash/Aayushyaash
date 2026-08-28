<!-- Header Section -->
<div align="center">
   <img width="100%" src="assets/header.gif" alt="Animated Header"/>
</div>
<h1 align="center">Hi <img src="assets/emojis/Person Raising Hand Medium-Dark Skin Tone.png" width="32px" height="32px" alt="Person Raising Hand"/>, I'm Aayush Yash</h1>
<h3 align="center">Python Backend & AI Engineer | FastAPI • Computer Vision • RAG <img src="assets/emojis/Rocket.png" width="20px" height="20px" alt="Rocket"/></h3>

<p align="center">
  <a href="mailto:aayushyaash@outlook.com">
    <img src="https://img.shields.io/badge/Email-aayushyaash%40outlook.com-0078D4?style=for-the-badge&logo=microsoft-outlook&logoColor=white" alt="Email"/>
  </a>
  <a href="https://linkedin.com/in/aayush-yash" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-Aayush_Yash-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
  </a>
  <img src="https://img.shields.io/badge/Open_to_Work-Python%20%E2%80%A2%20Backend%20%E2%80%A2%20AI-success?style=for-the-badge"/>
</p>

## <img src="assets/emojis/Technologist Medium-Dark Skin Tone.png" width="24px" height="24px"/> About Me

Backend & AI engineer focused on building document intelligence pipelines, local-first RAG systems, and asynchronous backend services with **Python, FastAPI, PyTorch, and SQL**, alongside frontend engineering with **TypeScript and React**.

> <img src="assets/emojis/Light Bulb.png" width="16px" height="16px"/> *Engineering focus: building resilient OCR/vision extraction pipelines and low-latency retrieval architectures.*

---

## <img src="assets/emojis/Rocket.png" width="24px" height="24px"/> Open Source Contributions

### [QwenLM/qwen-code](https://github.com/QwenLM/qwen-code) — [PR #1890](https://github.com/QwenLM/qwen-code/pull/1890) (Merged)
Fixed a Windows compatibility bug where CRLF line endings caused externally-created subagents, skills, and Claude-converted agents to fail silently ([Issue #1868](https://github.com/QwenLM/qwen-code/issues/1868)).
- **Root Cause**: Core parsers relied on newline-sensitive regex patterns expecting only `\n`, failing on Windows `\r\n` content.
- **Architecture & Refactoring**: Introduced a centralized `normalizeContent()` utility for BOM stripping and CRLF normalization, replacing duplicate parsing logic across subagent, skill, and converter modules.
- **Verification**: Added regression and integration test suites; verified on Windows 11 with all 13 automated checks passing.

---

## <img src="assets/emojis/Floppy Disk.png" width="24px" height="24px" alt="Projects"/> Featured Projects

### <img src="assets/emojis/Magnifying Glass Tilted Left.png" width="20px" height="20px"/> [Bharat-ID-Validator](https://github.com/Aayushyaash/Bharat-ID-Validator)
FastAPI pipeline for Indian identity document classification and OCR field extraction.
- **Engineering Choice**: Two-phase OCR with YOLO-based orientation correction reduces invalid text extraction noise.
- **Results**: 98%+ classification accuracy across 7 document formats (50+ field classes); ~80% latency reduction over naive whole-image OCR passes.
- **Stack**: `FastAPI`, `PyTorch`, `YOLO`, `OpenCV`, `Pydantic`, `pytest`

### <img src="assets/emojis/Books.png" width="20px" height="20px"/> [Rag-chatbot](https://github.com/Aayushyaash/Rag-chatbot)
Privacy-first RAG engine for multi-document PDF querying.
- **Engineering Choice**: Hybrid semantic + BM25 keyword search unified via Reciprocal Rank Fusion (RRF) to mitigate precision loss in vector-only search for exact domain identifiers.
- **Privacy & Execution**: Local chunk embedding storage; switchable local vs cloud inference pipeline with deduplication.
- **Stack**: `FastAPI`, `ChromaDB`, `PyTorch`, `Gemini API`, `HuggingFace`

### 🎭 [MITRA Theatre — Live Site](https://mitraproductions.com/)
Cinematic theatre company website — designed, built, and deployed independently for a live theatre organization.
- **Engineering**: Automated local validation pipeline — Husky pre-commit/pre-push hooks, Knip dead-code detection, Conventional Commits enforcement, and Vitest + Playwright browser testing.
- **Frontend**: React 19 + TypeScript, Framer Motion, custom cinematic intro/loading sequence, modular component hierarchy, and dark-theatrical design system.
- Source code is private.
- **Stack**: `React 19`, `TypeScript`, `Vite`, `Framer Motion`, `Vitest`, `Playwright`

### <img src="assets/emojis/Brain.png" width="20px" height="20px"/> [MindMate-AI](https://github.com/Aayushyaash/MindMate-AI)
Collaborative AI mental health platform *(Team Project — Original repository maintained by team lead)*.
- **My Contributions**: Real-time voice pipeline (Twilio WebRTC + ElevenLabs TTS), asynchronous WebSocket consumers, PHQ-9 assessment and scoring workflows, and JWT authentication.
- **Stack**: `Django`, `Redis Channels`, `WebSockets`, `Twilio`, `ElevenLabs`

---

## <img src="assets/emojis/Hammer and Wrench.png" width="24px" height="24px" alt="Tech Stack"/> Technical Skills

<details open>
<summary><strong>Languages</strong></summary>
<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=cplusplus&logoColor=white)

</details>

<details>
<summary><strong>Backend & Data</strong></summary>
<br>

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)

</details>

<details>
<summary><strong>AI / ML, Retrieval & Computer Vision</strong></summary>
<br>

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO-00FFFF?style=for-the-badge&logo=yolo&logoColor=black)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6600?style=for-the-badge&logo=database&logoColor=white)

</details>

<details>
<summary><strong>Frontend, Testing & Developer Tools</strong></summary>
<br>

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=for-the-badge&logo=vitest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=for-the-badge&logo=playwright&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

</details>

---

<p align="center">
  <img src="assets/emojis/High Voltage.png" width="16px" height="16px"/> <b>Fun fact:</b> I enjoy music <img src="assets/emojis/Musical Notes.png" width="16px" height="16px"/>, anime <img src="assets/emojis/Television.png" width="16px" height="16px"/>, and reading light novels <img src="assets/emojis/Books.png" width="16px" height="16px"/>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=aayushyaash&label=Profile%20views&color=0e75b6&style=for-the-badge" alt="Profile Views" />
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=60&section=footer"/>
</p>
