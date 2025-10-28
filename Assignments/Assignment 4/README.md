[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/c_r6tmJp)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=21343317&assignment_repo_type=AssignmentRepo)
# MCTS Tic-Tac-Toe

## Goal

Implement a working **Monte Carlo Tree Search (MCTS)** agent and a **model interface** that can be evaluated by a frozen harness. You must preserve the public APIs and the directory structure.

---

## What you must implement

* `student_project/mcts.py`

  * Implement `mcts(root, net, n_simulations: int) -> int`
    **Return value:** the chosen move index in `[0..8]` for the current board.
* `student_project/models.py`

  * Implement a `Model` class (and optionally a `build_model()` factory)
  * Implement `load_state_dict(...)` so your weights can be loaded from `checkpoints/model.pth`

Everything else is **frozen** and used by the autograder.

---

## Do **NOT** edit

* `student_project/play.py`  *(contains the frozen `play_game(model1, model2, sims)` harness)*
* `student_project/game.py`
* `student_project/tree.py`
* Public function names or signatures
* Project layout and package names

Files marked “DO NOT EDIT” may be checked for integrity; edits can result in zero credit.

---

## Repository layout

```
student_project/
├─ __init__.py
├─ game.py               # DO NOT EDIT
├─ tree.py               # DO NOT EDIT
├─ play.py               # DO NOT EDIT (provides play_game)
├─ mcts.py               # ← YOUR MCTS IMPLEMENTATION
├─ models.py             # ← YOUR MODEL + build_model()
└─ train.py              # your training script
checkpoints/
└─ model.pth             # your weights (see Checkpoint format)
pyproject.toml
README.md
```

---

## Environment & installation

* Python ≥ 3.9

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -U pip
pip install -e .                   # installs the package in editable mode
```

---

## How your code is evaluated

1. We import your package under an alias and **do not** modify your files.
2. We create two models:

   * `model1 = build_model()` (or `Model()`), load `checkpoints/model.pth`
   * `model2 = ...` (another submission or a baseline)
3. We call the **frozen** harness:

   ```python
   from student_project.play import play_game
   winner = play_game(model1, model2, sims=100)   # 1 (X), -1 (O), 0 (draw)
   ```
4. We may run best-of-N matches with seeding and time limits.

You must ensure a **single game finishes in reasonable time** for the required `sims` (e.g., 100–400 simulations per move depending on rubric).

---

## Performance expectations

* The game must complete within the assignment’s time budget (per game)
* Use efficient data structures in the search tree
* Avoid copying whole boards unnecessarily; prefer in-place apply/undo where safe

---

## Submission checklist

* [ ] Do not edit frozen files (`play.py`, `game.py`, `tree.py`) or public signatures
* [ ] `mcts(root, net, n_simulations)` implemented and returns an **int move**
* [ ] `Model` (and optionally `build_model`) implemented
* [ ] `checkpoints/model.pth` present and loadable
* [ ] No large artifacts committed (datasets, logs, multi-GB files)

---

## Academic integrity

Write your own code for `mcts.py` and `models.py`. Cite any external resources in code comments if concepts influenced your implementation.
