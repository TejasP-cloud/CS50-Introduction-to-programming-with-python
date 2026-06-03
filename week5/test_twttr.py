from twttr import shorten

def test_lowercase():
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"

def test_mixed():
    assert shorten("Twitter") == "Twttr"

def test_numbers():
    assert shorten("CS50") == "CS50"

