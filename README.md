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

If your code needs to work the same way with regular, asynchronous, and generator functions, you normally have to write three sets of nearly identical tests. With this library, you no longer need to do that — just use the special fixture, which generates the necessary variants automatically.


## Usage

To use the fixture, install it via:

```bash
pip install transtests
```

The `transformed` fixture is now available. It returns a decorator that transforms the original function into one of three variants: the original synchronous function, the same function but as an async one, or as a generator function:

```python
from asyncio import run
from inspect import iscoroutinefunction, isgeneratorfunction

def test_something(transformed):
    @transformed
    def some_function(a, b):
        return a + b
    
    if iscoroutinefunction(some_function):
        assert run(some_function(1, 2)) == 3

    elif isgeneratorfunction(some_function):
        assert list(some_function(1, 2)) == [3]

    else:
        assert some_function(1, 2) == 3
```

This functionality is based on the [`transfunctions`](https://github.com/mutating/transfunctions) library, so you can use context managers from that library in the source function.
