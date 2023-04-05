import re

def phone_is_valid(phone):
    """Validate if phone number is in the format (XX)XXX-XXX-XXX"""
    mold = r'^\(\d{2}\)\d{3}[-]\d{3}[-]\d{3}$'
    is_match = re.findall(mold, phone)
    return is_match
