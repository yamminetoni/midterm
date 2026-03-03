def days_since_birthday(birthday):
    # birthday format: "DD-MM-YYYY"

    # split the string
    parts = birthday.split("-")

    birth_year = int(parts[2])

    current_year = 2026  # current year

    # calculate full years passed (excluding birth year and current year)
    full_years = current_year - birth_year - 1

    if full_years < 0:
        return 0

    # calculate days (ignoring leap years)
    days = full_years * 365

    return days