from typing import Awaitable, Callable, Generator, TypeVar, Union

try:
    # TODO: Consider to delete all unused-ignore's from this file if Python 3.8 is deleted from the CI
    from typing import ParamSpec  # type: ignore[attr-defined, unused-ignore]
except ImportError:  # pragma: no cover
    from typing_extensions import ParamSpec  # type: ignore[assignment, unused-ignore]

import pytest
from transfunctions import transfunction

from transtests.errors import StrangeFunctionTypeError

FunctionParameters = ParamSpec('FunctionParameters')
ReturnValue = TypeVar('ReturnValue')

@pytest.fixture(params=['sync', 'async', 'generator'])
def transformed(request: pytest.FixtureRequest) -> Callable[[Callable[FunctionParameters, ReturnValue]], Callable[FunctionParameters, Union[ReturnValue, Generator[ReturnValue, None, None], Awaitable[ReturnValue]]]]:  # type: ignore[valid-type, unused-ignore]
    """
    Return a decorator that exposes a function in each supported form.

    A test using this fixture runs once with the original synchronous function,
    once with an async function, and once with a generator function.

    Example:

    >>> from asyncio import run
    >>> from inspect import iscoroutinefunction, isgeneratorfunction
    >>>
    >>> def test_something(transformed):
    ...     @transformed
    ...     def some_function(a, b):
    ...         return a + b
    ...
    ...     if iscoroutinefunction(some_function):
    ...         assert run(some_function(1, 2)) == 3
    ...     elif isgeneratorfunction(some_function):
    ...         assert list(some_function(1, 2)) == [3]
    ...     else:
    ...         assert some_function(1, 2) == 3
    """
    def transformator_function(function: Callable[FunctionParameters, ReturnValue]) -> Callable[FunctionParameters, Union[ReturnValue, Generator[ReturnValue, None, None], Awaitable[ReturnValue]]]:  # type: ignore[valid-type, unused-ignore]
        if request.param == 'sync':
            return function
        if request.param == 'async':
            return transfunction(check_decorators=False)(function).get_async_function()
        if request.param == 'generator':
            return transfunction(check_decorators=False)(function).get_generator_function()
        raise StrangeFunctionTypeError("You shouldn't see this error, but if you do, something has probably gone wrong with pytest.")  # pragma: no cover

    return transformator_function
