"""
Kata: IP Validation (4 kyu)

Description:

Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. Input to the function is guaranteed to be a single string.

Examples of valid inputs: 1.2.3.4 123.45.67.89

Examples of invalid inputs: 1.2.3 1.2.3.4.5 123.456.78.90 123.045.067.089

URL: https://www.codewars.com/kata/ip-validation
"""

def is_valid_IP(ip):
    octets = ip.split('.')
    if len(octets) != 4: return False
    for octet in octets:
        if not is_valid_octet(octet):
            return False
    return True

def is_valid_octet(octet):
    if not octet.isdigit():
        return False
    if len(octet) > 1 and octet[0] == '0':
        return False
    octet = int(octet)
    if octet >= 0 and octet <= 255:
        return True
    else:
        return False