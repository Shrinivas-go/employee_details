from employee import employee_details

def test_employee_details():
    expected = "Name: Shrinivas\nAge: 20\n"
    assert employee_details("Shrinivas", 20) == expected
