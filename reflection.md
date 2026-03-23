# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
- What did the game look like the first time you ran it?
The game looked like a number game where you had to guess a number. The game would give you hints to go high or low. You are also given a choice to start the game over if wanted to. 

List at least two concrete bugs you noticed at the start  
(for example: "the secret number kept changing" or "the hints were backwards").
  1. The hints were inaccurate when you enter your number choice
  2. When the number is guessed the game will not start over
  3. The secret number is not within the range difficulty mode of the game.

---

## 2. How did you use AI as a teammate?
- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used the Claude AI and Copilot Extension in VSCODE.

Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
So for the hints error I typed into claude "I noticed this error did you catch this as well". Claude responded saying "Yes, I did catch this error and I believe it can be fixed very easily". Claude guided me to the lines where the error was and I was able to catch the error almost instantly. The print statement was saying "Go Higher" when secret < user_guess and "Go Lower" when secret > user_guess.

Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
I was having trouble with indentation while trying to fix the error that was causing the game to crash when restarting. Claude kept suggesting to remove the comment block I had added as an outline to fix my code as well as make some edits in the code under it. I accepted the suggestions but once I did claude changed the code under it that produced a new error. 

After this happened what I did was control Z and started a fresh new chat window because I remembered in class what can cause more errors is stringing the AI to fix numerous of tasks in one chat window.

---

## 3. Debugging and testing your fixes

How did you decide whether a bug was really fixed?
I had to run the program to see if the code was actually fixed or not. This is because when I fixed some errors I caused other errors
either to come back or create new ones. 

Describe at least one test you ran (manual or using pytest)  
and what it showed you about your code.
One manual test that I ran was seeing if the game saw the change in range. For example, I first changed the in the print statement before the code to see what the game would do. Which I knew that it wouldn't make a change / difference unless I change the code itself with the error. Eventually after playing around with the code I saw that there were multiple areas of the code that had to be changed not just the print  statement. As well I noticed that when I tried to change it the range would only default to 1 to 100. So I had to break all the ranges up separately.

Did AI help you design or understand any tests? How?
Yes, It mostly helped me to locate the areas in the code where the errors were. This helped a lot because with many lines of code it is hard to see the errors or the lines of code that needs to be manipulated or changed.

---

## 4. What did you learn about Streamlit and state?

In your own words, explain why the secret number kept changing in the original app.
The secret number kept changing because Streamlit reruns the entire script from top to bottom every time the user interacts with the app (like clicking a button or entering text). Without proper state management, `random.randint(low, high)` was being called on every rerun, generating a new random number each time. This meant the secret number never stayed the same long enough for the player to make a real guess.

How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit is like a program that restarts itself every time you click a button or type something. Without special memory, it would forget everything and reset. Session state is like giving Streamlit a notebook to write things down in so it can remember what happened before the restart. When Streamlit reruns, it checks the notebook first to see what was there before, so important values like the secret number stay the same across interactions.

What change did you make that finally gave the game a stable secret number?
I wrapped the secret number creation in an if statement: `if "secret" not in st.session_state:` before calling `random.randint(low, high)`. This ensures the secret number is only generated once when the game first starts, and it stays stored in session state through all the reruns. When the player clicks "New Game," only then does it generate a fresh secret number.

---

## 5. Looking ahead: your developer habits

What is one habit or strategy from this project that you want to reuse in future labs or projects?
I want to reuse the strategy of testing my code manually after each small fix instead of trying to fix multiple bugs at once. When I tested after each change, I could immediately see what broke and fix it right away. This saved me from compounding errors and getting stuck in long debugging sessions.

What is one thing you would do differently next time you work with AI on a coding task?
I would start a fresh chat window or session more frequently rather than asking AI to fix multiple things in one chat. When I kept piling requests into one chat, the AI started making conflicting changes that created new errors. Breaking it into smaller focused conversations would help keep the AI's suggestions clearer and more reliable.

In one or two sentences, describe how this project changed the way you think about AI generated code.
I learned that AI-generated code is a starting point that needs testing and verification, not a finished product. AI can help you find bugs and understand code faster, but the final responsibility for correctness falls on you as the developer.

