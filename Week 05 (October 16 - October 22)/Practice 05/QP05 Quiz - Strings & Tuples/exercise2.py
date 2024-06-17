import string

def camel_case(phrase):
    result = ""
    capitalize_next = False

    for char in phrase:
        if char.isalpha():
            if result == "":
                result += char.lower()
            elif capitalize_next:
                result += char.upper()
                capitalize_next = False
            else:
                result += char.lower()
        elif char in string.punctuation or char == " ":
            capitalize_next = True

    return result