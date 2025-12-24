# Assignment 6 — Differentiable Programming and Geodesic Simulation

## Overview

### Exercise 01 — Radial Motion in an Effective Potential

Using **PyTorch**, simulate the radial trajectory of test particles moving in an effective gravitational potential.
The effective potential is defined as

$$
V_{\text{eff}}(r) = \frac{\ell^2}{2r^2} - \frac{r_s}{2r} - \frac{r_s \ell^2}{2 r^3}.
$$

The radial geodesic-like equation to use is

$$
\frac{1}{2}\left(\frac{dr}{ds}\right)^2 + V_{\text{eff}}(r) = E,
$$

with initial conditions

$$
r(0) = 10, r_s, \qquad \frac{dr}{ds}(0) = 0.1.
$$

Your task is to integrate this equation numerically between
$r = r_s$ and $r \to \infty$, for multiple choices of **angular momentum** $\ell$ and **Schwarzschild radius** $r_s$.

You must also determine the **possible circular orbits**, i.e. values of (r) such that

$$
\frac{dV_{\text{eff}}}{dr} = 0,
\qquad
E = V_{\text{eff}}(r).
$$

**Note:** The allowed region for particle motion must satisfy

$$
E - V_{\text{eff}}(r) \ge 0.
$$

---

## What to do

* Implement the full simulation and analysis inside **`src/Set_01.ipynb`**.
* Use **PyTorch tensors with gradients enabled** so that the integration and potential analysis are fully differentiable.
* For each choice of $\ell$ and $r_s$:

  * Plot the effective potential.
  * Numerically integrate the radial geodesic equation.
  * Identify allowed and forbidden regions.
  * Find circular orbits and assess their stability.
* Clearly comment derivations, numerical schemes, and all code cells.

---

## Submission rules

* Push your completed notebook to the **default branch** before the deadline.
* Do not rename the provided notebook or alter the directory structure.
* All plots must be generated automatically when the notebook is run.

---

## Collaboration & integrity

* This is an **individual assignment**.
* Cite all resources, papers, or external code that you use.
* Follow the academic integrity policies strictly.

---

If you'd like, I can also produce a **LaTeX version**, **GitHub-friendly markdown styling**, or a **more compact / more elaborate version**.
