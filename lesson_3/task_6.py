#!/usr/bin/env python3
""">>>\nThis module converts all Latin words in input text
to uppercase first letter.
\nThe User needs to enter text in line.

Functions:

    main() -> None

    get_input_text() -> str

    int_func(input_text: str) -> str

    is_valid(word: str) -> bool

*author: Nemykin Eugene (Student GeekBrains)\n<<<
"""
def get_input_text() -> str:
    """Requests User input and returns a string.

    Returns:
        text: str -- user's input string
    """
    print('Enter one or several words separated by space:')
    text: str = input()
    return text


def int_func(input_text: str) -> str:
    """Returns all Latin words in input argument with uppercase first letter.

    Internal Functions:
        is_valid -- Validates the input word belongs to Latin
                    by its ASCII character codes
    
    Arguments:
        input_text -- any string of words

    Returns:
        output_text -- same string with uppercase first letter in Latin words
    """
    def is_valid(word: str) -> bool:
        """Validates the input word belongs to Latin
        by its ASCII character codes.

        Arguments:
            word -- input word

        Returns:
            True if input word is Latin and False if not
        """
        ord_list: list[int] = list(map(ord, [symb for symb in word]))
        for ord_symb in ord_list:
            if ord_symb not in range(97, 122 + 1):
                return False
        return True

    output_text: str = ''
    for word in input_text.split():
        if is_valid(word):
            word = word.title()
        output_text += f'{word} '
    return output_text


if __name__ == '__main__':
    print(__doc__)
    input_text: str = get_input_text()
    print(int_func(input_text))
