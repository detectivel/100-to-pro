def is_leap_year(year):
    """Return True if the specified year is a leap year, False otherwise."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """
    Return the number of days in the specified month and year.

    Parameters:
    - year: int, the year number.
    - month: int, the month number (1-12).

    Returns:
    - int, the number of days in the month.

    Raises:
    - ValueError: If the month is not between 1 and 12.
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if not 1 <= month <= 12:
        raise ValueError(f"Invalid month: {month}. Month must be between 1 and 12.")

    if month == 2 and is_leap_year(year):
        return 29
    else:
        return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
try:
    days = days_in_month(year, month)
    print(days)
except ValueError as e:
    print(e)



