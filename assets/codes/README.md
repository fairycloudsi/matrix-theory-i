# Code

Numerical companions to the lectures. Each script checks the *identities* shown on the
slides — it verifies the mathematics, not hardware performance claims.

| File | Week | Run it |
|---|---|---|
| `lecture1_computation_checks.py` | Week 1 — Matrix multiplication (§1.1–1.6) | `python3 lecture1_computation_checks.py` |

Requires NumPy only:

```bash
pip install numpy
python3 lecture1_computation_checks.py
```

Every example is asserted against its expected value with `assert_allclose`, so the script
either prints each result and ends with `All numerical checks passed.` or fails loudly on
the first discrepancy. If you modify an example and it still passes, you have not broken
the identity; if it fails, read the traceback — the label tells you which slide.
