import random
import requests

random_integer = random.randint(6, 10) - 1
url = "https://random-word-api.vercel.app/api?words=1&length=" + str(random_integer)
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

theWord = data[0]
print("_ " * len(theWord))
print("Choose a letter:")
temp = ['_'] * len(theWord)
letters_used = []
gi = 7
for i in range(len(theWord) + gi + 30):
    if (gi == i):
        print("Oops looks like you failed.\nThat's sad. The word was: ")
        print(str(theWord))
        break
    guess = input()
    if not guess.isalpha():
        continue
        gi += 1
    if len(guess) != 1:
        print("That's a word! Taking first letter. Only enter one letter!")
        guess = guess[0]
    if guess in theWord:
        positions = [index for index, char in enumerate(theWord) if char == guess]
        for hm in range(len(positions)):
            temp[positions[hm]] = guess
        for l in range(len(theWord)):
            print(temp[l], end=" ")
        gi += 1
    else:
        for k in range(len(theWord)):
            print(temp[k], end=" ")

    if guess not in letters_used:
        letters_used.append(guess)
    elif guess in letters_used and guess not in theWord:
        print("\nYou already guessed that letter!")
        gi += 1

    if "_" in temp:
        print(letters_used)
        if (gi - i - 1) > 0:
            print(gi - i - 1, end=" ")
            print("guesses left. Choose a letter:", end=" ")

    else:
        print("\nCongratulation on the Win!\nYou managed to win the game with", end=" ")
        print(gi - i - 1, end=" ")
        print("guesses left")
        exit()

    print()
    print("="*20)

print("Too many same guesses! Exiting game")