# Phase 0 — PDM vs pip: The Landscape (Theory)

**Goal:** Understand *why* PDM exists and where it sits relative to `pip`, `venv`, and Poetry.
No commands to run in this phase — just build the mental model. (You'll install pdm in Phase 1.)

---

## 1. The problem: "installer" is not "project manager"

When people start with Python, the workflow is usually:

```bash
python -m venv .venv          # create an isolated environment
source .venv/bin/activate     # activate it
pip install requests          # install a package
pip freeze > requirements.txt # write down what's installed
```

This works, but notice how many *separate* tools and manual steps are involved, and what's
missing:

- **`venv`** creates the isolated environment — a separate tool you invoke by hand.
- **`pip`** installs packages into the active environment — that's *all* it does.
- **`pip freeze`** dumps a flat list of whatever happens to be installed. You maintain it by hand.

### What pip does NOT do

- It does **not** know about "your project." There's no project metadata, no concept of dev vs
  runtime dependencies, no scripts.
- It does **not** produce a true **lockfile**. `requirements.txt` from `pip freeze` is a flat
  snapshot; it doesn't cleanly separate *what you asked for* (`requests`) from *what got pulled in*
  (`requests`'s own dependencies like `urllib3`, `certifi`...). Re-resolving later can drift.
- It does **not** manage the virtualenv or the Python interpreter for you.
- It has a resolver, but no persisted, cross-platform "this exact tree is what works" artifact.

> **Mental model:** `pip` is a *power drill*. PDM is the whole *workshop* — it owns the project,
> the environment, the dependency graph, and the routine tasks.

---

## 2. What PDM adds

PDM (**P**ython **D**ependency **M**anager) is an **all-in-one project & dependency manager**
built on **modern Python packaging standards** (PEP 621, PEP 517/518). One tool gives you:

| Capability | pip | PDM |
|------------|-----|-----|
| Install packages | ✅ | ✅ |
| Create/manage a virtualenv for you | ❌ (use `venv` separately) | ✅ |
| Project metadata file | ❌ | ✅ `pyproject.toml` (PEP 621 standard) |
| Real lockfile (full pinned tree + hashes) | ❌ | ✅ `pdm.lock` |
| Separate dev / test / optional dependency groups | ❌ | ✅ |
| Run project scripts/tasks | ❌ | ✅ `pdm run`, `[tool.pdm.scripts]` |
| Build & publish a package | ❌ (use `build`/`twine`) | ✅ |
| Manage which Python interpreter is used | ❌ | ✅ (`pdm use`, works with pyenv) |

### The two key files PDM gives you

1. **`pyproject.toml`** — *what you want*. Human-edited intent: your project name, the Python
   version you support, and your **direct** dependencies (e.g. `requests>=2.31`). This is a
   **standard** file — not a PDM invention — so other tools understand it too.

2. **`pdm.lock`** — *exactly what you get*. Machine-generated. The **entire** resolved
   dependency tree, pinned to exact versions with hashes, so that `pdm install` on another
   machine (or next year) reproduces the **identical** environment.

> Think: `pyproject.toml` is your *shopping list*; `pdm.lock` is the *itemized receipt* that
> guarantees everyone gets the same cart.

---

## 3. Why lockfiles matter (the reproducibility story)

Imagine you `pip install requests` today and it pulls `urllib3 2.2.1`. Six months later a
teammate runs the same command and gets `urllib3 2.5.0`, which has a subtle behavior change —
and now "works on my machine" but not on theirs. A lockfile prevents this: it records the exact
versions of **everything**, direct and indirect, so installs are **deterministic**.

`pip freeze > requirements.txt` is a *poor man's lockfile*: it captures versions but mixes your
real dependencies with transitive ones and has no separate "intent" file, so it's easy to drift.

---

## 4. Where does Poetry fit? (so you're not confused later)

You'll hear about **Poetry** — it's the most popular tool in this same category. PDM and Poetry
solve the same problem (project + dependency management + lockfile). Key difference in
philosophy:

- **PDM** leans hard on **official standards** (`pyproject.toml` `[project]` table per PEP 621).
  Your metadata is portable.
- **Poetry** historically used its **own** `[tool.poetry]` table (it has since adopted more of
  the standard). Slightly more opinionated/heavier.

For learning, the concepts transfer almost 1:1. We use PDM because it's standards-first and
lightweight.

> There's also **uv** (a very fast newer tool) and **pipenv** (older). Same family. Once you
> understand PDM, you understand the category.

---

## 5. The vocabulary you now own

- **Installer** vs **project/dependency manager** — pip is the former, PDM the latter.
- **`pyproject.toml`** — standard project metadata + your *direct* dependencies (intent).
- **Lockfile (`pdm.lock`)** — exact pinned full tree (reproducibility).
- **Dependency group** — e.g. `dev` deps (pytest, ruff) kept separate from runtime deps.
- **Virtualenv** — isolated per-project environment; PDM creates/manages it for you.
- **Transitive dependency** — a dependency of your dependency.

---

## ✅ Checkpoint

Without looking, answer these (see [EXERCISES.md](EXERCISES.md) Phase 0):

1. In one sentence, what's the difference between pip and PDM?
2. What's the difference between `pyproject.toml` and `pdm.lock`?
3. Why is `pip freeze > requirements.txt` not as good as a real lockfile?

When you can answer those, move to **[Phase 1 → Setup](01-setup.md)**.
