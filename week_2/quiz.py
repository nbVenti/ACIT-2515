import pytest

class typeError(Exception):
    pass

def average(my_list):
    if not len(my_list):
        return 0 
    
    try:
        result = sum(my_list)/len(my_list)
    except TypeError:
        raise typeError("The list must contain numbers")
    
    return result


def test_ave():
    result = average([0,5,10])
    assert result == 5
    
def test_ave2():
    with pytest.raises(typeError):
        average(['a','b','c'])
        
def test_ave3():
    result = average([])
    assert result == 0


list = [1, 2, 3 ,4]

for myVar in range(len(list)):
    print(list[myVar])

if __name__ == "__main__":
    test_ave()
    test_ave2()
    test_ave3()
    