# Deploy PocketShark Website

This site is ready for a separate public GitHub repository named `PocketShark-Website` and a static Cloudflare Pages deployment.

## 1. Publish the website repository to GitHub

From inside the extracted `PocketShark-Website` folder on Kali Linux, initialise Git first:

```bash
git init
git branch -M main
git add .
git commit -m "Initial PocketShark website"
gh auth status
gh repo create Black7i77/PocketShark-Website \
  --public \
  --description "Official website for PocketShark Android" \
  --source=. \
  --remote=origin \
  --push
```

If the repository already exists, use:

```bash
git remote add origin https://github.com/Black7i77/PocketShark-Website.git
git push -u origin main
```

If `origin` already exists, use:

```bash
git remote set-url origin https://github.com/Black7i77/PocketShark-Website.git
git push -u origin main
```

## 2. Connect it to Cloudflare Pages

In the Cloudflare dashboard:

1. Open **Workers & Pages**.
2. Choose **Create** → **Pages** → **Connect to Git**.
3. Select the GitHub repository `Black7i77/PocketShark-Website`.
4. Use these deployment settings:

```text
Production branch: main
Framework preset: None
Build command: exit 0
Build output directory: .
Root directory: leave blank (repository root)
```

5. Deploy the project.
6. Cloudflare will assign a `*.pages.dev` URL.

Because this is a no-build static site, Cloudflare serves the files directly from the repository root. The `_headers` file supplies the site's response security headers.

## 3. Add the Cloudflare URL back to GitHub

After Cloudflare gives you the live URL, add it to the **About** section of:

`https://github.com/Black7i77/PocketShark-Android`

You can also add a Website section to the Android README, for example:

```markdown
## Website

Official PocketShark website: https://YOUR-PROJECT.pages.dev/
```

## 4. Optional custom domain later

A custom domain can be connected in Cloudflare Pages under **Custom domains** without changing the website source.
