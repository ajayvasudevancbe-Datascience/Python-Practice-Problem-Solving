""" Question 5: Hangman """
"""
Input: string
Output: interactive hangman game
"""
def play_hangman(word):
    actual_word = word.lower()
    current_word = "-" * len(actual_word)
    guessed_letters = []
    parts_left = 6

    while parts_left != 0 and "-" in current_word:
        print("Current Word:", current_word)
        print("Parts Left:", parts_left)
        print("Guessed:", guessed_letters)

        letter = get_guess_letter(guessed_letters)
        guessed_letters.append(letter)

        if letter in actual_word:
            print("Good Guess!")
            current_word = update_current_word(letter, actual_word, current_word)
        else:
            print("Wrong Guess!")
            parts_left -= 1

        print("-" * 20)

    print("Final word:", actual_word)

    if "-" not in current_word:
        print("You Won!")
    else:
        print("You Lost!")


def update_current_word(letter, actual_word, current_word):
    result = ""

    for i in range(len(actual_word)):
        if actual_word[i] == letter:
            result += letter
        else:
            result += current_word[i]   # keep previous progress

    return result


def get_guess_letter(guessed_letters):
    while True:
        letter = input("Enter a letter: ").lower()

        if len(letter) != 1:
            print("Enter only one letter!")
        elif letter in guessed_letters:
            print("Already guessed!")
        else:
            return letter


if __name__ == '__main__':
    play_hangman("programming")




""" Sample Hangman game in Python terminal:

Current word: _ _ _ _ _ _ _ _ _ _ _ 
Incorrect guesses left: 6
Letters guessed: 
Which letter do you want to guess: e
Not quite...
-----
Current word: _ _ _ _ _ _ _ _ _ _ _ 
Incorrect guesses left: 5
Letters guessed: e
Which letter do you want to guess: o
Good guess!
-----
Current word: _ _ o _ _ _ _ _ _ _ _ 
Incorrect guesses left: 5
Letters guessed: e, o
Which letter do you want to guess: i
Good guess!
-----
Current word: _ _ o _ _ _ _ _ i _ _ 
Incorrect guesses left: 5
Letters guessed: e, o, i
Which letter do you want to guess: n
Good guess!
-----
Current word: _ _ o _ _ _ _ _ i n _ 
Incorrect guesses left: 5
Letters guessed: e, o, i, n
Which letter do you want to guess: g
Good guess!
-----
Current word: _ _ o g _ _ _ _ i n g 
Incorrect guesses left: 5
Letters guessed: e, o, i, n, g
Which letter do you want to guess: y
Not quite...
-----
Current word: _ _ o g _ _ _ _ i n g 
Incorrect guesses left: 4
Letters guessed: e, o, i, n, g, y
Which letter do you want to guess: as
Please enter only one letter.
Which letter do you want to guess: a
Good guess!
-----
Current word: _ _ o g _ a _ _ i n g 
Incorrect guesses left: 4
Letters guessed: e, o, i, n, g, y, a
Which letter do you want to guess: m
Good guess!
-----
Current word: _ _ o g _ a m m i n g 
Incorrect guesses left: 4
Letters guessed: e, o, i, n, g, y, a, m
Which letter do you want to guess: i
You already guessed that letter! Pick a different letter.
Which letter do you want to guess: t
Not quite...
-----
Current word: _ _ o g _ a m m i n g 
Incorrect guesses left: 3
Letters guessed: e, o, i, n, g, y, a, m, t
Which letter do you want to guess: r
Good guess!
-----
Current word: _ r o g r a m m i n g 
Incorrect guesses left: 3
Letters guessed: e, o, i, n, g, y, a, m, t, r
Which letter do you want to guess: p
Good guess!
-----
Final word: p r o g r a m m i n g 
You won in 11 turns.
"""

if __name__ == '__main__':
    play_hangman("programming")




