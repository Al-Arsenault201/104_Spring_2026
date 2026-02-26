# in class coding from Wednesday, February 25

#add a new function that figures out how many leap days to add

def leap_days(year):
	leaps = (2026 - year)%4
	return leaps

def calculate_days (years, months, days):

    def get_year():
        return int(input("Enter the current year: "))


    num_days = 365 * (get_year() - years) + 30 * (14 - months)%12 + (25 - days)
    num_days += leap_days(years)

    """
	if years > 4:
		num_days += 1
	"""
    return num_days

if __name__ == '__main__':
    """
	birth_year = int(input("Enter birth year: "))
	birth_month = int(input("Enter birth month: "))
	birth_day = int(input("Enter birth day: "))
	num_days = calculate_days(birth_year, birth_month, birth_day)
	print(" you are: ",num_days, "days old")
    """
    start_year = int(input("Enter the year you started college: "))
    start_month = int(input("Enter the month you started college: "))
    start_day = int(input("Enter the day you started college: "))
    days_in_college = calculate_days(start_year, start_month, start_day)
    print("you have been in college: ", days_in_college, " days")

