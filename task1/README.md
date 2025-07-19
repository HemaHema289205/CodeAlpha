Hangman game code:

🎮 Hangman Game Summary
🔤 Word Source
- Uses NLTK's words corpus, which provides a large set of English words.
- A random word is selected from this list as the secret word for the game.
🧠 Game Setup
- Initializes:
- guessed_letters as an empty list to track correct guesses.
- wrong_guesses to count incorrect attempts.
- max_wrong_guesses set to 6.
🧩 Display Mechanism
- display_word() function shows the current state of the word:
- Reveals guessed letters.
- Hides remaining letters with underscores _.
🔁 Game Loop
- Keeps running while:
- Wrong guesses are fewer than 6.
- The word is not fully guessed.
- Accepts user input one letter at a time.
- Validates input:
- Must be a single alphabetic character.
- Must not be repeated.
✅ Guess Handling
- If the letter is in the word → responds with "Good guess!"
- If not → increases wrong_guesses and says "Incorrect!"
🏁 Game End
- If all letters are guessed correctly → displays "Congratulations!"
- If the user reaches 6 incorrect guesses → prints "Game Over!" and reveals the word.

