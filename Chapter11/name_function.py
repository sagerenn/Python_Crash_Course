
if __name__ == '__main__':
    print("sdfsdf")

def get_formatted_name(first, last, middle=''):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {middle} {last}".replace("  "," ")
    return full_name.title()