# PocketShark Website Design

## Goal
Create a fast, static, Cloudflare Pages-ready website for PocketShark Android that presents the app professionally, links to its public GitHub repository and release area, explains the app's privacy model and Android limitations accurately, and invites feedback.

## Product positioning
PocketShark is presented as a rootless Android network-inspection and packet-analysis app. The site must not imply promiscuous Wi-Fi capture, TLS decryption, packet injection, spoofing, or traffic modification. Copy should emphasize local on-device analysis, Android VpnService, PCAP import/export, and safe/authorized use.

## Visual direction
Use a dark network-operations aesthetic derived from the Android icon colors: near-black/navy background, cyan primary accent (#37D9FF), mint secondary accent (#50E3A4), and restrained amber for caution/limits. The page should feel modern and technical without copying Scarface Stego Studio's green forensic-terminal identity.

## Architecture
Use plain HTML, CSS, and minimal JavaScript with no framework and no third-party runtime dependencies. Keep the site deployable as a static directory with no build command. Cloudflare Pages should publish the repository root.

## Page structure
1. Sticky navigation with PocketShark mark, Features, How it works, Boundaries, GitHub, and Get APK.
2. Hero with headline “Network visibility in your pocket.”, concise rootless/local description, GitHub and Releases CTAs, and a stylized phone packet-list preview.
3. Trust strip for rootless capture, local analysis, PCAP support, and version v0.2.0.
4. Feature grid covering live IPv4 capture, protocol identification, packet/hex detail, PCAP import/export, compatibility bypass, and privacy posture.
5. Three-step workflow: start local VPN capture, inspect traffic, export or review PCAP.
6. Android boundaries section stating phone-only local VPN visibility, IPv4 live capture, encrypted TLS/QUIC remains encrypted, and one VPN per user/profile.
7. Safety section that explicitly says no packet injection, spoofing, or traffic modification and limits use to owned/authorized devices, networks, or captures.
8. Footer with source, releases, issues/feedback, privacy policy, and license links.

## Accessibility and responsive behavior
Use semantic landmarks, keyboard-visible focus styles, readable contrast, `prefers-reduced-motion` handling, and a mobile menu. The layout must work from small Android screens through wide desktop screens.

## Cloudflare readiness
Include `_headers` with CSP, X-Content-Type-Options, Referrer-Policy, Permissions-Policy, and frame protection. Use only local assets and no analytics or trackers.

## Validation
Automated tests should assert required files, product claims, GitHub links, safe-use/boundary copy, security headers, and validity of local links. A local HTTP smoke test should return HTTP 200 for the homepage.
