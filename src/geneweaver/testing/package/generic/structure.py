"""Generic tests that the package structure is correct."""

__all__ = [
    "test_has_src_directory",
    "test_has_tests_directory",
    "test_has_contributing_file",
    "test_has_readme_file",
    "test_has_license_file",
]

import pathlib


def test_has_src_directory(project_root: pathlib.Path) -> None:
    """Test that the src directory exists."""
    assert (
        project_root / "src"
    ).is_dir(), '"src" directory expected at root of git repository'


def test_has_tests_directory(project_root: pathlib.Path) -> None:
    """Test that the tests directory exists."""
    assert (
        project_root / "tests"
    ).is_dir(), '"tests" directory expected at root of git repository'


def test_has_contributing_file(project_root: pathlib.Path) -> None:
    """Test that the CONTRIBUTING.md file exists."""
    assert (project_root / "CONTRIBUTING.md").is_file(), (
        "CONTRIBUTING.md file not found, "
        "you may need to create one at the root of your git repository"
    )


def test_has_readme_file(project_root: pathlib.Path) -> None:
    """Test that the README.md file exists."""
    assert (project_root / "README.md").is_file(), (
        "README.md file not found, "
        "you may need to create one at the root of your git repository"
    )


def test_has_license_file(project_root: pathlib.Path) -> None:
    """Test that the LICENSE file exists."""
    assert (project_root / "LICENSE").is_file(), (
        "LICENSE file not found, "
        "you may need to create one at the root of your git repository"
    )
