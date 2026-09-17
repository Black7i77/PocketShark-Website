from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PocketSharkSiteTests(unittest.TestCase):
    def test_required_site_files_exist(self):
        required = [
            "index.html",
            "styles.css",
            "script.js",
            "assets/pocketshark-mark.svg",
            "_headers",
            "404.html",
        ]
        for rel in required:
            with self.subTest(rel=rel):
                self.assertTrue((ROOT / rel).is_file(), rel)

    def test_homepage_has_core_product_copy_and_safe_boundaries(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        required_phrases = [
            "Network visibility in your pocket.",
            "Android VpnService",
            "v0.2.0",
            "Live IPv4",
            "PCAP",
            "TLS and QUIC traffic stays encrypted",
            "No packet injection",
            "owned or authorised",
        ]
        for phrase in required_phrases:
            with self.subTest(phrase=phrase):
                self.assertIn(phrase, html)

    def test_homepage_links_to_canonical_project_destinations(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        urls = [
            "https://github.com/Black7i77/PocketShark-Android",
            "https://github.com/Black7i77/PocketShark-Android/releases",
            "https://github.com/Black7i77/PocketShark-Android/issues",
            "https://github.com/Black7i77/PocketShark-Android/blob/main/PRIVACY_POLICY.md",
            "https://github.com/Black7i77/PocketShark-Android/blob/main/LICENSE",
        ]
        for url in urls:
            with self.subTest(url=url):
                self.assertIn(url, html)

    def test_local_links_and_assets_exist(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        refs = re.findall(r'(?:href|src)="([^"]+)"', html)
        local = [r for r in refs if not (r.startswith("http") or r.startswith("#") or r.startswith("mailto:"))]
        for ref in local:
            clean = ref.split("?", 1)[0].split("#", 1)[0].lstrip("/")
            if not clean:
                continue
            with self.subTest(ref=ref):
                self.assertTrue((ROOT / clean).exists(), ref)

    def test_security_headers_are_present(self):
        headers = (ROOT / "_headers").read_text(encoding="utf-8")
        for header in [
            "Content-Security-Policy:",
            "X-Content-Type-Options: nosniff",
            "Referrer-Policy:",
            "Permissions-Policy:",
            "X-Frame-Options: DENY",
        ]:
            with self.subTest(header=header):
                self.assertIn(header, headers)

    def test_no_external_runtime_dependencies(self):
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        external_asset = re.compile(r'(?:src|href)="https?://[^\"]+\.(?:js|css|woff2?|ttf)(?:\?[^\"]*)?"', re.I)
        self.assertIsNone(external_asset.search(html))

    def test_html_avoids_inline_styles_under_strict_csp(self):
        for name in ["index.html", "404.html"]:
            html = (ROOT / name).read_text(encoding="utf-8")
            with self.subTest(name=name):
                self.assertNotIn(' style="', html)

    def test_project_docs_include_github_and_cloudflare_handoff(self):
        readme = ROOT / "README.md"
        deploy = ROOT / "DEPLOY.md"
        self.assertTrue(readme.is_file(), "README.md")
        self.assertTrue(deploy.is_file(), "DEPLOY.md")
        readme_text = readme.read_text(encoding="utf-8")
        deploy_text = deploy.read_text(encoding="utf-8")
        self.assertIn("PocketShark-Website", readme_text)
        self.assertIn("git init", deploy_text)
        self.assertIn("gh repo create Black7i77/PocketShark-Website", deploy_text)
        self.assertIn("Cloudflare Pages", deploy_text)
        self.assertIn("Build command: exit 0", deploy_text)
        self.assertIn("Build output directory: .", deploy_text)


if __name__ == "__main__":
    unittest.main()
