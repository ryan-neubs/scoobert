#datevalidator.py

def isleapyear(year):
    if year % 100 == 0:
        return (year % 4 == 0 and year % 400 == 0)
    elif year % 4 == 0:
        return True
    return False

def month_lengths(year):
    """ construct a list of month lengths
    pre: year is an int
    post: returns a list, lengths, where lengths[month] is the number of
    days in that month of year
    """
    if isleapyear(year):
        return [31, 29, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]
    
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def days_in_month(month, year):
    """return number of days in a given month of a year
    
    pre: month is an int representing a valid month number
         and year is an int representing the year (e.g. 2021).
    post: returns an int of the number of days in the month
    """
    assert month in range(1,13)
    return month_lengths(year)[month - 1]


def is_valid_date(day, month, year):
    """determine whether date is valid

    pre: day, month, and year are ints
    post: returns True if values indicate a legal date, 
          False otherwise.
    """

    return ( 1 <= month <= 12
            and 1 <= day <= days_in_month(month, year)
            and year > 1582)
