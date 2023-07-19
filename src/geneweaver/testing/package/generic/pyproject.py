"""Generic tests that pyproject.toml has required sections and contents."""
import pathlib
import warnings
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
    "test_poetry_has_homepage",
    "test_poetry_has_repository",
    "test_poetry_packages_defined_in_src_dir",
    "test_pyproject_has_ruff",
    "test_pyproject_ruff_has_required_rules",
    "test_pyproject_ruff_does_not_have_other_specifications",
    "test_ruff_per_files_ignores",
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


def test_poetry_has_homepage(
    pyproject_toml_contents: Optional[dict],
) -> None:
    """Test that the pyproject.toml file has a homepage set."""
    assert (
        "homepage" in pyproject_toml_contents["tool"]["poetry"]
    ), "pyproject.toml file does not have a homepage section"
    assert (
        pyproject_toml_contents["tool"]["poetry"]["homepage"] != ""
    ), "pyproject.toml file does not have a value for the homepage"


def test_poetry_has_repository(
    pyproject_toml_contents: Optional[dict],
) -> None:
    """Test that the pyproject.toml file has a repository set."""
    assert (
        "repository" in pyproject_toml_contents["tool"]["poetry"]
    ), "pyproject.toml file does not have a repository section"
    assert (
        pyproject_toml_contents["tool"]["poetry"]["repository"] != ""
    ), "pyproject.toml file does not have a value for the repository"


def test_poetry_packages_defined_in_src_dir(
    pyproject_toml_contents: Optional[dict],
) -> None:
    """Test that the pyproject.toml file has its package defined from src directory."""
    error_msg = (
        "all packages must be defined in the `src` directory, see "
        "https://python-poetry.org/docs/pyproject/#packages for more information."
    )
    for package in pyproject_toml_contents["tool"]["poetry"]["packages"]:
        assert "from" in package, (
            "pyproject.toml file does not have a `from` definition for a package. "
            f"{error_msg}"
        )
        assert package["from"] == "src", error_msg


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

RUFF_ERROR_MSG = (
    "\n\npyproject.toml `ruff` section should look like: \n"
    "[tool.ruff]\n"
    f"select = {list(REQUIRED_RUFF_RULES.keys())}"
)


@pytest.mark.parametrize("rule", REQUIRED_RUFF_RULES.keys())
def test_pyproject_ruff_has_required_rules(
    pyproject_toml_contents: Optional[dict], rule: str
) -> None:
    """Test that the pyproject.toml file has the required rules enabled."""
    assert "ruff" in pyproject_toml_contents["tool"], (
        "pyproject.toml file does not have a [tool.ruff] section\n"
        "see https://beta.ruff.rs/docs/configuration/ for more information."
    ) + RUFF_ERROR_MSG

    assert "select" in pyproject_toml_contents["tool"]["ruff"], (
        "pyproject.toml [ruff.tool] section missing 'select' key."
    ) + RUFF_ERROR_MSG

    assert rule in pyproject_toml_contents["tool"]["ruff"]["select"], (
        f"pyproject.toml [tool.ruff] select = section missing rule `{rule}`."
    ) + RUFF_ERROR_MSG


PER_FILES_IGNORES_MSG = (
    "pyproject.toml [tool.ruff.per-file-ignores] is only allowed to specify "
    "tests/*.\nIt should look like: \n\n"
    '[tool.ruff.per-file-ignores]\n"tests/*" = ["ANN201"]\n\n'
    "You can optionally ignore argument type annotations (`ANN001`), but it is "
    "not recommended.\n"
)

IGNORING_ALLOWED_WARN = (
    "\n\nGeneweaver allows ignoring argument and return type annotations in "
    "tests.\nMost tests return nothing, and so it is not necessary to specify "
    "`-> None` for every test.\n"
    "It is recommended not to ignore argument type annotations, but is allowed "
    "at the discretion of the developer.\n\n"
    "To ignore return type annotations in test, add the following to you "
    "pyproject.toml file:\n\n"
    '[tool.ruff.per-file-ignores]\n"tests/*" = ["ANN201"]\n'
    "To ignore return and argument type annotations in test, add the following "
    "to you pyproject.toml file:\n\n"
    '[tool.ruff.per-file-ignores]\n"tests/*" = ["ANN001", "ANN201"]\n'
)


def test_pyproject_ruff_does_not_have_other_specifications(
    pyproject_toml_contents: Optional[dict],
) -> None:
    """Test that the pyproject.toml file does not have other specifications."""
    assert "ruff" in pyproject_toml_contents["tool"], (
        "pyproject.toml file does not have a [tool.ruff] section\n"
        "see https://beta.ruff.rs/docs/configuration/ for more information."
    ) + RUFF_ERROR_MSG

    assert "select" in pyproject_toml_contents["tool"]["ruff"], (
        "pyproject.toml [ruff.tool] section missing 'select' key."
    ) + RUFF_ERROR_MSG

    assert len(pyproject_toml_contents["tool"]["ruff"]["select"]) == len(
        REQUIRED_RUFF_RULES.keys()
    ), (
        "pyproject.toml [tool.ruff] select = section has other specifications."
    ) + RUFF_ERROR_MSG

    ruff_section_length = 1

    # You can optionally ignore argument and return type annotations in tests.
    per_files_ignores = pyproject_toml_contents["tool"]["ruff"].get("per-file-ignores")
    if per_files_ignores:
        ruff_section_length = 2

    assert len(pyproject_toml_contents["tool"]["ruff"]) == ruff_section_length, (
        "pyproject.toml [tool.ruff] section has non-standard specifications."
    ) + RUFF_ERROR_MSG


def test_ruff_per_files_ignores(
    pyproject_toml_contents: Optional[dict],
) -> None:
    """Ensure that the ruff configuration only ignores allowed errors."""
    # You can optionally ignore argument and return type annotations in tests.
    per_files_ignores = pyproject_toml_contents["tool"]["ruff"].get("per-file-ignores")
    if per_files_ignores:
        assert len(per_files_ignores) == 1, PER_FILES_IGNORES_MSG
        assert "tests/*" in per_files_ignores, PER_FILES_IGNORES_MSG
        assert len(per_files_ignores["tests/*"]) in (1, 2), PER_FILES_IGNORES_MSG
        for ignore in per_files_ignores["tests/*"]:
            assert ignore in ("ANN201", "ANN001"), PER_FILES_IGNORES_MSG
    else:
        warnings.warn(IGNORING_ALLOWED_WARN)  # noqa: B028
