---
layout: page
title: Matrix Theory and Applications I
---

<div class="hero" markdown="1">
The matrix is the data structure of modern AI. This course is about understanding it,
computing with it, and — the part that is usually skipped — computing with it *reliably*.

Sixteen weeks built on **Golub & Van Loan, _Matrix Computations_, 4th edition**, with every
week tied to specific sections of the book and to a problem you will meet in machine learning,
vision, or scientific computing.
</div>

<ul class="facts">
  <li><span class="k">Course code</span><span class="v">{{ site.course.code }}</span></li>
  <li><span class="k">Contact hours</span><span class="v">{{ site.course.hours }}</span></li>
  <li><span class="k">Format</span><span class="v">{{ site.course.format }}</span></li>
  <li><span class="k">Instructor</span><span class="v">{{ site.course.instructor }}</span></li>
  <li><span class="k">Meetings</span><span class="v">{{ site.course.meeting }}</span></li>
  <li><span class="k">Office hours</span><span class="v">{{ site.course.office_hours }}</span></li>
</ul>

<ul class="cards">
  <li><a class="card" href="{{ '/schedule/' | relative_url }}">
    <strong>Schedule</strong>
    <span>All 16 weeks, with readings and links to each week's materials.</span></a></li>
  <li><a class="card" href="{{ '/assignments/' | relative_url }}">
    <strong>Assignments</strong>
    <span>Five programming assignments, four quizzes, and how you are graded.</span></a></li>
  <li><a class="card" href="{{ '/resources/' | relative_url }}">
    <strong>Resources</strong>
    <span>Textbooks, the author's own code and errata, and software setup.</span></a></li>
</ul>

## What you will be able to do

1. **Analyse** — state and use the core theorems of matrix analysis, and judge when a matrix
   problem is well- or ill-conditioned.
2. **Compute** — select and derive an appropriate decomposition or iterative method, and reason
   about its cost and stability.
3. **Implement** — turn an algorithm from the board into working code, and verify it against a
   reference implementation.
4. **Apply** — recognise the matrix problem hiding inside a machine learning, vision, or
   scientific computing task, and solve it.

## How the course is built

The five parts run in the book's own order, which is not the order most syllabi use:

- **Weeks 1–4 · Foundations.** Matrix multiplication as a computation, then norms, the SVD,
  and conditioning.
- **Weeks 5–8 · Linear systems.** LU, pivoting and stability, positive definite and banded
  systems, then structured solvers.
- **Weeks 9–11 · Least squares.** QR, the full-rank problem, then rank deficiency and
  regularization.
- **Weeks 12–14 · Eigenvalues.** Theory and perturbation, the QR algorithm, then the symmetric
  case — where the SVD is finally computed.
- **Weeks 15–16 · Scale and synthesis.** Sparse and iterative methods, then matrix calculus
  and backpropagation.

> **Why the SVD appears twice.** Golub and Van Loan introduce the SVD on page 76, in the
> *analysis* chapter, and defer its computation 410 pages to §8.6. We follow them. What the SVD
> *is* needs only norms, so it lands in Week 3 and is then available as an instrument for the
> rest of the course; how to compute it *stably* is an algorithm that cannot be motivated before
> QR iteration, so it lands in Week 14.

## Prerequisites

Linear algebra, calculus, and a first course in numerical analysis. You should be comfortable
writing and debugging code in MATLAB, Python, or Julia — the assignments are language-agnostic,
but every one of them requires you to implement something and check it.
