---
id: 0001
title: AI-Native Software Development Book Project Constitution
stage: constitution
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: user
command: /sp.constitution Project: AI-Native Software Development Book + Docusaurus Website + Integrated RAG Chatbot
labels: ["constitution", "project-setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:

tests:

---

## Prompt

/sp.constitution Project: AI-Native Software Development Book + Docusaurus Website + Integrated RAG Chatbot

Core Principles:
- Accuracy through primary source verification and consistent fact-checking
- Clarity suitable for technical readers studying AI-native software development
- Reproducibility: all implementation steps verifiable on a fresh environment
- Rigor: references must come from authoritative and peer-reviewed sources where possible
- Modular structure aligned with the 4-course modules and weekly breakdown plan

Key Standards:
- All factual or technical claims must be traceable to original sources
- Citation format: APA style for external references
- Source requirement: at least 50% peer-reviewed or official technical documentation
- Plagiarism tolerance: 0% (content must be original)
- Writing clarity target: Flesch-Kincaid grade 10–12

Docusaurus Requirements:
- All book content must be formatted as Markdown compatible with Docusaurus
- Must include sidebars, navigation, table of contents, and search metadata
- Each chapter must include:
  - A “Personalize Content” button
  - A “Translate to Urdu” button
- The 4-module course structure and weekly breakdown must be included as:
  - /modules overview page
  - Individual pages for each weekly topic

Chatbot Integration Requirements:
- RAG chatbot must be embedded in the published Docusaurus website
- Chatbot must answer questions about the book content
- Must support “answer based on selected text only” mode
- Must use:
  - OpenAI Agents / ChatKit SDK
  - FastAPI backend
  - Neon Serverless Postgres
  - Qdrant Cloud free-tier for vector embeddings

Authentication Requirements:
- Signup & Signin implemented using better-auth.com
- Signup flow must collect the user's:
  - Software background
  - Hardware background
- User profile must be used to personalize chapter content

Reusable Intelligence Requirements:
- Must include Claude Code Subagents and Agent Skills
- Book should demonstrate:
  - How reusable intelligence components are built
  - How the project itself uses subagents/skills internally

Constraints:
- Book Word Count: 15,000–30,000 words total
- Minimum 20 sources
- All content authored inside Claude Code and generated via Spec-Kit Plus
- Output Format:
  - Docusaurus Markdown files
  - GitHub Pages deployment-ready
  - PDF export optional

Success Criteria:
- All claims verified with sources
- Zero plagiarism
- Docusaurus site builds successfully without errors
- RAG chatbot functions both globally and on selected text
- Personalized and Urdu translation buttons work on every chapter
- Signup/signin system works end-to-end with personalization logic
- Subagents and skills implemented and documented
- Follows all hackathon base + bonus requirements

## Response snapshot

Acknowledged the project constitution, outlining core principles, key standards, and requirements for Docusaurus, chatbot integration, authentication, and reusable intelligence, along with project constraints and success criteria.

## Outcome

- ✅ Impact: Project constitution defined and recorded.
- 🧪 Tests: n/a
- 📁 Files: history/prompts/constitution/0001-ai-native-software-development-book-project-constitution.constitution.prompt.md
- 🔁 Next prompts: n/a
- 🧠 Reflection: Successfully recorded the project constitution as a PHR.
- Failure modes observed: none
- Graders run and results (PASS/FAIL): n/a
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): n/a
