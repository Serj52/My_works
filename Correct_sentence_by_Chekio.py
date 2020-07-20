# For the input of your function, you will be given one sentence.
# You have to return a corrected version, that starts with a capital letter and ends with a period (dot).
# Pay attention to the fact that not all of the fixes are necessary.
# If a sentence already ends with a period (dot), then adding another one will be a mistake.
#
# Input: A string.
#
# Output: A string.
#
# Precondition: No leading and trailing spaces, text contains only spaces, a-z A-Z , and .

def correct_sentence(text):

    if text[0].istitle() is False and text[len(text)-1] != '.':
        return text[0].title() + text[1:] + '.'
    elif text[0].istitle() and text[len(text) - 1] != '.':
        return text + '.'
    elif text[0].istitle() is False and text[len(text) - 1] is '.':
        return  text[0].title() + text[1:]
    else:
        return text


if __name__ == '__main__':
    print("Example:")
    print(correct_sentence("greetings, friends"))

    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")