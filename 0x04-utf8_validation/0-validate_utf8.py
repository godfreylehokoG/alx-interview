#!/usr/bin/python3
"""
Define validUTF8(data) function that validates whether a
string of ints represents a valid UTF-8 encoding.
"""

def validUTF8(data):
        """ doc """
        try:
            maskeddata = [n & 255 for n in data]
            bytes(maskeddata).decode("UTF-8")
            return True
        except Exception:
            return False
