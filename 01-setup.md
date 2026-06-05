# Phase 1 — Setup: Install PDM & Init Git (Theory + Practical)

**Goal:** Get a working `pdm` on your machine, understand how it's isolated, and put this
course folder under git.

---

## Theory

### How should pdm be installed?

pdm is itself a Python application. The golden rule for Python **CLI tools**: install them in
**their own isolated environment**, never into a project's venv or your system Python. Options:

- **Homebrew** (what we'll use) — `brew install pdm`. Brew keeps pdm and its dependencies fully
  isolated and gives you `brew upgrade pdm` later. Simplest on your Mac.
- **pipx** — installs Python CLI tools each in their own venv. Also great; one more tool to set up.
- **Official script** — `curl -sSL https://pdm-project.org/install-pdm.py | python3 -`.

We chose **Homebrew** because you already have it.

### pdm and your Python interpreters

pdm doesn't *replace* Python — it *picks* one. For each project, pdm selects an interpreter
(your system Python, a pyenv version, etc.) and builds the project's virtualenv from it. You
have `pyenv` installed, so later you could do things like `pdm use 3.12`. For this course your
system Python 3.9.6 is fine.

> Key idea: **pdm-the-tool** lives in its own brew-managed environment. The **project venvs**
> pdm creates are entirely separate from that. Don't confuse the two.

---

## Practical

### 1. Install pdm

```bash
brew install pdm
```

### 2. Verify

```bash
pdm --version
```

Expected: something like `PDM, version 2.x.x`. If you see a version number, you're good.

### 3. Look around pdm's config (read-only tour)

```bash
pdm config            # prints all current config keys and values
```

Two settings worth knowing about:

- `python.use_venv` — whether pdm uses a classic virtualenv (default `true`, recommended).
- `venv.in_project` — if `true`, the venv is created as `.venv/` **inside** your project
  folder (tidy and easy to find). Let's turn that on:

```bash
pdm config venv.in_project true
```

This is a global pdm setting (stored in pdm's own config, not your project), so you only do it
once.

### 4. Put this course folder under git

You're in `/Users/roshan/code/pdm-learning`. Initialize a local repository:

```bash
cd /Users/roshan/code/pdm-learning
git init
git add .
git commit -m "Phase 0-1: course material + setup notes"
```

> We're doing **local git only** for now. Pushing to GitHub is an optional final step in Phase 5.

---

## What just happened

- `pdm` now lives in a brew-isolated environment, available globally as a command.
- You told pdm to keep project venvs inside each project as `.venv/`.
- This learning folder is now a git repo with your first commit.

---

## ✅ Checkpoint (see [EXERCISES.md](EXERCISES.md) Phase 1)

- `pdm --version` prints a version.
- `pdm config venv.in_project` returns `True`.
- `git log --oneline` shows your first commit.

Next: **[Phase 2 → Your first PDM project](02-first-project.md)**.
