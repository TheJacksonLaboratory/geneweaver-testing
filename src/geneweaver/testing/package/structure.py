"""Test that the package structure is correct."""

__all__ = [
    "test_has_src_directory",
    "test_has_geneweaver_directory",
    "test_geneweaver_dir_is_namespace_package",
    "test_has_package_directory",
    "test_has_tests_directory",
    "test_has_contributing_file",
]

import pathlib


def test_has_src_directory(project_root: pathlib.Path) -> None:
    """Test that the src directory exists."""
    assert (
        project_root / "src"
    ).is_dir(), '"src" directory expected at root of git repository'


def test_has_geneweaver_directory(project_root: pathlib.Path) -> None:
    """Test that the geneweaver namespace exists."""
    assert (
        project_root / "src" / "geneweaver"
    ).is_dir(), '"geneweaver" namespace expected in "src" directory'


def test_geneweaver_dir_is_namespace_package(project_root: pathlib.Path) -> None:
    """Test that the geneweaver namespace is a namespace package."""
    assert (project_root / "src" / "geneweaver" / "__init__.py").is_file() is False, (
        '"geneweaver" namespace is not a namespace package, '
        "it should not have an __init__.py file"
    )


def test_has_package_directory(
    project_root: pathlib.Path, package_submodule_name: str
) -> None:
    """Test that the package directory exists."""
    assert (project_root / "src" / "geneweaver" / package_submodule_name).is_dir(), (
        f'"{package_submodule_name}" package directory '
        f'expected in "geneweaver" namespace'
    )


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
