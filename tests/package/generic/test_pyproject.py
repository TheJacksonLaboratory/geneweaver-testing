"""Test the geneweaver.testing.package.generic.pyproject module."""
from typing import Optional
from unittest.mock import patch

import pytest
from geneweaver.testing.package.generic.pyproject import (
    _check_controller_per_file_ignore,
)
from geneweaver.testing.package.generic.pyproject import (
    test_poetry_build_system_definition as t_poetry_build_system_definition,
)
from geneweaver.testing.package.generic.pyproject import (
    test_ruff_per_files_ignores as t_ruff_per_files_ignores,
)


def test_test_poetry_build_system_definition():
    """Test with a valid pyproject.toml content."""
    valid_pyproject_content = {
        "build-system": {
            "requires": ["poetry-core"],
            "build-backend": "poetry.masonry.api",
        }
    }
    t_poetry_build_system_definition(valid_pyproject_content)


def test_controller_per_file_ignore():
    """Test the _check_controller_per_file_ignore function."""
    valid_per_files_ignore = {
        "tests/*": ["test_*.py", "tests/*"],
        "src/geneweaver/api/controllers/*": ["B008"],
        "src/*": ["ANN101", "ANN102", "ANN103", "ANN204", "ANN205", "ANN206"],
    }
    _check_controller_per_file_ignore(valid_per_files_ignore)


PER_FILES_IGNORES_MSG = "custom error message for per-files-ignores"
IGNORING_ALLOWED_WARN = "custom warning message for ignoring allowed"


@pytest.mark.parametrize(
    "pyproject_toml_contents",
    [
        {"tool": {"ruff": {"per-file-ignores": ["src/*"]}}},
        {"tool": {"ruff": {"per-file-ignores": ["tests/*"]}}},
        {"tool": {"ruff": {"per-file-ignores": ["src/*", "tests/*"]}}},
        {"tool": {"ruff": {"per-file-ignores": ["src/*", "tests/*", "controllers/*"]}}},
    ],
)
def test_test_ruff_per_files_ignores(
    pyproject_toml_contents: Optional[dict],
):
    """Test different scenarios of pyproject.toml contents for ruff configuration."""
    with patch(
        "geneweaver.testing.package.generic.pyproject._check_tests_per_file_ignore"
    ) as mock_test_ignore, patch(
        "geneweaver.testing.package.generic.pyproject._check_src_per_file_ignore"
    ) as mock_src_ignore, patch(
        "geneweaver.testing.package.generic.pyproject._check_controller_per_file_ignore"
    ) as mock_controller_ignore:
        # Call the function under test
        t_ruff_per_files_ignores(pyproject_toml_contents)

        # Assert that the mocks were called as expected
        if (
            pyproject_toml_contents
            and "per-file-ignores"
            in pyproject_toml_contents.get("tool", {}).get("ruff", {})
        ):
            per_files_ignores = pyproject_toml_contents["tool"]["ruff"][
                "per-file-ignores"
            ]
            if "tests/*" in per_files_ignores:
                mock_test_ignore.assert_called_with(per_files_ignores)
            if "src/*" in per_files_ignores:
                mock_src_ignore.assert_called_with(per_files_ignores)
            if len(per_files_ignores) == 3:
                mock_controller_ignore.assert_called_with(per_files_ignores)
