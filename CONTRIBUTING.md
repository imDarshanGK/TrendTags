# Contributing to TrendTags

Thank you for your interest in contributing to TrendTags! Here's how you can help improve this YouTube tag generator.

## Getting Started

### Prerequisites

- Python >=3.12
- Git
- Basic understanding of Flask (for backend contributions)

## How to Contribute

### Reporting Issues

- Search existing issues before creating new ones
- Include:
  - Clear description of the problem
  - Steps to reproduce
  - Expected vs actual behavior
  - Screenshots (if applicable)

### Making Changes

1. Fork the repository
1. Clone your fork with `git clone https://github.com/yourusername/TrendTags.git`
1. Navigate to your directory with `cd TrendTags`
1. Create a virtual environment with `python -m venv .venv`
1. Activate you virtual environment
    - Windows: `source .venv/Scripts/activate`
    - Unix: `source .venv/bin/activate`
1. Install dependencies with `pip install -r requirements.txt`
1. Create a branch: `git switch -c {type}/branch-name`
1. Make your changes prefixing commits with `{type}: changed xyz`
    - When possible, squash/rebase smaller related commits before pushing
1. Validate your changes by running `pytest -v [specificTestDirectory or Test]`
1. Test app functionally locally by running `python app.py`
1. When your changes are ready, push to your fork: `git push origin {type}/branch-name`
1. Open a [Pull Request](https://github.com/imDarshanGK/TrendTags/pulls)

#### Branch & Commit Types

Use these prefixes for your `{type}` when creating branches and making commits:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code formatting changes
- `refactor`: Code changes that neither fix bugs nor add features
- `test`: Test related changes

### Testing with PyTest

This project uses `pytest` for all testing. Tests are located in the following locations:

```bash
TrendTags/
├── tests/
│   ├── integration/    # Integration Tests
│   ├── unit/           # Unit tests
```

To run all tests:

```bash
pytest -v tests/
```

To run just unit or integration tests:

```bash
pytest -v tests/unit
pytest -v tests/integration
```

To run all tests and check coverage:

```bash
pytest -v --cov-report term-missing --cov=. tests/
```

This will provide you with both a verbose test result for all tests (or your specific tests if specified) as well as a coverage report indicating what lines of code are not currently covered by tests. For additional testing and coverage features, please see the documentation for [Pytest](https://docs.pytest.org/en/stable/) and [Pytest-Cov](https://pytest-cov.readthedocs.io/en/latest/readme.html)

```bash
========================================================================================================================================================= test session starts =========================================================================================================================================================
platform darwin -- Python 3.13.2, pytest-8.3.5, pluggy-1.6.0 -- /Users/username/Developer/TrendTags/.venv/bin/python3.13
cachedir: .pytest_cache
rootdir: /Users/user/Developer/TrendTags
plugins: cov-6.1.1
collected 2 items                                                                                                                                                                                                                                                                                                                     

tests/unit/test_classes.py::TestRemoveDuplicateTags::test_remove_duplicate_items PASSED                                                                                                                                                                                                                                         [ 50%]
tests/unit/test_classes.py::TestRemoveDuplicateTags::test_remove_duplicate_items_unique PASSED                                                                                                                                                                                                                                  [100%]

=========================================================================================================================================================== tests coverage ============================================================================================================================================================
__________________________________________________________________________________________________________________________________________ coverage: platform darwin, python 3.13.2-final-0 ___________________________________________________________________________________________________________________________________________

Name                         Stmts   Miss  Cover   Missing
----------------------------------------------------------
app.py                          94     94     0%   1-167
config.py                        7      7     0%   1-14
src/__init__.py                  1      0   100%
src/utilities.py                 3      0   100%
tests/__init__.py                0      0   100%
tests/unit/__init__.py           0      0   100%
tests/unit/test_classes.py      10      0   100%
----------------------------------------------------------
TOTAL                          115    101    12%
========================================================================================================================================================== 2 passed in 0.02s ==========================================================================================================================================================
```

Make sure all tests pass before opening a pull request. If you add new functionality or modify existing behavior please include appropriate tests. Failing tests may prevent pull requests from being merged.

### Pull Request Process

- Ensure your branch is up-to-date with `main` (rebase if necessary)
- All tests must pass before submitting
- Include in your PR:
  - Description of changes
  - Screenshots (for UI changes)
  - Related issue numbers (e.g., "Fixes #123") - [Linking a pull request to an issue
](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/linking-a-pull-request-to-an-issue)
- Request review from maintainers

## Code Standards

### Python

- Follow the [PEP 8 Style Guide](https://peps.python.org/pep-0008/)
- Use type hints for new functions
- Include docstrings for public methods
- Keep lines under 88 characters

### JavaScript

- Use ES6+ syntax
- Prefer `const` over `let`
- Use meaningful variable names

### HTML/CSS

- Semantic HTML5
- Responsive design principles
- BEM naming convention for CSS classes
