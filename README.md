# Geneweaver Testing
This package is used to test the Geneweaver project. It contains tools for running tests against Geneweaver project
packages and components to aid in the development of Geneweaver. 

## Quick Start
1. Install the package
    ```bash
    poetry install -G dev geneweaver-testing
    ```
2. Make a "common" test file
    ```
    touch tests/common.py
    ```
3. Add the following to the "common" test file
    ```
    # Inside tests/common.py
    from geneweaver.testing import *
    ```
4. Add a fixture file at test root (if you don't have one already)
    ```
    touch tests/conftest.py
    ```
5. Add the following to the fixture file
    ```
    # Inside tests/conftest.py
    from geneweaver.testing.fixtures import *
    ```
6. Run Tests!
    ```bash
    pytest tests
    ```

## Package Modules
Like all Geneweaver packages, this package is namespaced under the `geneweaver` package. The root of this package is
`geneweaver.testing`. The package is structured for usage in pytest tests, with pre-defined tests available through
splat (`*`) imports as shown in the Quick Start. Other package functionality is available by specifically importing
modules.

The following modules are available in this package:

### `geneweaver.testing.fixtures`
This module contains pytest fixtures that are used to test Geneweaver packages. These fixtures can be used to set up
test contexts for Geneweaver packages. This module does not contain any tests.

### `geneweaver.testing.package`
This module contains tools for testing and validating Geneweaver packages. 


## Contributing
Contributions to this package are welcome. Please see the [Contributing](CONTRIBUTING.md) document for more information.

