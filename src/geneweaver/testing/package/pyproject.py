"""Test that pyproject.toml file is present and has required sections and contents."""
import pathlib
from typing import Optional

import pytest

__all__ = [
    "test_has_pyproject_toml",
    "test_has_tool_poetry_section",
    "test_pyproject_has_package_name",
    "test_pyproject_has_version",
    "test_pyproject_has_description",
    "test_pyproject_has_authors",
    "test_pyproject_has_license",
    "test_pyproject_has_readme",
    "test_poetry_has_packages_definition",
    "test_poetry_packages_defined_in_src_dir",
    "test_poetry_packages_in_geneweaver_namespace",
    "test_pyproject_has_ruff",
    "test_pyproject_ruff_has_required_rules",
]

POETRY_ERROR_MESSAGE = (
    "see https://python-poetry.org/docs/ for information on getting started with "
    "Python Poetry"
)


def test_has_pyproject_toml(project_root: pathlib.Path) -> None:
    """Test that the pyproject.toml file exists."""
    assert (project_root / "pyproject.toml").is_file(), (
        "pyproject.toml file not found, "
        "you may need to create one at the root of your git repository. "
        f"{POETRY_ERROR_MESSAGE}"
    )


def test_has_tool_poetry_section(pyproject_toml_contents: Optional[dict]) -> None:
    """Test that the pyproject.toml file has a [tool.poetry] section."""
    error_msg = (
        "pyproject.toml file does not have a [tool.poetry] section, "
        f"{POETRY_ERROR_MESSAGE}"
    )

    assert "tool" in pyproject_toml_contents, error_msg
    assert "poetry" in pyproject_toml_contents["tool"], error_msg


def test_pyproject_has_package_name(pyproject_toml_contents: Optional[dict]) -> None:
    """Test that the pyproject.toml file has a name."""
    assert "name" in pyproject_toml_contents["tool"]["poetry"], (
        "You need to define the package name as `name = ` "
        "in the [tool.poetry] section of the pyproject.toml file"
    )


def test_pyproject_has_version(pyproject_toml_contents: Optional[dict]) -> None:
    """Test that the pyproject.toml file has a version."""
    assert (
        "version" in pyproject_toml_contents["tool"]["poetry"]
    ), "pyproject.toml file does not have a version in the [tool.poetry] section"


def test_pyproject_has_description(pyproject_toml_contents: Optional[dict]) -> None:
    """Test that the pyproject.toml file has a description."""
    assert "description" in pyproject_toml_contents["tool"]["poetry"], (
        "pyproject.toml file does not have a description "
        "set in the [tool.poetry] section"
    )

    assert pyproject_toml_contents["tool"]["poetry"]["description"] != "", (
        "pyproject.toml file does not have a value for "
        "description in the [tool.poetry] section"
    )


def test_pyproject_has_authors(pyproject_toml_contents: Optional[dict]) -> None:
    """Test that the pyproject.toml file has authors."""
    assert (
        "authors" in pyproject_toml_contents["tool"]["poetry"]
    ), "pyproject.toml file does not have an authors section"
    assert (
        len(pyproject_toml_contents["tool"]["poetry"]["authors"]) > 0
    ), "pyproject.toml file does not have any authors listed"


def test_pyproject_has_license(pyproject_toml_contents: Optional[dict]) -> None:
    """Test that the pyproject.toml file has a license."""
    assert (
        "license" in pyproject_toml_contents["tool"]["poetry"]
    ), "pyproject.toml file does not have a license section"
    assert (
        pyproject_toml_contents["tool"]["poetry"]["license"] != ""
    ), "pyproject.toml file does not have a value for the license"
    assert (
        pyproject_toml_contents["tool"]["poetry"]["license"] == "Apache-2.0"
    ), "license in pyproject.toml file must be set to Apache-2.0"


def test_pyproject_has_readme(pyproject_toml_contents: Optional[dict]) -> None:
    """Test that the pyproject.toml file has a readme."""
    assert (
        "readme" in pyproject_toml_contents["tool"]["poetry"]
    ), "pyproject.toml file does not have a readme section"
    assert (
        pyproject_toml_contents["tool"]["poetry"]["readme"] == "README.md"
    ), 'readme in pyproject.toml file must be "README.md"'


