COURSES = ["ACIT2515", "ACIT1620", "ACIT0220", "ACIT0320","ACIT1420", "ACIT1951", "COMM0330", "COMM0350", "COMM1650","ENGL0220", "ENGL0510", "MATH0150", "ENGL0450", "PROJ0900","PROJ1360"]
import pytest 

class AttributeError(Exception):
    pass

def department_courses(course_list, department):    
    if type(course_list) != list and type(course_list) != tuple:
        return []
    if type(course_list) != (list or tuple):
        return []
    if len(department) <= 3 or len(department)>= 5:
        raise AttributeError("Department must be 4 characters long")
        
    return [x for x in course_list if x[0:4] == department]
    

def text(str) -> str:
    return (str.replace("o" or "O" ,"0").replace("e" or "E", "3").replace("l", "1").replace("I", "|").replace("a","@"))

def test_text():
    assert text("") == ""
    assert text("Hello") == "H3110"
    assert text("Goodbere") == "G00db3r3"
    
def test_department_courses():
    # assert department_courses([], "") == []
    
    # assert department_courses(["ACIT1234"], "") == []
    
    assert department_courses({"ACIT1234"}, "ACIT") == []
    
    assert department_courses(("ACIT1234"), "ACIT") == []
    
    assert department_courses({"ACIT1234"}, "ACIT") == []
    
    assert department_courses({"ACIT1234"}, "ACIT") == []
    
    with pytest.raises(AttributeError):
        department_courses(["ACIT1234"], "ACI")
    
    assert department_courses(["ACIT1234"], "ENGL") == []
    
    assert department_courses(["ACIT1234"], "ACIT") == ["ACIT1234"]
    
    assert department_courses(["ACIT1234", "ACIT5678"], "ACIT") == ["ACIT1234","ACIT5678"]
    
    assert department_courses(["ACIT1234", "ACIT5678", "ENGL1234"], "ACIT") == ["ACIT1234", "ACIT5678"]
    
    assert department_courses(["ACIT1234", "ACIT5678", "ENGL1234"], "ENGL") == ["ENGL1234"]
    
    with pytest.raises(AttributeError):
        department_courses(["ACIT1234", "ACIT5678", "ENGL1234"], "ENG")

if __name__ == "__main__":
    test_text()
    test_department_courses()
    print("All tests passed!")