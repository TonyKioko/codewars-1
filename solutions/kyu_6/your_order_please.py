# pylint: disable=unnecessary-lambda
"""Your order,  please
https://www.codewars.com/kata/your-order-please

Your task is to sort a given string.
Each word in the String will contain a single number. 
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input String is empty, return an empty String.
The words in the input String will only contain valid consecutive numbers.

For an input: "is2 Thi1s T4est 3a" the function should return "Thi1s is2 3a T4est"
"""


def order(sentence):
    return ' '.join(sorted(sentence.split(), key=lambda word: sorted(word)))
