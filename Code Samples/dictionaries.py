# illustration of how dictionaries work

employee_record = {
    "last_name":"Arsenault",
    "first_name":"Alfred",
    "emp_id": "ABC123",
    "dept":"EECS",
    "college":"COEIT",
    "rank":"Adjunct",
    "hourly_pay":1
}

#l = ["Arsenault, Alfred","ABC123", 89,54,33,16,22]
print(employee_record)
print(employee_record["first_name"])

employee_record["years_teaching"] = 22
print(employee_record)

employee_record["first_name"] = "John"
print(employee_record)