from bank import value

def test_hello():
    assert value("Hello") == 0

def test_starwithh():
    assert value("Hey") == 20

def test_differentword():
    assert value("what's up") == 100

