import employee_details from employee
def test_employee_details():
  expected = (
    "Name: Shrinivas\n"
    "Age: 20\n"
  )
  assert employee_details("Shrinivas" , 20) == expected