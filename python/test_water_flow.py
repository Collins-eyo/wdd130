# test_water_flow.py by Collins Ekpenyong Asikpo

from pytest import approx
import pytest
from water_flow import water_column_height, pressure_gain_from_water_height, pressure_loss_from_pipe, \
    pressure_loss_from_fittings, reynolds_number, pressure_loss_from_pipe_reduction

# Task 8: Testing Pressure Loss from Fittings Function
def test_pressure_loss_from_fittings():
    assert pressure_loss_from_fittings(0.1, 2.0) == approx(0.1, abs=0.001)
    assert pressure_loss_from_fittings(0.05, 3.0) == approx(0.225, abs=0.001)
    assert pressure_loss_from_fittings(0.2, 1.5) == approx(0.45, abs=0.001)

# Task 9: Testing Reynolds Number Function
def test_reynolds_number():
    assert reynolds_number(0.05, 2.0, 1e-5) == approx(50000.0, abs=0.001)
    assert reynolds_number(0.1, 3.0, 2e-5) == approx(60000.0, abs=0.001)
    assert reynolds_number(0.2, 1.5, 1.5e-5) == approx(40000.0, abs=0.001)

# Task 10: Testing Pressure Loss from Pipe Reduction Function
def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.1, 0.05, 10.0, 2.0) == approx(0.5, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.2, 0.1, 15.0, 3.0) == approx(1.5, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.15, 0.1, 8.0, 1.5) == approx(0.6, abs=0.001)

# Task 11: Run all tests
if __name__ == "__main__":
    pytest.main()
