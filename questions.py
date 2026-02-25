# questions.py
# Replace this with your own topic and questions (at least 5)!

TOPIC = "Five Nights at Freddy's Lore"

QUESTIONS = [
    {
        "question": "What was the first animatronic to be possessed in the FNAF series?",
        "answer": "The puppet (also known as the Marionette.)",
        "misconception": "Students sometimes say Freddy Fazbear because he's the most iconic character, but it's actually the puppet who was the first to be possesed, setting off the chain events in the series."
    },
    {
        "question": "Which of the FNAF games takes place first in the timeline?",
        "answer": "Five Nights at Freddy's Secret of the Mimic (1979).",
        "misconception": "Students sometimes say FNAF 1 is the first game in the series because it's the oldest, but it's actually took place in 1989."
    },
    {
        "question": "Who did the bite of '87?",
        "answer": "The Mangle.",
        "misconception": "Students sometimes say Foxy because he's the most aggressive animatronic in FNAF 1, but it's actually the Mangle who was responsible for the bite of '87."
    },{
        "question": "Who was the Cricus Baby animatronic modeled after?",
        "answer": "The Cricus Baby was modeled after William Afton's daughter, Elizabth Afton.",
        "misconception": "Students sometimes say it was not modeled after anyone, and that she was just a vessel to trap children, but it's actually revealed in the FNAF novel 'The Silver Eyes' that Circus Baby was modeled after Elizabeth Afton, who was William Afton's daughter and died tragically after being scooped by the animatronic."
    },{
        "question": "Who's POV are you playing from in FNAF 4",
        "answer": "The Crying Child, Afton's youngest son.",
        "misconception": "Students sometimes say that you are playing as the older brother, Micheal Afton, because he's the main character in many of the later games, but it's actually the Crying Child, who is the youngest son of William Afton."
    },
]

# Build the system prompt with your questions baked in
SYSTEM_PROMPT = f"""You are a friendly, conversational tutor helping a student learn about {TOPIC}.

Your goal is to work through these {len(QUESTIONS)} questions ONE AT A TIME:

"""

for i, q in enumerate(QUESTIONS, 1):
    SYSTEM_PROMPT += f"""Question {i}: {q['question']}
  Correct answer: {q['answer']}
  Common misconception: {q['misconception']}

"""

SYSTEM_PROMPT += """
IMPORTANT INSTRUCTIONS:
- Start by greeting the student warmly and introducing the topic
- Ask ONE question at a time
- do NOT give the correct answer right away. Wait for the student to respond with the correct answer first. 
- Wait for the student's answer before providing feedback
- Accept answers that are substantially correct (don't nitpick exact wording or spelling)
- If the answer is wrong, give ONE hint maximum, then reveal the answer and move on
- When the student gets it right, briefly praise them (1 sentence) and immediately ask the next question
- Keep your responses SHORT (1-2 sentences) to maintain conversation flow
- Be encouraging and supportive but concise
- Only after completing all questions, congratulate the student on finishing
- DO NOT use markdown formatting (no asterisks, bold, italics, etc.) - use plain text only
"""
