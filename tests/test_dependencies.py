"""
Test that certain key dependencies are installed and importable.
"""


def test_can_import_mypy():
    import mypy

    assert mypy is not None


def test_can_import_ruff():
    import ruff

    assert ruff is not None


def test_can_import_pytest():
    import pytest

    assert pytest is not None
