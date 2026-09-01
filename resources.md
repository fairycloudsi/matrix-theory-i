---
layout: page
title: Resources
permalink: /resources/
---

## Textbooks

### Primary

**Golub, G. H. and Van Loan, C. F., _Matrix Computations_, 4th edition.**
Johns Hopkins University Press, 2013.

The spine of this course. Van Loan maintains a companion page with material that is *not* in the
printed book and is free to download:

- [MATLAB M-files](https://www.cs.cornell.edu/cv/GVL4/M-Files/M-Home.htm) — code by chapter, with
  a complete zip. Chapters 10–11 are directly relevant to Week 15.
- [Errata](https://blogs.cornell.edu/charlievl/cvl_home/books/gvl4_errata/) — around forty
  corrections, indexed by page. Worth checking before you trust a formula.
- [Master bibliography](https://blogs.cornell.edu/charlievl/files/2021/11/GVL4_Bib.pdf) —
  deliberately omitted from the printed book to save space.
- [Table of contents](https://blogs.cornell.edu/charlievl/files/2021/11/GVL4_TableOfContents.pdf)
  and [preface](https://blogs.cornell.edu/charlievl/files/2021/11/GVL4_Preface.pdf).
- [All of Van Loan's book pages](https://blogs.cornell.edu/charlievl/cvl_home/books/)

> Note: the URL cited in most papers, `cs.cornell.edu/cv/GVL4/golubandvanloan.htm`, is dead.
> The links above are the current ones.

A Chinese edition of the 3rd edition, translated by Ya-Xiang Yuan and colleagues, is published by
Science Press.

### Supplementary

**Horn, R. A. and Johnson, C. R., _Matrix Analysis_, 2nd edition.** Cambridge University Press,
2013. The theory reference — strongest for Weeks 2–4 and Week 12, where the results matter more
than the algorithms.

**Deisenroth, M. P., Faisal, A. A. and Ong, C. S., _Mathematics for Machine Learning_.**
Cambridge University Press, 2020. [Free online.](https://mml-book.github.io/)
**Required for Week 16** — Golub & Van Loan has no matrix-calculus chapter, so the material on
differentials, gradients and backpropagation comes from Chapter 5 of this book.

## Courses worth following alongside

- [Cornell CS 6210, Matrix Computations](https://www.cs.cornell.edu/courses/cs6210/2025fa/)
  (David Bindel) — the book's home course. Complete lecture notes and homework are public on
  GitHub: [cs6210-f19](https://github.com/dbindel/cs6210-f19) is the most complete archive.
- [Stanford CME 302, Numerical Linear Algebra](https://ericdarve.github.io/NLA/) — originally
  Golub's own course.
- [MIT 18.335, Introduction to Numerical Methods](https://github.com/mitmath/18335) — excellent
  Julia notebooks.

## Software

Assignments are language-agnostic. Pick one and be fluent in it.

| | Reference implementations | Sparse and iterative |
|---|---|---|
| **Python** | NumPy / SciPy `scipy.linalg` | `scipy.sparse`, `scipy.sparse.linalg`, [PyAMG](https://github.com/pyamg/pyamg) |
| **MATLAB** | built in | built in |
| **Julia** | `LinearAlgebra` | `SparseArrays`, `IterativeSolvers.jl` |

Two habits worth forming from Week 1:

1. **Always have a reference to check against.** `scipy.linalg.lu`, `numpy.linalg.svd`, and their
   equivalents exist so you can verify your own code, not so you can avoid writing it.
2. **Compute in double precision** unless you are deliberately studying precision. In single
   precision the residual of a well-posed problem plateaus around `1e-6`, and a tolerance below
   that is unreachable — a very common way to convince yourself a correct solver is broken.

## Reference implementations to read

Reading good numerical code is underrated. These are worth an afternoon each:

- [LAPACK](https://www.netlib.org/lapack/) — the reference for everything in Weeks 5–14.
- [PyAMG](https://github.com/pyamg/pyamg) — readable Python algebraic multigrid, relevant to Week 15.
- [Van Loan's M-files](https://www.cs.cornell.edu/cv/GVL4/M-Files/M-Home.htm) — written for
  clarity rather than speed, which is exactly what you want while learning.
