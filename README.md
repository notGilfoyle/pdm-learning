# Learning PDM — A Phased, Hands-On Course

Welcome! This is a self-paced course to learn **PDM** (Python Dependency Manager): what it is,
how it differs from `pip`, and how to use it confidently on real projects — ending with your
code under version control.

It follows a **theory → practical** rhythm. Do **one phase at a time**, run the practicals
yourself, and make a local git commit at the end of each phase.

## How to use this course

1. Read the lesson file for the phase.
2. Run the **Practical** commands in your terminal as you go.
3. Hit the **Checkpoint** in [EXERCISES.md](EXERCISES.md) before moving on.
4. Commit your progress locally (you'll set git up in Phase 1).

> Tip: keep this folder open in one window and a terminal in another.

## Syllabus

| Phase | File | What you learn | Type |
|-------|------|----------------|------|
| 0 | [00-pdm-vs-pip.md](00-pdm-vs-pip.md) | The packaging landscape; pip vs pdm vs poetry; why lockfiles matter | Theory |
| 1 | [01-setup.md](01-setup.md) | Install pdm (Homebrew), verify, configure, init git | Theory + Practical |
| 2 | [02-first-project.md](02-first-project.md) | `pdm init`, anatomy of `pyproject.toml`, the virtualenv | Theory + Practical |
| 3 | [03-dependencies.md](03-dependencies.md) | Add/remove deps, dependency groups, `pdm.lock`, sync/install | Theory + Practical |
| 4 | [04-running-code.md](04-running-code.md) | `pdm run`, custom scripts, build & test a tiny app | Theory + Practical |
| 5 | [05-reproducibility-git.md](05-reproducibility-git.md) | Reproducible installs, `.gitignore`, commit, optional GitHub push | Theory + Practical |

Then: [EXERCISES.md](EXERCISES.md) — checkpoints per phase + a capstone.

## Your environment (as of course creation)

- macOS, Homebrew installed ✅
- System Python: 3.9.6 · `pyenv` installed ✅
- pdm: **not yet installed** (you'll install it in Phase 1)
- git configured as `Roshan Sahu <iamroshannn@gmail.com>`
- GitHub: pushing is **optional** and saved for the end — local git first.

## The 30-second summary

- **pip** = an *installer*. It puts packages somewhere. You manually maintain `requirements.txt`.
- **pdm** = a *project manager*. It tracks your project in `pyproject.toml`, locks the exact
  dependency tree in `pdm.lock`, manages the virtualenv, groups dev/runtime deps, and runs scripts.

Start with **[Phase 0 →](00-pdm-vs-pip.md)**.
