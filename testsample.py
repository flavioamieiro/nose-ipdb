def test_error():
    raise Exception("Enforcing an error")

def test_failure():
    assert 1 == 2, "This is a failure"
