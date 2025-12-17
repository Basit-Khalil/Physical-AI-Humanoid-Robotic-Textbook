---
id: 0003
title: AI-Native Software Development Book Architectural Plan
stage: plan
date: 2025-12-06
surface: agent
model: claude-sonnet-4-5-20250929
feature: AI-Native-Book
branch: master
user: user
command: /sp.plan sp.plan
labels: ["plan", "architecture"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - specs/AI-Native-Book/plan.md
tests:

---

## Prompt

/sp.plan sp.plan

Create:
- High-level architecture sketch covering:
  - Docusaurus book structure
  - GitHub Pages deployment flow
  - FastAPI backend architecture
  - RAG pipeline (Neon + Qdrant + OpenAI Agents/ChatKit)
  - Authentication flow (better-auth.com)
  - Personalization and Urdu translation workflow
  - Claude Code Subagents and Agent Skills usage
- Section-by-section outline of the book including:
  - 4 modules
  - Weekly breakdowns
  - Chapter-level learning outcomes
  - Embedded task-based tutorials
- Research approach for collecting:
  - AI-native software development theory
  - RAG systems best practices
  - Vector databases (Qdrant)
  - Serverless Postgres (Neon)
  - Authentication frameworks
  - Docusaurus + FastAPI integration strategies
- Quality-validation plan to ensure:
  - Technical accuracy
  - Reproducibility
  - Alignment with hackathon acceptance criteria
  - Consistency with APA citation style
  - Smooth Docusaurus build without errors

Decisions needing documentation:
- Choice of Docusaurus vs other SSG options (tradeoffs: ecosystem, MDX, search)
- Choice of Qdrant vs other vector DBs (tradeoffs: performance, free-tier limits)
- Whether embeddings are stored in Neon or Qdrant only
- Choice of FastAPI instead of Node.js for backend
- Where personalization logic resides (client vs server)
- Urdu translation method (LLM-based vs static translations)
- Whether subagents handle:
  - Document structuring
  - Code generation
  - Personalization rules
- Sidebar strategy for modules and weekly content
- Deployment method: GitHub Pages vs Vercel vs Netlify
- User-data flow (signup → personalization → content rendering)

Testing strategy:
- Validate all chapters render correctly inside Docusaurus
- Ensure RAG chatbot:
  - Answers from book content only
  - Works in “selected text only” mode
  - Handles edge cases (empty selection, long queries)
- Validate authentication flow:
  - Signup & signin work end-to-end
  - Background questions are stored and retrievable
- Personalization tests:
  - Different user profiles produce different versions of the same chapter
- Urdu translation tests:
  - Button triggers correct transformation
  - Maintains formatting in Markdown/MDX
- Backend validation:
  - API endpoints return correct responses
  - Qdrant and Neon connections stable
- Spyglass-quality checks:
  - Factual accuracy
  - Source traceability
  - APA citation formatting
- Compatibility tests:
  - GitHub Pages deployment builds successfully
  - Chatbot iframe or widget works inside Docusaurus

Technical details:
- Use a research-concurrent approach (research while writing; update as needed)
- Follow APA citation style as defined in sp.constitution
- Organize the plan and writing workflow by phases:
  1. Research Phase → Collect sources, validate concepts
  2. Foundation Phase → Establish Docusaurus structure + repo
  3. Analysis Phase → Break down chapters, modules, weekly topics
  4. Synthesis Phase → Write, integrate backend, embed chatbot, test features

## Response snapshot

Successfully created a detailed architectural plan for the AI-Native Software Development Book, covering high-level architecture, book outline, research approach, quality validation, decisions, and testing strategy in `specs/AI-Native-Book/plan.md`.

## Outcome

- ✅ Impact: Comprehensive architectural plan drafted and documented.
- 🧪 Tests: n/a
- 📁 Files: specs/AI-Native-Book/plan.md
- 🔁 Next prompts: Review and approval of the architectural plan.
- 🧠 Reflection: All requested sections of the plan have been thoroughly addressed and documented in `specs/AI-Native-Book/plan.md`.
- Failure modes observed: none
- Graders run and results (PASS/FAIL): n/a
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): n/a
