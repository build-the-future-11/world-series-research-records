#!/usr/bin/env python3
"""Tiny mathematical reference checks from MATH_FOUNDATIONS. Not model training.

Uses only the standard library so the planning pack validates without a numerical stack.
"""
from __future__ import annotations

import math
import sys


def check_bounded_diagonal_update() -> None:
    theta = [1.0, -0.5]
    g = [0.2, -0.1]
    eta = 0.1
    d_diag = [1.5, 0.8]
    assert eta > 0 and all(x > 0 for x in d_diag)
    theta_next = [th - eta * d * gi for th, d, gi in zip(theta, d_diag, g)]
    expected = [1.0 - eta * 1.5 * 0.2, -0.5 - eta * 0.8 * (-0.1)]
    assert all(abs(a - b) < 1e-12 for a, b in zip(theta_next, expected))


def check_finite_mixture_moments() -> None:
    w = [0.3, 0.7]
    means = [0.0, 2.0]
    vars_ = [1.0, 0.5]
    s = sum(w)
    w = [x / s for x in w]
    mean = sum(wi * mi for wi, mi in zip(w, means))
    second = sum(wi * (vi + mi * mi) for wi, vi, mi in zip(w, vars_, means))
    var = second - mean * mean
    assert abs(sum(w) - 1.0) < 1e-12
    assert abs(mean - 1.4) < 1e-12
    assert var > 0


def check_sparse_laplacian_psd() -> None:
    # 3-node path Laplacian eigenvalues via characteristic structure
    # L = [[1,-1,0],[-1,2,-1],[0,-1,1]]
    # Known eigenvalues: 0, 1, 3
    L = [
        [1.0, -1.0, 0.0],
        [-1.0, 2.0, -1.0],
        [0.0, -1.0, 1.0],
    ]
    # Power-free PSD check: x^T L x >= 0 on a grid of simple vectors
    vectors = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0],
        [1.0, 1.0, 1.0],
        [1.0, -1.0, 0.0],
        [1.0, 0.0, -1.0],
        [1.0, -2.0, 1.0],
    ]
    for x in vectors:
        qx = 0.0
        for i in range(3):
            for j in range(3):
                qx += x[i] * L[i][j] * x[j]
        assert qx >= -1e-12, qx
    # Nullspace: constant vector
    assert abs(sum(L[0])) < 1e-12 and abs(sum(L[1])) < 1e-12 and abs(sum(L[2])) < 1e-12
    _ = math  # keep import intentional for future exact checks


def main() -> int:
    checks = [
        ("bounded_diagonal_update", check_bounded_diagonal_update),
        ("finite_mixture_moments", check_finite_mixture_moments),
        ("sparse_laplacian_psd", check_sparse_laplacian_psd),
    ]
    failed = 0
    print("world_series_cursor_pack check_math_reference")
    for name, fn in checks:
        try:
            fn()
            print(f"PASS {name}")
        except Exception as exc:  # noqa: BLE001
            failed += 1
            print(f"FAIL {name}: {exc}")
    if failed:
        print("STATUS: FAIL")
        return 1
    print("STATUS: PASS")
    print("NOTE: tiny reference examples only; not a theorem proof or trained model.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
