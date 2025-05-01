import datetime

# We count the Sundays that fall on the first of the month between 1901 and 2000
def compute():
    sunday_count = 0

    # Loop through each year from 1901 to 2000
    for year in range(1901, 2001):
        # Loop through each month from January to December
        for month in range(1, 13):
            # Create a date object for the first day of each month
            first_day = datetime.date(year, month, 1)
            # Check if the first day of the month is a Sunday (weekday() returns 6 for Sunday)
            if first_day.weekday() == 6:
                sunday_count += 1

    return str(sunday_count)


if __name__ == "__main__":
    print(compute())
