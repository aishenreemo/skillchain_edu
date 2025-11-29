# SkillChain EDU

**AI-Powered Curriculum Intelligence + Web3 Student Skill Identity**

> [!important]
> **Core insight:** Curriculums don’t match industry needs and student abilities aren’t properly represented. SkillChain EDU solves both — together.

---
[![Status: In Development](https://img.shields.io/badge/status-active-blue)]()
[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-green)]()
[![Built with AI + Web3](https://img.shields.io/badge/AI%20%2B%20Web3-enabled-purple)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)]()
---

## Table of contents

* [Project Overview](#project-overview)
* [Problems We Solve](#problems-we-solve)
* [Unified Solution](#unified-solution)
* [How It Works (20‑second flow)](#how-it-works-20-second-flow)
* [Key Features](#key-features)
* [Tech Stack (Pitch-Level)](#tech-stack-pitch-level)
* [Architecture (Pitch Diagram)](#architecture-pitch-diagram)
* [Target Users](#target-users)
* [SDG Alignment](#sdg-alignment)
* [Ethics & Privacy](#ethics--privacy)
* [Contributing](#contributing)
* [License](#license)

---

## Project Overview

SkillChain EDU is an AI-driven curriculum intelligence platform integrated with a Web3 student skill identity layer. It continuously analyzes course syllabi, job market demands, and emerging technologies to detect curriculum gaps and recommend updates. Students who complete industry-validated modules, projects, or workshops receive verifiable, consent-based skill credentials stored in a tamper-evident manner.

By combining AI-based curriculum mapping with blockchain-secured skill identity, SkillChain EDU helps institutions keep curricula relevant while providing students and employers trustable proof of capabilities.

---

## Problems We Solve

1. **Curriculum Gap**
   * Outdated syllabi
   * Slow curriculum updates
   * Industry–academe mismatch

2. **Identity & Proof**
   * Grades ≠ skills
   * Skills scattered across platforms
   * No trusted way to verify competencies

---

## Unified Solution

Two integrated layers:

* **Layer 1 — AI Curriculum Gap Detector**

  * Inputs: course syllabi, job market signals, tech trend feeds
  * Outputs: missing skills, outdated topics, curriculum recommendations

* **Layer 2 — Web3 Student Skill Identity**

  * Issue verifiable skill credentials (NFT / DID style)
  * Store only skill metadata on-chain; sensitive data remains off-chain
  * QR / Wallet verification for employers

Together these layers create a continuous loop: AI detects a gap → curriculum is updated → students learn and earn verifiable badges → employers verify skills → feedback flows back to AI.

---

## How It Works (Explain in 20 seconds)

![photo](how_it_works.png)

---

## Key Features

* **Automated Gap Detection**: NLP + embeddings analyze syllabi and job postings to surface missing skills.
* **Recommendation Engine**: Actionable curriculum updates prioritized by impact and feasibility.
* **Skill Badge Issuance**: Verifiable, portable credentials issued as on-chain claims (NFT or DID pointers).
* **Verification UX**: QR / Wallet-based verification for employers and third parties.
* **Analytics Dashboard**: Visualize skill supply/demand, adoption, and student progress.
* **Privacy-first Design**: No grades on-chain; consent required for any public attestation.

---

## Tech Stack (Pitch-Level Only)

**AI Layer** (SDG 9 alignment)

* NLP pipelines, embeddings store
* Skill extraction and mapping models
* Analytics and reporting dashboard (web)

**Web3 Layer**

* Smart contracts for credential anchoring
* NFT or verifiable credential standards (e.g., W3C Verifiable Credentials / DIDs)
* Wallet & QR verification flow

**Infrastructure / Integrations**

* Cloud-hosted backend APIs
* LMS integration adapters (LTI, SCORM connectors)
* Job market connectors (LinkedIn jobs, remote job feeds, company APIs)

---

## Architecture (Pitch Diagram)

> *(Include a one-slide architecture diagram in the pitch deck — show data flow: Syllabi & Job Feeds → AI Engine → Curriculum Recommendations → LMS → Student Assessment → Credential Issuer → Blockchain → Employer Verification → Feedback to AI.)*

---

## Target Users

* **Students** — Gain verifiable skill badges to complement academic transcripts.
* **Faculty / Curriculum Designers** — Get AI-guided recommendations to modernize courses.
* **Employers / Recruiters** — Quickly verify candidate competencies.
* **Researchers & Policy Makers** — Access aggregated skill demand analytics.

---

## SDG Alignment

* **SDG 9 — Industry, Innovation & Infrastructure**: Modernizes education systems using AI and decentralized verification infrastructure, enabling innovation in workforce development.
* **SDG 4 — Quality Education**: Improves learning relevance and outcomes by aligning curricula to real-world skill demand and providing proof of competencies.

---

## Ethics & Privacy
* No storing of grades or sensitive personal data on-chain.
* Skill attestations are consent-based and revocable.
* AI provides recommendations — human governance and review remain mandatory.
* Transparent audit logs for credential issuance and revocation.

---

## License

This project is released under the **MIT License**. See [LICENSE](LICENSE.md) for details.

---

> [!quote]
> Curriculum evolves with industry - credentials evolve with students.
