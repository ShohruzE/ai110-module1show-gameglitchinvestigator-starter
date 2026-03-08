# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable.

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: _"How do I keep a variable from resetting in Streamlit when I click a button?"_
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
  - A number-guessing game where the player picks a difficulty, and then guesses the secret number within a range of numbers with a limited number of tries determined by the difficulty.
- [x] Detail which bugs you found.
  - The secret number was being regenerated on each UI interaction because it was created outside of streamlit's session state. The hints displayed during guesses were also flipped.
- [x] Explain what fixes you applied.
  - I moved the core logic into `logic_utils.py`, stored the secret and game data in streamlit's `session_state` so that it persists across streamlit reruns and made the 'New Game' button reset session state values as intended.

## 📸 Demo

- [x]
  ![Winning Screenshot](demo-win.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
