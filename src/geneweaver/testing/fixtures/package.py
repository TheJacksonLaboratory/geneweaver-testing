"""Fixtures relating to the package and its structure."""
import pathlib
from typing import Optional

import pytest
import tomli
from _pytest.fixtures import FixtureRequest

__all__ = [
    "project_root",
    "pyproject_toml_path",
    "git_dir",
    "pyproject_toml_contents",
    "package_name_from_pyproject",
    "package_submodule_name",
    "is_tool_package",
]


@pytest.fixture(scope="session")
def project_root(request: FixtureRequest) -> pathlib.Path:
    """Return the root directory of the project."""
    return pathlib.Path(request.config.rootdir)


@pytest.fixture(scope="session")
def pyproject_toml_path(project_root: pathlib.Path) -> pathlib.Path:
    """Find the pyproject.toml file, should be at the root of the git repository."""
    return project_root / "pyproject.toml"


@pytest.fixture(scope="session")
def git_dir(project_root: pathlib.Path) -> pathlib.Path:
    """Find the .git directory, should be at the root of the git repository."""
    return project_root / ".git"


@pytest.fixture(scope="session")
def pyproject_toml_contents(pyproject_toml_path: pathlib.Path) -> Optional[dict]:
    """Read the contents of the pyproject.toml file."""
    return (
        read_pyproject_toml(pyproject_toml_path)
        if pyproject_toml_path.is_file()
        else None
    )


def read_pyproject_toml(pyproject_toml_path: pathlib.Path) -> dict:
    """Open and read the contents of a pyproject.toml file.

    :return: A dictionary containing the contents of the pyproject.toml file.
    """
    with open(pyproject_toml_path, "rb") as pyproject_file:
        return tomli.load(pyproject_file)


@pytest.fixture(scope="session")
def package_name_from_pyproject(
    pyproject_toml_contents: Optional[dict],
) -> Optional[str]:
    """Get the package name from the pyproject.toml file."""
    return (
        pyproject_toml_contents["tool"]["poetry"]["name"]
        if pyproject_toml_contents
        else None
    )


@pytest.fixture(scope="session")
def package_submodule_name(package_name_from_pyproject: Optional[str]) -> Optional[str]:
    """Get the package name from the pyproject.toml file."""
    return (
        "_".join(package_name_from_pyproject.split("-")[1:])
        if package_name_from_pyproject
        else None
    )


@pytest.fixture(scope="session")
def is_tool_package(project_root: Optional[str]) -> bool:
    """Return True if the package is a tool package."""
    return (project_root / "src" / "geneweaver" / "tools").is_dir()
