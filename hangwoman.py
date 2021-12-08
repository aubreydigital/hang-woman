import random
import words
import hang

lives = 7

# hang_word = words[random.randint(0, len(words) - 1)]
hang_word = random.choice(words.words)
print()
print('h a n g w o m a n')
print()
status = list('_' * len(hang_word))


while lives > 0 and status != hang_word:
    print()
    print(''.join(status))
    print()
    choice = input('Pick a letter: \n').lower()
    hang_word = list(hang_word)
    i = 0
    wrong_i = 0

    for letter in hang_word:
        if choice == letter:
            status[i] = choice
        else:
            wrong_i += 1
        i += 1
    if wrong_i == len(hang_word):
        print(hang.stages[lives -1])
        print('Incorrect guess!')
        lives -= 1
        print()
        print(lives, 'lives left')
        print()
    if hang_word == status:
        print('You win!')
        print()
    elif lives == 0:
        print('You are dead!')
        print()