def test_poetry_has_packages_definition(
    pyproject_toml_contents: Optional[dict],
) -> None:
    """Test that the pyproject.toml file has a package definition."""
    assert (
        "packages" in pyproject_toml_contents["tool"]["poetry"]
    ), "pyproject.toml file does not have a packages section"
    assert (
        len(pyproject_toml_contents["tool"]["poetry"]["packages"]) > 0
    ), "pyproject.toml file does not have any packages listed"


def test_poetry_packages_defined_in_src_dir(
    pyproject_toml_contents: Optional[dict],
) -> None:
    """Test that the pyproject.toml file has its package defined from src directory."""
    error_msg = (
        "all Geneweaver packages must be defined in the `src` directory, see "
        "https://python-poetry.org/docs/pyproject/#packages for more information."
    )
    for package in pyproject_toml_contents["tool"]["poetry"]["packages"]:
        assert "from" in package, (
            "pyproject.toml file does not have a `from` definition for a package. "
            f"{error_msg}"
        )
        assert package["from"] == "src", error_msg


def test_poetry_packages_in_geneweaver_namespace(
    pyproject_toml_contents: Optional[dict],
) -> None:
    """Test that the pyproject.toml has package defined in the geneweaver namespace."""
    for package in pyproject_toml_contents["tool"]["poetry"]["packages"]:
        assert (
            "include" in package
        ), "pyproject.toml file does not have an `include` definition for a package."
        include = package["include"].split("/")
        assert include[0] == "geneweaver", (
            "all Geneweaver packages must be located in the `geneweaver` namespace "
            "package. See https://peps.python.org/pep-0420/ for more information."
        )


def test_poetry_build_system_definition(
    pyproject_toml_contents: Optional[dict],
) -> None:
    """Test that the pyproject.toml file has a complete [build-system] section."""
    error_msg = (
        "pyproject.toml file does not have a complete [build-system] section, see"
        "https://python-poetry.org/docs/pyproject/#poetry-and-pep-517 "
        "for information on the [build-system] section and Python Poetry"
    )
    assert "build-system" in pyproject_toml_contents, error_msg
    assert "requires" in pyproject_toml_contents["build-system"], error_msg
    assert (
        "poetry-core" == pyproject_toml_contents["build-system"]["requires"]
    ), error_msg
    assert "build-backend" in pyproject_toml_contents["build-system"], error_msg
    assert (
        "poetry.masonry.api" == pyproject_toml_contents["build-system"]["build-backend"]
    ), error_msg


def test_pyproject_has_ruff(pyproject_toml_contents: Optional[dict]) -> None:
    """Test that the pyproject.toml file has a ruff section."""
    assert "ruff" in pyproject_toml_contents["tool"], (
        "pyproject.toml file does not have a [ruff] section see"
        "https://beta.ruff.rs/docs/configuration/ for more information."
    )


REQUIRED_RUFF_RULES = {
    "F": "PyFlakes",
    "E": "PyCodeStyle Errors",
    "W": "PyCodeStyle Warnings",
    "A": "Builtins",
    "C90": "McCabe Complexity",
    "N": "PEP8 Naming",
    "B": "Bandit (security)",
    "ANN": "Flake8 Annotations",
    "D": "PyDocStyle",
    "I": "Isort",
    "ERA": "Eradicate (dead code)",
    "PD": "Pandas Specific Linting",
    "NPY": "NumPy Speficic Linting",
    "PT": "PyTest Style",
}


@pytest.mark.parametrize("rule", REQUIRED_RUFF_RULES.keys())
def test_pyproject_ruff_has_required_rules(
    pyproject_toml_contents: Optional[dict], rule: str
) -> None:
    """Test that the pyproject.toml file has the required rules enabled."""
    assert "select" in pyproject_toml_contents["tool"]["ruff"], (
        "pyproject.toml [ruff.tool] section missing 'select' key.\n"
        "Geneweaver requires using rules: \n"
        "[tool.ruff]\n"
        f"select = {list(REQUIRED_RUFF_RULES.keys())}"
    )

    assert rule in pyproject_toml_contents["tool"]["ruff"]["select"], (
        f"pyproject.toml [tool.ruff] select = section missing rule `{rule}.\n"
        "Geneweaver requires using rules: \n"
        "[tool.ruff]\n"
        f"select = {list(REQUIRED_RUFF_RULES.keys())}"
    )
