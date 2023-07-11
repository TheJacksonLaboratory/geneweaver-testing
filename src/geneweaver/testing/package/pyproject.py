"""Test that pyproject.toml file is present and has required sections and contents."""
from typing import Optional

__all__ = [
    "test_poetry_packages_in_geneweaver_namespace",
]


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
