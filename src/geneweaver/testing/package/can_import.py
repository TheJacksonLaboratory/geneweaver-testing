"""Tests that verify that the package can be imported as expected."""
import importlib
from typing import Optional

__all__ = [
    "test_can_import_absolute",
    "test_can_import_relative",
    "test_can_import_geneweaver",
    "test_submodule_available_from_namespace_package",
]

ERROR_MESSAGE = (
    "The package is not importable. Review available test traceback to identify "
    "the cause. If you are unable to identify the cause from the traceback, "
    "we recommend opening a python terminal and attempting to import the "
    "package manually."
)


def test_can_import_absolute(
    package_submodule_name: Optional[str], is_tool_package: bool
) -> None:
    """Test that we can import the package from the top level namespace."""
    root_module = "geneweaver.tools" if is_tool_package else "geneweaver"
    module = importlib.import_module(f"{root_module}.{package_submodule_name}")
    assert module is not None, ERROR_MESSAGE


def test_can_import_relative(
    package_submodule_name: Optional[str], is_tool_package: bool
) -> None:
    """Test that we can import the package relative to the geneweaver namespace."""
    root_module = "geneweaver.tools" if is_tool_package else "geneweaver"
    module = importlib.import_module(f".{package_submodule_name}", root_module)
    assert module is not None, ERROR_MESSAGE


def test_can_import_geneweaver() -> None:
    """Test that we can import geneweaver top level namespace package."""
    # Note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    # MyPY Error: Skipping analyzing "geneweaver": module is installed,
    # but missing library stubs or py.typed marker
    import geneweaver  # type: ignore

    assert geneweaver is not None, ERROR_MESSAGE


def test_submodule_available_from_namespace_package(
    package_submodule_name: Optional[str], is_tool_package: bool
) -> None:
    """Test that the package is available from the geneweaver namespace."""
    import geneweaver

    if is_tool_package:
        package_submodule_name = f"tools.{package_submodule_name}"

    assert hasattr(geneweaver, package_submodule_name), ERROR_MESSAGE
    assert getattr(geneweaver, package_submodule_name) is not None, ERROR_MESSAGE
