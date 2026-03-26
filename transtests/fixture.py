from collections.abc import Awaitable, Callable, Generator
from typing import TypeVar, Union

import pytest
from transfunctions import transfunction
from typing_extensions import ParamSpec


FunctionParameters = ParamSpec('FunctionParameters')
ReturnValue = TypeVar('ReturnValue')

@pytest.fixture
def transformed() -> Callable[[Callable[FunctionParameters, ReturnValue]], Generator[Callable[FunctionParameters, Union[ReturnValue, Generator[ReturnValue, None, None], Awaitable[ReturnValue]]], None, None]]:
    def transformator_function(function: Callable[FunctionParameters, ReturnValue]) -> Generator[Callable[FunctionParameters, Union[ReturnValue, Generator[ReturnValue, None, None], Awaitable[ReturnValue]]], None, None]:
        transformations = [
            lambda x: x,
            lambda x: transfunction(check_decorators=False)(x).get_async_function(),
            lambda x: transfunction(check_decorators=False)(x).get_generator_function(),
        ]

        for transformation in transformations:
            yield transformation(function)  # type: ignore[no-untyped-call]

    return transformator_function
