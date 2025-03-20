import logging
import datetime
from decimal import Decimal, InvalidOperation
import calendar
import math

logger = logging.getLogger(__name__)

def get_number(input_str:str):
    """
    convert input string to float

    Args:
        input_str (str): input string

    Returns:
        _type_: _description_
    """
    try:            
        return float(input_str)
    except ValueError:
        print("Please enter a number.")
            

def is_two_decimal_places(input_str):
    """
    Check if input is up to 2 decimal places

    Args:
        input_str (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        number = Decimal(input_str)
        #print(number.as_tuple())
        # Check if the number of decimal places is up to 2
        return number.as_tuple().exponent >= -2 #
    except InvalidOperation:
        return False
    
def get_date(input_str):
    """
    Convert input string to date

    Args:
        input_str (_type_): _description_

    Returns:
        _type_: _description_
    """
    try:
        return datetime.datetime.strptime(input_str, "%Y%m%d").date()
    except ValueError:
        return None
    
def math_round(num):
    frac = num - math.floor(num)
    if frac < 0.5:
        return math.floor(num)

    return math.ceil(num)