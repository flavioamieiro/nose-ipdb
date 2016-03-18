def test_error():
    raise Exception("Enforcing an error")

def test_failure():
    assert 1 == 2, "This is a failure"

def test_failure_with_print():
    # This test is here to trigger issue #16
    # https://github.com/flavioamieiro/nose-ipdb/issues/16
    print("Test")
    assert 1 == 2, "This failure has a print before it"

def test_failure_with_local_variable():
    local_variable = 'foo'
    assert local_variable == 'bar', "This is a failure with a local variable in scope"

def test_error_with_print_and_exception_that_needs_more_than_one_arg():
    class ExceptionWithManyArgs(Exception):
        def __init__(self, arg1, arg2, *args, **kwargs):
            super(ExceptionWithManyArgs, self).__init__(*args, **kwargs)
    print("Test")
    raise ExceptionWithManyArgs('arg1', 'arg2')
