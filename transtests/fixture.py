from typing import Awaitable, Callable, Generator, TypeVar, Union

try:
    from typing import ParamSpec  # type: ignore[attr-defined]
except ImportError:  # pragma: no cover
    from typing_extensions import ParamSpec

import pytest
from transfunctions import transfunction

from transtests.errors import StrangeFunctionTypeError

FunctionParameters = ParamSpec('FunctionParameters')
ReturnValue = TypeVar('ReturnValue')

@pytest.fixture(params=['sync', 'async', 'generator'])
def transformed(request: pytest.FixtureRequest) -> Callable[[Callable[FunctionParameters, ReturnValue]], Callable[FunctionParameters, Union[ReturnValue, Generator[ReturnValue, None, None], Awaitable[ReturnValue]]]]:  # type: ignore[valid-type]
    def transformator_function(function: Callable[FunctionParameters, ReturnValue]) -> Callable[FunctionParameters, Union[ReturnValue, Generator[ReturnValue, None, None], Awaitable[ReturnValue]]]:  # type: ignore[valid-type]
        if request.param == 'sync':
            return function
        if request.param == 'async':
            return transfunction(check_decorators=False)(function).get_async_function()
        if request.param == 'generator':
            return transfunction(check_decorators=False)(function).get_generator_function()
        raise StrangeFunctionTypeError("You shouldn't see this error, but if you do, something has probably gone wrong with pytest.")  # pragma: no cover

    return transformator_function
