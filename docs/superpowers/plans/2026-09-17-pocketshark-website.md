# PocketShark Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a polished, static, Cloudflare Pages-ready marketing site for PocketShark Android.

**Architecture:** A no-build static site using `index.html`, `styles.css`, `script.js`, and local SVG assets. Product facts and limitations are drawn from the current PocketShark Android README, and deployment is designed for Cloudflare Pages with the repository root as the publish directory.

**Tech Stack:** HTML5, CSS3, vanilla JavaScript, SVG, Python standard-library tests

**Spec:** `docs/superpowers/specs/2026-09-17-pocketshark-website-design.md`

## Global Constraints

- No frontend framework or package manager.
- No third-party runtime dependencies, analytics, trackers, or external fonts.
- Primary visual accents: `#37D9FF` and `#50E3A4`.
- Do not claim promiscuous Wi-Fi capture, live IPv6 capture, TLS/QUIC decryption, packet injection, spoofing, or traffic modification.
- Source repository: `https://github.com/Black7i77/PocketShark-Android`.
- Current displayed app version: `v0.2.0`.
- Static Cloudflare Pages deployment; no build command required.

---

### Task 1: Contract tests and static structure

**Files:**
- Create: `tests/site_test.py`
- Create: `index.html`
- Create: `styles.css`
- Create: `script.js`
- Create: `assets/pocketshark-mark.svg`
- Create: `_headers`
- Create: `404.html`

**Interfaces:**
- Consumes: Product facts in the design spec.
- Produces: Static site files directly publishable by Cloudflare Pages.

- [ ] **Step 1: Write tests that assert required files, copy, links, local references, and security headers.**
- [ ] **Step 2: Run `python3 -m unittest -v tests.site_test` and confirm RED because production files are missing.**
- [ ] **Step 3: Implement the minimal complete static site that satisfies the tests.**
- [ ] **Step 4: Run `python3 -m unittest -v tests.site_test` and confirm GREEN.**
- [ ] **Step 5: Commit the website implementation.**

### Task 2: Documentation and deployment handoff

**Files:**
- Create: `README.md`
- Create: `DEPLOY.md`

**Interfaces:**
- Consumes: Static site from Task 1.
- Produces: Exact GitHub and Cloudflare Pages setup instructions.

- [ ] **Step 1: Extend tests to require README/DEPLOY and exact deploy commands.**
- [ ] **Step 2: Run tests and confirm RED for missing docs.**
- [ ] **Step 3: Add project README and Cloudflare Pages deployment instructions.**
- [ ] **Step 4: Run tests and confirm GREEN.**
- [ ] **Step 5: Commit documentation.**

### Task 3: Final verification and distributable archive

**Files:**
- Verify: all project files
- Create outside repo: `PocketShark-Website-v1.zip`

**Interfaces:**
- Consumes: Tasks 1-2.
- Produces: Verified static site archive ready for the user's Kali machine.

- [ ] **Step 1: Run full unit tests.**
- [ ] **Step 2: Start `python3 -m http.server` locally and verify `/` returns HTTP 200.**
- [ ] **Step 3: Search for forbidden claims and external runtime dependencies.**
- [ ] **Step 4: Create a ZIP archive excluding `.git` and caches.**
- [ ] **Step 5: Record final Git status and commit log for handoff.**
