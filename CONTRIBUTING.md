# Contributing

This documentation is a work in progress. Please check back often for updates.

The Geneweaver ecosystem is a community-driven project. We welcome contributions from 
all members of the community. 

## Quick Start
You will need:
- Git
- Python 3.9 or higher (see [PyEnv](https://github.com/pyenv/pyenv))
- [Python Poetry](https://python-poetry.org/)

### Installation
To get started, clone the repository and install the dependencies:
```bash
git clone git@github.com:bergsalex/geneweaver-testing.git
cd geneweaver-testing
poetry install
poetry shell
````

### Code Checking
Before submitting a pull request, please run the following commands to check your code:
```bash
ruff check src/geneweaver/testing
isort src/geneweaver/testing
black src/geneweaver/testing
pytest tests
```

## Project Dependencies
### Python Version
All packages in the `geneweaver-*` ecosystem depend on Python version 3.9 or higher.

If you need to manage multiple version of python on your development machine, we 
recommend using [pyenv](https://github.com/pyenv/pyenv) to manage your python versions.

### Poetry
All packages in the `geneweaver-*` ecosystem use [poetry](https://python-poetry.org/)
to manage dependencies and build packages. 

The [Python Poetry Documentation](https://python-poetry.org/docs/#installation)
maintains a list of installation instructions for all major operating systems.

### PyTest
All packages in the `geneweaver-*` ecosystem use 
[PyTest](https://docs.pytest.org/en/7.2.x/) as their test runner.

### Ruff
All code in the `geneweaver-*` ecosystem is linted using 
[ruff](https://github.com/charliermarsh/ruff) and [mypy](https://mypy-lang.org/).

### Black and Isort
All code in the `geneweaver-*` ecosystem is formatted using 
[black](https://github.com/psf/black) and [isort](https://pycqa.github.io/isort/).

## Code Standards

### Organization
This package is intended to be consumed by other packages in the `geneweaver-*` 
ecosystem so that they can run tests and fixtures in a consistent manner. The intended
consumption pattern is to use splat (`*`) imports to import all fixtures and tests and
can be seen in the `tests/conftest.py` and `tests/test_common.py` files.

All code in _this_ package should be categorized as one of two types:

- PyTest Tests: Tests that are run using the `pytest` test runner.
- PyTest Fixtures: Fixtures that are used by PyTest tests.

You can learn more about [PyTest](https://docs.pytest.org/en/7.2.x/) fixtures 
[here](https://docs.pytest.org/en/stable/fixture.html).

#### Pytest Fixtures
All pytest fixtures should be placed in the `src/geneweaver/testing/fixtures` module,
or an organizationally relevant submodule of that module.

##### PyTest Tests
All pytest tests should be placed in the `src/geneweaver/testing` module, or an
organizationally relevant submodule of that module. Tests should be created with the
assumption that packages using this package will make all fixtures available to them.

### Splat Imports
Both PyTest Tests and PyTest Fixtures are intended to be imported by other packages
using splat (`*`) imports. This allows other packages to import all tests and fixtures
in this package with a single import statement.

To manage this, all PyTest Tests and PyTest Fixtures need to be included in the 
`__all__` variable in the namespace (file) they are defined in. When a new file is
created, it must be added to the import chain in each `__init__.py` file in the
package.

All PyTest Tests should be imported in the `src/geneweaver/testing/__init__.py` file.

All PyTest Fixtures should be imported in the 
`src/geneweaver/testing/fixtures/__init__.py` file.

PyTest Fixtures should **not** be imported in the `src/geneweaver/testing/__init__.py` 
file.

All `__init__.py` files should be kept in alphabetical order, and rely on the splat
(`*`) import to import all tests / fixtures from the namespace files in their directory.
Higher level modules should use the splat (`*`) import to import all tests / fixtures
from the lower level modules.

#### Disabling Ruff F403
Ruff will complain about the splat (`*`) imports in the `__init__.py` files. This is
because the splat (`*`) import is not explicitly listing all the names that are
being imported. This is intentional, and the splat (`*`) import is the only way to
import all tests and fixtures in a namespace.

To disable this warning, add the following line to the top of the `__init__.py` file:
```python
# flake8: noqa: F403
```

### Docstrings
All PyTest Tests and PyTest Fixtures should have docstrings. The docstrings should
follow the [Google Style](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings)
for docstrings.

### Type Annotations
All PyTest Tests and PyTest Fixtures should have type annotations. MyPy will be used
to check type annotations.

### Tests
All code contributed to this package should be tested, this includes tests for 
PyTest Fixtures **and** tests for PyTest Tests. This package is a core component of
the Geneweaver ecosystem. Other packages in the ecosystem depend on this package being
well tested.

**For emphasis:** 
- you **must** write tests for tests contributed to this repository, and
- you **must** write tests for fixtures contributed to this repository.

Test code coverage is calculated using the `pytest-cov` module. The minimum code
coverage threshold is 100%. This should be seen as a **minimum**, and not a goal. Code
should be **well tested** through a variety of tests, not just a high code coverage
percentage.


