from wordlist import hanglist
import random
def is_word_length_valid(word):
    return len(word) > 8
def has_only_alpha_characters(word):
    return word.isalpha()
def has_no_uppercase_characters(word):
    return not any(char.isupper() for char in word)
def hangman_game():
    from wordlist import hanglist
    words = hanglist.copy()
    word = random.choice(words)
    if not (is_word_length_valid(word) and has_only_alpha_characters(word) and has_no_uppercase_characters(word)):
     while True:
        word = random.choice(words)
        if is_word_length_valid(word) and has_only_alpha_characters(word) and has_no_uppercase_characters(word):
            break
    print("____________________________________________________________________\n")
    guesses = ''
    guess_turns = 8
    while guess_turns > 0:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end="")
            else:
                print("_ ", end="")
                failed += 1
        if failed == 0:
            print("\nYou win!")
            print("The word is:", word)
            return
        guess = input("\nGuess a character: ")
        guesses += guess
        if guess not in word:
            guess_turns -= 1
            print("Wrong!")
            print("You have", guess_turns, "more guesses")
            if guess_turns == 0:
                print("You lose!")
                print("The word is:", word)
                return
hangman_game()