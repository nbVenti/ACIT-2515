from demo import Person
from demo import create_person 
from demo import create_from_file
import pytest

from unittest.mock import patch
from unittest.mock import mock_open


@pytest.fixture
def person():
    return Person("John")

def test_constructor(person):
    
    assert person.name == "John"
    assert person.age == 0
    

def test_greet(person):
    
    assert person.greet() == "Hello, my name is John and I am 0 years old."
    
def test_age(person):
    
    person.birthday()
    assert person.age == 1
    
    
@patch("builtins.input", side_effect=["John","100"])
def test_create(mock_input):
    person = create_person()
    assert mock_input.call_count == 2      
    assert person.name == "John"
    assert person.age == 100

@patch("builtins.open", new_callable=mock_open, read_data="Sam\nTim\n")
def test_create_file(mock_file):
        person = create_from_file()
        assert len(person) == 2
    