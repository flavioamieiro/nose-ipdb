def test_error():
    raise Exception("Enforcing an error")

def test_failure():
    assert 1 == 2, "This is a failure"

def test_failure_with_local_variable():
    local_variable = 'foo'
    assert local_variable == 'bar', "This is a failure with a local variable in scope"
