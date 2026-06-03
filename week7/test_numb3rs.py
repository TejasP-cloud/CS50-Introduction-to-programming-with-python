from numb3rs import validate

def test_valid():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("192.168.1.1") == True

def test_invalid_range():
    assert validate("256.0.0.0") == False
    assert validate("999.999.999.999") == False
    assert validate("1000.1.2.3") == False

def test_invalid_format():
    assert validate("cat") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("") == False