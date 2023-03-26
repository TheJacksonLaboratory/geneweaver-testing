"""Test that certain key dependencies are installed and importable."""


def test_can_import_mypy() -> None:
    """Test that mypy is installed and importable."""
    import mypy

    assert mypy is not None


def test_can_import_ruff() -> None:
    """Test that ruff is installed and importable."""
    import ruff

    assert ruff is not None


def test_can_call_ruff_with_subprocess() -> None:
    """Test that ruff is installed and callable from subprocess."""
    import subprocess

    completed = subprocess.run(["ruff", "--version"], capture_output=True, text=True)
    assert completed.returncode == 0
    assert completed.stdout.startswith("ruff")


def test_can_import_pytest() -> None:
    """Test that pytest is installed and importable."""
    import pytest

    assert pytest is not None


def test_can_call_pytest_with_subprocess() -> None:
    """Test that pytest is installed and callable from subprocess."""
    import subprocess

    completed = subprocess.run(["pytest", "--version"], capture_output=True, text=True)
    assert completed.returncode == 0
    assert completed.stdout.startswith("pytest")
