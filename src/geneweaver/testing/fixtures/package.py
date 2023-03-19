import pytest
import pathlib
import tomli
from typing import Optional

__all__ = [
    "project_root",
    "pyproject_toml_path",
    "git_dir",
    "pyproject_toml_contents",
    "package_name_from_pyproject",
    "package_submodule_name"
]


@pytest.fixture(scope="session")
def project_root(request) -> pathlib.Path:
    """Return the root directory of the project."""
    return pathlib.Path(request.config.rootdir)


@pytest.fixture(scope="session")
def pyproject_toml_path(project_root) -> pathlib.Path:
    """Find the pyproject.toml file, should be at the root of the git repository."""
    return project_root / "pyproject.toml"


@pytest.fixture(scope="session")
def git_dir(project_root) -> pathlib.Path:
    """Find the .git directory, should be at the root of the git repository."""
    return project_root / ".git"


@pytest.fixture(scope="session")
def pyproject_toml_contents(pyproject_toml_path) -> Optional[dict]:
    """

    :return:
    """
    return (
        read_pyproject_toml(pyproject_toml_path)
        if pyproject_toml_path.is_file()
        else None
    )


def read_pyproject_toml(pyproject_toml_path) -> dict:
    """
    Read the contents of a pyproject.toml file.
    :return: A dictionary containing the contents of the pyproject.toml file.
    """
    with open(pyproject_toml_path, "rb") as pyproject_file:
        return tomli.load(pyproject_file)


@pytest.fixture(scope="session")
def package_name_from_pyproject(pyproject_toml_contents) -> Optional[str]:
    """Get the package name from the pyproject.toml file."""
    return (
        pyproject_toml_contents["tool"]["poetry"]["name"]
        if pyproject_toml_contents
        else None
    )


@pytest.fixture(scope="session")
def package_submodule_name(package_name_from_pyproject) -> Optional[str]:
    """Get the package name from the pyproject.toml file."""
    return (
        package_name_from_pyproject.split("-")[-1]
        if package_name_from_pyproject
        else None
    )
