<details>
  <summary>ⓘ</summary>

[![Downloads](https://static.pepy.tech/badge/transtests/month)](https://pepy.tech/project/transtests)
[![Downloads](https://static.pepy.tech/badge/transtests)](https://pepy.tech/project/transtests)
[![Coverage Status](https://coveralls.io/repos/github/mutating/transtests/badge.svg?branch=main)](https://coveralls.io/github/mutating/transtests?branch=main)
[![Lines of code](https://sloc.xyz/github/mutating/transtests/?category=code)](https://github.com/boyter/scc/)
[![Hits-of-Code](https://hitsofcode.com/github/mutating/transtests?branch=main)](https://hitsofcode.com/github/mutating/transtests/view?branch=main)
[![Test-Package](https://github.com/mutating/transtests/actions/workflows/tests_and_coverage.yml/badge.svg)](https://github.com/mutating/transtests/actions/workflows/tests_and_coverage.yml)
[![Python versions](https://img.shields.io/pypi/pyversions/transtests.svg)](https://pypi.python.org/pypi/transtests)
[![PyPI version](https://badge.fury.io/py/transtests.svg)](https://badge.fury.io/py/transtests)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/mutating/transtests)

</details>


![logo](https://raw.githubusercontent.com/mutating/transtests/develop/docs/assets/logo_1.svg)

Sometimes you have code that needs to work the same way with regular, asynchronous, and generator functions. Usually, this means you have to write three sets of nearly identical tests. With this library, you no longer need to do that: a special fixture will generate the necessary tests for you.


## Usage

To use the fixture, you need to add it to your project using the following command:

```bash
pip install transtests
```

The `transformed` fixture is now available for use. It returns a decorator that transforms the original function into one of three variants: the function itself, the same function but as an async, or as a generator function:

```python
from asyncio import run
from inspect import iscoroutinefunction, isgeneratorfunction

def test_something(transformed):
    @transformed
    def some_function(a, b):
        return a + b
    
    if iscoroutinefunction(function):
        assert run(function(1, 2)) == 3

    elif isgeneratorfunction(function):
        assert list(function(1, 2)) == [3]

    else:
        assert function(1, 2) == 3
```

This functionality is based on the [`transfunctions`](https://github.com/mutating/transfunctions) library, so you can use context managers from that library in the original template function.
