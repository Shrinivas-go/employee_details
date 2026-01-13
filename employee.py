def employee_details(name, age):
    result = (
        f"Name: {name}\n"
        f"Age: {age}\n" 
    )
    return result
if __name__ == "__main__":
  name = "Shrinivas"
  age = 20
  print(employee_details(name, age))