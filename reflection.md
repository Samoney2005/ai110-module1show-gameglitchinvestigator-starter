# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?
- What did the game look like the first time you ran it?
The game looked like a number game where you had to huess a number. The game would give you hints rather to go high or low. You are also given a choice to start the game over if wanted to. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The hints were inaccurate when you enter your number choice
  2. When the number is guessed the game will not start over
  3. The secret number is not within the range difficuly mode of the game.

---

## 2. How did you use AI as a teammate?
- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I will be using the Claude AI Extension in VSCODE.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).So for the hints error I typed into claude "I noticed this error did you catch this as well". Claude responded saying "Yes, I did catch this error and I believe it can be fixed very easily". Claude guided me to the lines where the error was and I was able to catch the error almost instantly. The print statement was saying "Go Higher" when secret < user_guess and "Go Lower" when secret > user_guess.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).I was having trouble with indentation while trying to fix the error that was causing the game to crash when restarting. Claude kept suggesting to remove the comment block I had added as an outline to fix my code as well as make some edits in the code under it. I accepted the suggestions but once I did claude chnage the code under it that produced a new error. 

After this happened what I did was control Z and started a fresh new chat window because I remebered in class whatcan cause more errors is stringing the AI to fix numberous of tasks in one chat window.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I had to run the program to see if the code was actually fix or not> This is because when I fixed som errors I caused so other errors
either to come back or create new ones. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  One manual test that I ran was seeing if the game saw the change in range. For example, I first changed the in the print statement before the code to see what the game would do. Which I new that it wouldnt make a chnage / difference unless I change the code itself with the error. Eventually after playing around with the code I saw that thier were multiple areas of the code that had to be chnaged not just the print  statement. As well I noticed that when I tried to change it the range would only defalut to 1 to 100. So I had to vreak all the ranges up seperately.

- Did AI help you design or understand any tests? How?
Yes, It mostly helped me to locate the areasin the code where the errors were. This helped alot because with many lines ofcode it is hard to see the errors ir the lines of code that needs to be manipulated or changed.

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
