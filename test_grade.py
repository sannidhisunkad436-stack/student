
import pytest
from grade import get_student_result

def test_student_grade_A():
    name = "sannidhi"
    dept = "BCA"
    semester = "3"
    m1 = 85
    m2 = 80
    m3 = 90

    expected_output = (
        "Name: Anu, Department: BCA, Semester: 3, "
        "Average: 85.00, Grade: A"
    )

    assert get_student_result(name, dept, semester, m1, m2, m3) == expected_output