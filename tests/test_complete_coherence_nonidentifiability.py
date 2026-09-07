import numpy as np
import pytest
from conditional_output_no_go import full_disk_witness, qubit_unitary_for_target_chi


def test_full_disk_grid():
    radii = np.linspace(0.0, 1.0, 11)
    phases = np.linspace(-np.pi, np.pi, 25)
    worst = 0.0
    for r in radii:
        for phi in phases:
            z = r * np.exp(1j * phi)
            row = full_disk_witness(z)
            worst = max(worst, row["target_residual"], row["conditional_output_residual"])
            assert row["target_reached"]
            assert row["outputs_identical"]
    assert worst < 1e-12


def test_outside_disk_rejected():
    with pytest.raises(ValueError):
        qubit_unitary_for_target_chi(1.01 + 0j)
