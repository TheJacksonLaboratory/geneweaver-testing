"""Test that the package structure is correct."""

__all__ = [
    "test_has_geneweaver_directory",
    "test_geneweaver_dir_is_namespace_package",
    "test_has_package_directory",
]

import pathlib


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
    project_root: pathlib.Path, package_submodule_name: str, is_tool_package: bool
) -> None:
    """Test that the package directory exists."""
    root_path = project_root / "src" / "geneweaver"
    if is_tool_package:
        root_path = root_path / "tools"

    assert (root_path / package_submodule_name).is_dir(), (
        f'"{package_submodule_name}" package directory '
        f'expected in "geneweaver" namespace'
    )
