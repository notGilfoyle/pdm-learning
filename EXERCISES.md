# Exercises & Checkpoints

Use these to confirm each phase stuck. Try to answer/do them **without** looking back first.

---

## Phase 0 — pip vs pdm (concepts)

1. In one sentence, what's the difference between pip and PDM?
2. What does `pyproject.toml` hold vs what does `pdm.lock` hold?
3. Why is `pip freeze > requirements.txt` weaker than a real lockfile?
4. What is a *transitive* dependency? Give an example.

<details><summary>Answers</summary>

1. pip is an *installer* (puts packages in an env); PDM is a *project & dependency manager*
   (tracks metadata, locks the full tree, manages the venv, runs scripts).
2. `pyproject.toml` = your intent (metadata + direct deps). `pdm.lock` = the exact pinned full
   tree (direct + transitive) for reproducibility.
3. It mixes direct and transitive deps in one flat file with no separate "intent," so it drifts
   and isn't a reliable reproducible artifact.
4. A dependency of your dependency — e.g. `requests` pulls in `urllib3`.
</details>

---

## Phase 1 — Setup

- [ ] `pdm --version` prints a version.
- [ ] `pdm config venv.in_project` returns `True`.
- [ ] `git log --oneline` shows your first commit.

**Stretch:** What's the difference between *pdm-the-tool's* environment and the *project venv*
pdm creates?

---

## Phase 2 — First project

- [ ] `myapp/pyproject.toml` exists; you can point at the `dependencies` line.
- [ ] `pdm info` shows an interpreter path inside `.venv/`.
- [ ] You chose "application" (not library) during `pdm init` — why does that matter?

**Stretch:** Run `pdm info --env` and find where the venv lives.

---

## Phase 3 — Dependencies

- [ ] `requests` is under `[project] dependencies`.
- [ ] `pytest` is in the **dev** group, not runtime.
- [ ] Find `urllib3` — which file is it in, and why *that* file?
- [ ] Explain `pdm install` vs `pdm sync` vs `pdm lock`.

**Stretch:** Add a pinned version: `pdm add "requests==2.32.3"`, observe the change, then
`pdm update requests` and watch the lock change.

---

## Phase 4 — Running code

- [ ] `pdm run start` runs your app.
- [ ] `pdm run test` passes.
- [ ] Why is `pdm run python app.py` safer than `source .venv/bin/activate` then `python app.py`?

**Stretch:** Add a `lint` script that runs `python -c "import app; print('ok')"` and run it.

---

## Phase 5 — Reproducibility & git

- [ ] `git status` clean; `.venv/` **not** tracked; `pdm.lock` **is** tracked.
- [ ] You did (or can describe) the `clone → pdm install → pdm run test` loop.

---

## 🏆 Capstone

From a brand-new empty folder, recreate a working pdm project **from memory**:

1. `mkdir capstone && cd capstone`
2. `pdm init` (application, Python `>=3.9`)
3. Add a runtime dep (`pdm add httpx`) and a dev dep (`pdm add -dG dev pytest`).
4. Write a small module + a passing test.
5. Add `start` and `test` scripts to `pyproject.toml`.
6. `pdm run test` passes.
7. Add a `.gitignore`, `git init`, and commit.
8. (Optional) push to GitHub with `gh repo create`.

**Success =** you did all 8 without re-reading the lessons. If you got stuck on a step, revisit
that phase — that's exactly the bit worth reinforcing.

---

## Handy command cheat-sheet

```bash
pdm init                  # scaffold a project
pdm add <pkg>             # add a runtime dependency
pdm add -dG dev <pkg>     # add a dev-group dependency
pdm remove <pkg>          # remove a dependency
pdm list [--tree]         # list installed packages
pdm install               # install project + deps from lock (post-clone command)
pdm sync [--clean]        # match env to lock without re-resolving
pdm lock                  # re-resolve and rewrite pdm.lock
pdm update [<pkg>]        # upgrade deps and refresh lock
pdm run <cmd>             # run a command inside the project venv
pdm run <script-name>     # run a named script from [tool.pdm.scripts]
pdm info [--env]          # project/interpreter/venv info
pdm config                # view/set pdm configuration
```
