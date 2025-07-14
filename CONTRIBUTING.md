# Contributing to MkDocs Uptime Badge Plugin

Thank you for considering contributing to the MkDocs Uptime Badge Plugin! This document provides guidelines and instructions for contributing to this project.

## Development Environment Setup

1. Install Poetry (if not already installed):
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mkdocs-uptime-badge.git
   cd mkdocs-uptime-badge
   ```

3. Install the package and all dependencies (including development dependencies):
   ```bash
   poetry install
   ```

4. Activate the Poetry virtual environment:
   ```bash
   poetry shell
   ```

## Coding Standards

- Python 3.13 or higher is required.
- All public functions should be type-annotated.
- Follow PEP 8 style guidelines.
- Use ruff for linting:
  ```bash
  poetry run ruff --select E,F,I .
  ```
- Keep the plugin code concise (≤ 120 lines of code, excluding tests and setup).
- No external runtime dependencies beyond MkDocs itself.

## Testing

- Write tests for all new features or bug fixes.
- Maintain 100% test coverage for the plugin.py file.
- Run tests using pytest:
  ```bash
  poetry run pytest
  ```

## Pull Request Process

1. Fork the repository and create a new branch for your feature or bug fix.
2. Implement your changes, following the coding standards above.
3. Add or update tests to cover your changes.
4. Update documentation as needed.
5. Run the tests to ensure they pass.
6. Submit a pull request with a clear description of the changes and any relevant issue numbers.

## Demo Project

The repository includes a demo project that can be used to test the plugin:

1. Navigate to the demo directory:
   ```bash
   cd demo
   ```

2. Run MkDocs:
   ```bash
   poetry run mkdocs serve
   ```

3. Open your browser to http://127.0.0.1:8000/ to see the plugin in action.

## Building and Installing

To build the package:

```bash
poetry build
```

This will create distribution packages in the `dist/` directory.

To install the package:

```bash
poetry install
```

Or to install from the built package:

```bash
pip install dist/*.whl
```

## License

By contributing to this project, you agree that your contributions will be licensed under the project's MIT license.
