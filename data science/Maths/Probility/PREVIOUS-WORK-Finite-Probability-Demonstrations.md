# Previous Work: Finite Probability Demonstrations

> This project is referenced here as a backup / prior-work link. It was completed earlier and is kept as a foundation piece showing applied probability fundamentals in Python.

**Repository:** [Hitesh-Ojha/Finite-Probability-Demonstrations](https://github.com/Hitesh-Ojha/Finite-Probability-Demonstrations)

## Summary

A single-file Python script that visualizes core finite-probability concepts using `matplotlib` bar charts, computed entirely from basic set operations (no probability libraries used).

## Concepts Demonstrated

- Marginal probability — P(A), P(B), P(Art)
- Joint probability — P(A ∩ Art), P(B ∩ Art)
- Conditional probability — P(A|Art), P(B|Art)
- Union probability (inclusion-exclusion) — P(A ∪ Art), P(B ∪ Art)
- Complement — P(¬A), P(¬B)
- Law of total probability — P(Art) = P(Art|A)·P(A) + P(Art|B)·P(B)
- Bayes' theorem — P(A|Art) and the reverse conditional P(Art|A)

## Example Scenario

- Universe (sample space S): 9 students numbered 1–9
- Group A: students {1,2,3,4,5} (5 members)
- Group B: students {6,7,8,9} (4 members, disjoint from A)
- Art club: students {4,5,6,8,9} (5 members, overlapping both groups)

The script outputs seven aligned bar charts illustrating how these probability rules play out on this concrete finite example.

## Notable Implementation Details

- Clean, readable function names: `intersection_size`, `joint_probability`, `conditional_probability`, `bayes_theorem`, etc.
- Consistent use of Python set operations (`set(A) & set(B)`) for intersections
- Both directions of conditional probability shown side-by-side in the Bayes panel
- Educational color coding (blue & orange) distinguishing P(A|Art) vs P(Art|A)
- Minimal dependencies: only `matplotlib`
- Self-contained, single-file script

## Requirements & Usage

```bash
pip install matplotlib
git clone https://github.com/Hitesh-Ojha/Finite-Probability-Demonstrations.git
cd Finite-Probability-Demonstrations
python "Finite Probability Demonstrations.py"
```

## Why It's Linked Here

This repo demonstrates foundational, from-scratch probability reasoning (set-theoretic implementations of marginal/conditional/Bayesian probability) done prior to the current project. It's kept as a reference point for probability fundamentals rather than being merged into the active codebase.

---
*Linked as prior work — see the [live repository](https://github.com/Hitesh-Ojha/Finite-Probability-Demonstrations) for source code and commit history.*
