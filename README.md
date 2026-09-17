# PocketShark-Website

Public website for **PocketShark Android v0.2.0** — a rootless Android network-inspection and packet-analysis app.

The site is deliberately lightweight and privacy-friendly:

- plain HTML, CSS, and JavaScript
- no framework or package manager
- no external fonts, analytics, trackers, or runtime CDN dependencies
- responsive layout for phone and desktop
- Cloudflare Pages-ready security headers in `_headers`
- links to the canonical PocketShark Android source, releases, issues, privacy policy, and license

## Local preview

```bash
python3 -m http.server 8080
```

Then open `http://127.0.0.1:8080/`.

## Tests

```bash
python3 -m unittest -v tests.site_test
```

## Source app

PocketShark Android source:

`https://github.com/Black7i77/PocketShark-Android`

## Deployment

See [`DEPLOY.md`](DEPLOY.md) for GitHub and Cloudflare Pages steps.
