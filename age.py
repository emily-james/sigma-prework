import datetime

input_date = str(input('Enter date with the format DD-MM-YYYY: '))


def age(date):
    """Calculates age from the inputted date to the current date.
    Input:
        date (str): given date with format DD-MM-YYYY
    Returns:
        (int): age.
        """

    if len(date) != 10:
        raise Exception("The date must have the format DD-MM-YYYY")

    given_day, given_month, given_year = int(
        date[:2]), int(date[3:5]), int(date[6:])

    date_time = str(datetime.datetime.now())

    current_day, current_month, current_year = int(
        date_time[8:10]), int(date_time[5:7]), int(date_time[:4])

    if current_month > given_month:
        return current_year - given_year
    elif current_month < given_month:
        return current_year - given_year - 1
    elif current_month == given_month:
        if current_day < given_day:
            return current_year - given_year - 1
        else:
            return current_year - given_year


print(age(input_date))
