# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
  - The game showed an input box prompting me to guess a number. A banner was displayed telling me to guess a number and that I have 7 attempts. There is a sidebar where I can select the difficulty as well as the selected range and number of attempts left which I assume it would change based on the selected difficulty.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  - I tried to start a new game after completing one, and it did not start a new game. Entering guesses did not do anything and text was displayed telling me to start a new game even though I already have.
  - Pressing show hint doesn't seem to do anything. It doesn't change anything in the developer debug info dropdown and nothing changes anywhere else on the app.
  - The range and number of attempts does not accuractely reflect the difficulties.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  - I used GitHub Copilot with the GPT-5 mini and 5.3 Codex models.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  - The AI suggested to move the functions in app.py to logic_utils.py without me specifying it.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  - One thing that was incorrect was the range of the different difficulties. It stuck with keeping normal mode at 100 instead of 50 and vice versa for the hard mode which doesn't make sense. Verified the changes by reviewing the UI output.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  - I decided if a bug was really fixed by own judgement and verifying if functionality made sense through interacting with the streamlit app.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  - One test I ran was checking if entering guesses correctly matched the expected helper text.
- Did AI help you design or understand any tests? How?
  - Yes, AI wrote the tests for all of the helper functions of the app.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
