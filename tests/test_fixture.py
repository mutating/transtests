from asyncio import run
from inspect import iscoroutinefunction, isgeneratorfunction


def test_all_kind_of_functions(transformed):
    @transformed
    def function():
        return 123

    if iscoroutinefunction(function):
        assert run(function()) == 123

    elif isgeneratorfunction(function):
        assert list(function()) == [123]

    else:
        assert function() == 123
