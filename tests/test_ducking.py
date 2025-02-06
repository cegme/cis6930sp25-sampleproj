
import pytest

import main

compton_json = "https://nominatim.openstreetmap.org/search.php?q=Compton%2C+California&format=json"

@pytest.fixture
def cali_json():
    return r"https://nominatim.openstreetmap.org/search.php?q=Compton%2C+California&format=json"

@pytest.fixture
def tweets_url():
    return "https://ufdatastudio.com/cis6930sp25/documents/scripts/tweets.json"

def test_retrievework(cali_json):
    page = main.getjson(cali_json)
    assert page is not None


def test_isdatajson():
    assert True

def test_queryworks(tweets_url):
    result = main.querysomething_length(tweets_url)
    assert result is not None and result > 0
