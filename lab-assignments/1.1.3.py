
import datetime

def calculate_age(birthdate):
	bdate = datetime.datetime.strptime(birthdate, "%d-%m-%Y")
	today = datetime.datetime.today()
	age = today - bdate
	return age.days // 365


def convert_salary_to_dollars(salary_in_rupees):
    return salary_in_rupees * 0.012
    
birthdate = input()
salary_in_rupees = float(input())
age = calculate_age(birthdate)
salary_in_dollars = convert_salary_to_dollars(salary_in_rupees)
print(f"Age: {age}")
print(f"Salary in dollars: {salary_in_dollars:.2f}")
