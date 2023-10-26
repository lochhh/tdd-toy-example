def transform(input=None):
    print(type(input))
    if input is None or not isinstance(input, str):
        raise TypeError("Expected string parameter")
    if input == "":
        return ""
    output = ""
    for letter in input:
        output += transform_letter(letter)
    return output


def transform_letter(letter):
    if is_non_english_letter(letter):
        return letter
    # convert input to lowercase
    input_lower = letter.lower()
    # get unicode code point of first character
    char_code = ord(input_lower)
    if char_code >= ord("n"):
        char_code -= 13
    else:
        char_code += 13
    output = chr(char_code)
    return output.upper() if letter.isupper() else output


def is_non_english_letter(letter):
    return not letter.isascii() or not letter.isalpha()
