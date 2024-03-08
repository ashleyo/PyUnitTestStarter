test_data = [
        # Abnormal cases
        ("a", False),
        ("a"*16, False),
        ("", False),
        ("A", False),
        ("1", False),
        ("-", False),
        # Extreme cases
        ("a"*3, True),
        ("a"*15, True),
        # Normal cases
        ("a"*4, True),
        ("a"*14, True),
        ("abcdefghijklm", True),
        ("nopqrstuvwxyz", True),

]


def get_name()->str:
    import re

    messages = [
        "Must be more than  two characters.",
        "Must be fewer than  sixteen characters.",
        "Must only contain a-z.",
        "Please try again",
    ]

    while True:
        try:
            name = input("Name? :")
            if re.match(r'^[a-zA-Z]{3,15}$', name) is None:
                raise ValueError
                
        except ValueError:
            print(f"{messages[0]} {messages[1]} {messages[2]}") 
        else:
            break
        print(f"{messages[3]}")

    return name

if __name__ == "__main__":
    print(get_name())
