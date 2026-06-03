from plates import is_valid_plate


def test_length():
    assert is_valid_plate("CS50") == True
    assert is_valid_plate("A") == False
    assert is_valid_plate("ABCDEFG") == False


def test_start():
    assert is_valid_plate("AA123") == True
    assert is_valid_plate("11ABC") == False
    assert is_valid_plate("A1BCD") == False


def test_numbers():
    assert is_valid_plate("CS50") == True
    assert is_valid_plate("CS05") == False
    assert is_valid_plate("AAA222") == True


def test_symbols():
    assert is_valid_plate("PI3.14") == False
    assert is_valid_plate("HELLO!") == False
    assert is_valid_plate("CS 50") == False