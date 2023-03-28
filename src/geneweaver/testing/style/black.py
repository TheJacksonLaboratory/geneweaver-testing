"""Test that the src and tests directories had been formatted with black."""

import subprocess

__all__ = ["test_black_src_dir", "test_black_tests_dir"]


def test_black_src_dir() -> None:
    """Test that the src directory has been formatted with black."""
    completed = subprocess.run(
        ["black", "--check", "src"], capture_output=True, text=True
    )
    assert completed.returncode == 0, (
        "Black Formatting failed on src directory \n"
        + completed.stdout
        + completed.stderr
        + "Run 'black src' to fix formatting."
    )


def test_black_tests_dir() -> None:
    """Test that the tests directory has been formatted with black."""
    completed = subprocess.run(
        ["black", "--check", "tests"], capture_output=True, text=True
    )
    assert completed.returncode == 0, (
        "Black Formatting Failed on tests directory \n"
        + completed.stdout
        + completed.stderr
        + "Run 'black tests' to fix formatting."
    )
