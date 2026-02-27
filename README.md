[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/LkIvP-P-)
# Lab 4: Conversational Tutor with LiteLLM and Ollama

## Overview

In this lab you'll build a web-based chat interface where a student converses with an AI tutor. The tutor is grounded in **hardcoded educational questions** that you embed in the system prompt.

## Setup

### 1. Install Ollama

```bash
# macOS / Linux
curl -fsSL https://ollama.com/install.sh | sh

# Or download from https://ollama.com/download
```

### 2. Pull a model

```bash
ollama pull llama3.2
```

### 3. Set up your Python environment

```bash
conda activate flask-env
pip install -r requirements.txt
```

### 4. Test from the command line first

```bash
python chat_cli.py
```

### 5. Run the web app

```bash
python app.py
```

Then open http://127.0.0.1:5000/ in your browser.

## Your Tasks

1. **Replace the example questions** in `questions.py` with at least 5 questions on a topic you know well. Include correct answers and common misconceptions.
2. **Design a system prompt** that tells the LLM how to tutor. This is the creative heart of the lab — what kind of tutor do you want to build?
3. **Build out the chat interface** — the starter gives you a bare minimum. Make it your own.
4. **Test and iterate** on your system prompt. Try correct answers, wrong answers, "I don't know," and off-topic messages.

## Project Structure

```
lab4-starter/
    app.py              # Flask app with / and /chat routes
    questions.py        # Your educational questions (replace the examples!)
    chat_cli.py         # Command-line LLM chat (for testing)
    templates/
        chat.html       # Chat web interface
    requirements.txt
```

## Reflection Questions

Answer each question below by writing in the space provided. This is a markdown file — you can edit it directly in your code editor or on GitHub.

### 1. How did designing a *system prompt* compare to designing *frames* in Lab 3? Which gives you more control over the learning experience? Which is more work?

```
When designing the frames in Lab 3, you are essentially providing the program with word-for-word what to “say” or display for each question. The system prompt, on the other hand, is more of a general set of guidelines for the LLM tutor to follow. It will not display any of the text in the system prompt, but rather use the system prompt to write the displayed text and structure the tutoring and chatting experience. I think that in designing frames, you are able to control exactly what each question looks like, so there is more control over what is explicitly being taught, in that sense, but there is limited control in verifying that a student understands a given question, answer, or correction. When designing a system prompt and an LLM tutor, while it is more work (you have to consistently make tweaks to the prompt and the behavior to get the system to do exactly what you intend for it to do), the user or student has a bit more control over what they actually learn (they are able to ask questions, say they don’t know, and in turn adjust the way they are being taught, to some degree). Critically, though, the LLM tutor could be wrong, or could just give away the answers if not given the optimal system prompt, which spoils the whole learning experience.
```

### 2. Your tutor has hardcoded questions but generates responses dynamically. When is this an advantage over canned feedback? When is it a risk?

```
We addressed this a bit above, but this is an advantage over canned feedback when a given user fails to understand elements of what is being asked of them or the concepts underlying the question or correct answer, says that, AND the tutor is able to clarify CORRECTLY! Essentially, both the user and the tutor have to cooperate with what they are being asked to do and given. It is always a risk, because there is no way to guarantee that an LLM, like the tutor, will exactly follow the system prompt (we discovered there are always loopholes) and give correct answers (hence, why there is the little “ChatGPT can make mistakes” note at the bottom of every chat). 
```

### 3. What tutoring strategy did you choose, and why? If you could redesign it, what would you change based on testing?

```
We chose to use a friendly, conversational tutoring strategy because, after discussing, we agreed that our best learning/tutoring experiences that involved dynamic/conversational teaching (rather than, say, a teacher reading off a PowerPoint or only responding to questions with more questions) created an environment where we felt comfortable enough to make mistakes and ask questions without judgment.  A tutor who encourages you and meets you where you are tends to keep you engaged longer than one who just tells you the information or that you're wrong. If we could redesign it based on testing, we would add more structured encouragement/feedback when giving corrections or reiterating the correct answer. We noticed the tutor sometimes leaned too heavily on elaborating on the correct answer without actually telling the student that they got the answer correct or guiding the student toward the right answer in a more gentle way, which made it feel more robotic. 
```

### 4. Skinner insisted on a low error rate and immediate, predictable reinforcement. Your LLM tutor is neither predictable nor error-free. Is that a problem? For whom?

```
From a cognitive perspective, immediate reinforcement is beneficial because it creates a clear link between a response and feedback, helping the learner know exactly what behavior to repeat or correct, or in this case, exactly when their understanding of a concept is correct. Skinner's model, however, assumed the reinforcement was always accurate and consistent, two things an LLM tutor cannot guarantee. This is more of a problem for some learners than others. A student who is already fairly knowledgeable about FNAF lore might catch when the tutor is wrong and self-correct. A student who knows nothing about the topic, though, could internalize a wrong answer reinforced with confident, friendly feedback. This is arguably worse than no feedback at all since it reinforces that understanding, and that can be transferred to other contexts (which is less of the case in this particular context of learning FNAF lore, but an issue more generally). The unpredictability is also an issue: Skinner believed consistency was essential to conditioning, and an LLM that phrases responses and corrections differently each time, or occasionally lets a wrong answer slide, undermines that entirely
```

### 5. A school wants to use your tutor with real students. Name three things you'd worry about.

```
While this topic is interesting and fun, I would not say it is necessarily useful in any particular situation (outside of maybe meeting someone who is a fan of FNAF), so it likely will not add to the student’s curriculum.
Students could easily game the system, for example, by rephrasing questions to get the tutor to reveal answers, or by finding prompt loopholes that bypass the intended tutoring structure. Our tutor performed well in user-testing, but we discovered that no system prompt is fully airtight, and there is no reliable way to prevent a motivated student from exploiting the tutor rather than actually learning from it. While this may not be too much of an issue in the context of learning FNAF lore (one cannot really transfer this knowledge to other areas outside the game), it is an issue with LLM tutors generally.
The tutor could provide incorrect information with full confidence, and neither the student nor the teacher observing would necessarily know. There is no built-in accountability - the tutor doesn't "know" when it's wrong - and a student who trusts it could walk away having learned something false. Again, this is not so much a concern for the topic/context of our tutor, but a general concern.
```

## Submission Checklist

- [ ] At least 5 educational questions with answers and misconceptions
- [ ] System prompt that defines the tutor's behavior
- [ ] Flask app with /chat route managing conversation history
- [ ] LiteLLM calls to a local Ollama model
- [ ] Working chat interface in the browser
- [ ] Tested with correct, incorrect, and edge-case inputs
- [ ] System prompt iterated at least once based on testing
- [ ] Reflection questions answered (above)
- [ ] Committed with meaningful commit messages
