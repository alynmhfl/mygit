import string

def leter_count(a_str):
    """Return the count of letters in a str."""
    count = 0
    for char in a_str:
        if char.lower() in string.ascii_lowercase:
            count += 1
            return count
