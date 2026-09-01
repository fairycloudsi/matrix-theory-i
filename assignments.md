---
layout: page
title: Assignments and Grading
permalink: /assignments/
---

## Grading

<div class="table-scroll" markdown="0">
<table>
  <thead><tr><th>Component</th><th class="num">Weight</th><th>When</th></tr></thead>
  <tbody>
    <tr><td>Regular quizzes (four, 15 minutes each)</td><td class="num">20%</td><td>Weeks 2, 6, 10, 13</td></tr>
    <tr><td>Programming assignments (five)</td><td class="num">30%</td><td>Weeks 4, 7, 10, 13, 15</td></tr>
    <tr><td>Final examination</td><td class="num">50%</td><td>Examination period</td></tr>
  </tbody>
</table>
</div>

## The rule that applies to every assignment

**Implement it, then check it against a reference implementation.** Where your result and the
library's disagree, work out why before you move on. That gap is where the actual learning is —
a disagreement in the fifteenth digit and a disagreement in the second have very different
causes, and telling them apart is the skill this course is trying to build.

Submissions are code plus a short report. The report should state what you implemented, how you
verified it, and what you found — not restate the algorithm.

## The five assignments

### A1 · Norms and conditioning · due Week 4 · 6%

Implement a condition-number estimator. Construct matrices of increasing condition number and
demonstrate empirically that `κ(A)` predicts the error growth in a solved system. Show a case
with a tiny residual and a large error.

*Covers Weeks 2–4. Reference: §2.3, §2.6–2.7.*

### A2 · LU and Cholesky · due Week 7 · 6%

Write LU with partial pivoting and Cholesky from scratch. Verify both against a library routine.
Measure the growth factor on random and on adversarial matrices, and exhibit a matrix where
elimination without pivoting fails.

*Covers Weeks 5–7. Reference: §3.2–3.4, §4.2.*

### A3 · QR and least squares · due Week 10 · 6%

Implement Householder QR. Solve the same ill-conditioned least squares problem three ways —
normal equations, QR, and SVD — and explain the accuracy difference you observe in terms of
`κ(AᵀA) = κ(A)²`.

*Covers Weeks 9–10. Reference: §5.1–5.3.*

### A4 · Eigenvalues · due Week 13 · 6%

Implement power iteration and shifted inverse iteration. Apply them to a real problem: a graph
Laplacian, or a PageRank instance on a graph you construct. Compare convergence rates against
the theoretical prediction from the eigenvalue gap.

*Covers Weeks 12–13. Reference: §7.3, §8.2.*

### A5 · Sparse and iterative methods · due Week 15 · 6%

Implement conjugate gradient using only matrix–vector products — never form the matrix. Run it
with and without a simple preconditioner (Jacobi, or incomplete Cholesky) and plot the residual
history against the `√κ` bound.

*Covers Week 15. Reference: §11.2–11.3, §11.5.*

## Quizzes

Four 15-minute quizzes in Weeks 2, 6, 10 and 13, each covering the previous fortnight. They test
whether the definitions and the main theorems are at your fingertips — no computation that needs
a machine.

## Course project (optional, in place of A5)

If you would rather go deeper than broad, propose a project instead of the fifth assignment. Good
starting points are the topics the course deliberately omits: the matrix exponential and other
matrix functions (Ch. 9), multigrid (§11.6), tensor decompositions (§12.4–12.5), or randomized
low-rank approximation. Proposals due Week 11; presentations in Week 16.
