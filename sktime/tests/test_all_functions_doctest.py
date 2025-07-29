from sktime.utils._testing.doctest import run_doctest


def test_all_functions_doctest(func):
    """Run doctest for all functions in sktime."""
    run_doctest(func, name=f"function {func.__name__}")