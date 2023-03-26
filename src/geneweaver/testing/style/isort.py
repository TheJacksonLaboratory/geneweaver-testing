"""Test that isort has been run on all Python files in the src and tests directories."""

import subprocess

__all__ = ["test_isort_src_dir", "test_isort_tests_dir"]


def test_isort_src_dir() -> None:
    """Test that isort has been run on all Python files in the src directory."""
    completed = subprocess.run(
        ["isort", "--check-only", "src"], capture_output=True, text=True
    )
    assert completed.returncode == 0, (
        "isort failed on src directory \n"
        + completed.stdout
        + completed.stderr
        + "Run 'isort src' to fix formatting."
    )


def test_isort_tests_dir() -> None:
    """Test that isort has been run on all Python files in the tests directory."""
    completed = subprocess.run(
        ["isort", "--check-only", "tests"], capture_output=True, text=True
    )
    assert completed.returncode == 0, (
        "isort failed on tests directory \n"
        + completed.stdout
        + completed.stderr
        + "Run 'isort tests' to fix formatting."
    )
