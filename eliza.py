"""
Custom ELIZA-style chatbot (1966-inspired)
Rule-based pattern matching with reflection
"""

import re
import random

class CustomELIZA:
    """
    A simple rule-based psychotherapist chatbot.
    Uses pattern matching and keyword responses.
    """
    
    def __init__(self):
        # Reflection rules: map user pronouns to bot pronouns
        self.reflections = {
            "i am": "you are",
            "i'm": "you are",
            "i": "you",
            "me": "you",
            "my": "your",
            "mine": "yours",
            "you are": "I am",
            "you're": "I am",
            "you": "me",
            "your": "my",
            "yours": "mine",
            "am": "are",
            "was": "were",
            "i'd": "you would",
            "i've": "you have",
            "i'll": "you will",
        }
        
        # Pattern-response rules (priority order)
        self.rules = [
            # Rule 1: Greeting
            (r"hello|hi|hey|good morning|good afternoon", 
             ["Hello. How are you feeling today?",
              "Hi there. What's on your mind?"]),
            
            # Rule 2: Name
            (r"my name is (\w+)|i am (\w+)|i'm (\w+)",
             ["Nice to meet you, {}. Tell me about yourself.",
              "Hello {}. How can I help you today?"]),
            
            # Rule 3: Stressed / Anxiety
            (r"stress|anxious|nervous|worried|overwhelm",
             ["Why do you feel stressed?",
              "What situations make you feel this way?",
              "Let's talk about what's causing your stress."]),
            
            # Rule 4: Tired / Sleep
            (r"tired|exhausted|sleep|fatigue|no energy",
             ["How many hours of sleep do you get?",
              "What keeps you from resting well?",
              "Fatigue often has underlying causes. Tell me more."]),
            
            # Rule 5: Exams / Work pressure
            (r"exam|test|assignment|deadline|project",
             ["Academic pressure can be intense. What specifically concerns you?",
              "How do you prepare for your exams?",
              "Many students feel this way. Let's break it down."]),
            
            # Rule 6: Family / Mother
            (r"mother|mom|mum|father|dad|parent|family",
             ["Tell me more about your family relationship.",
              "How does that make you feel?",
              "Family dynamics are complex. What's on your mind?"]),
            
            # Rule 7: Need / Want statements
            (r"i need (.*)|i want (.*)|i wish (.*)",
             ["Why do you need {}?",
              "What would change if you had {}?",
              "Is that something you can control?"]),
            
            # Rule 8: Because statements
            (r"because (.*)",
             ["I see. And how does that affect you?",
              "Does that reason feel valid to you?",
              "Tell me more about that connection."]),
            
            # Rule 9: Sad / Depressed
            (r"sad|depress|unhappy|down|miserable",
             ["I'm sorry you're feeling this way. What happened?",
              "When did you start feeling this way?",
              "Let's talk through this together."]),
            
            # Rule 10: Happy / Good
            (r"happy|great|wonderful|excellent|good",
             ["That's wonderful to hear! What contributed to this?",
              "How can you have more moments like this?",
              "I'm glad things are going well."]),
            
            # Rule 11: I feel statements
            (r"i feel (.*)",
             ["Why do you feel {}?",
              "Does that feeling come up often?",
              "How long have you felt this way?"]),
            
            # Rule 12: Default / Fallback
            (r".*",
             ["Can you tell me more about that?",
              "I see. Please continue.",
              "What does that mean to you?",
              "How does that make you feel?"]),
        ]
        
        # Fallback responses (if no pattern matches at all)
        self.fallbacks = [
            "That's interesting. Tell me more.",
            "I'm listening. Please go on.",
            "How do you feel about that?",
            "What else comes to mind?",
        ]
    
    def reflect(self, text: str) -> str:
        """
        Apply reflection rules to make the bot sound more natural.
        Example: "I am sad" → "you are sad"
        """
        words = text.lower().split()
        for i, word in enumerate(words):
            for pattern, replacement in self.reflections.items():
                if word == pattern or text.find(pattern) != -1:
                    return text.replace(pattern, replacement)
        return text
    
    def respond(self, user_input: str) -> str:
        """
        Main response generator.
        Matches user input against rules and returns appropriate response.
        """
        user_input = user_input.lower().strip()
        
        # Try each rule in order
        for pattern, responses in self.rules:
            match = re.search(pattern, user_input, re.IGNORECASE)
            if match:
                # Extract captured groups (like name or need)
                groups = match.groups()
                response = random.choice(responses)
                
                # Fill in placeholders with reflected user input
                if groups:
                    # Use the first non-None group
                    captured = next((g for g in groups if g), "")
                    reflected = self.reflect(captured)
                    response = response.format(reflected)
                
                return response
        
        # No pattern matched
        return random.choice(self.fallbacks)
    
    def converse(self):
        """Interactive conversation loop for terminal testing."""
        print("ELIZA (Custom): Hello. I'm a psychotherapist chatbot. How can I help?")
        print("Type 'quit' to exit.\n")
        
        while True:
            user = input("You: ")
            if user.lower() in ["quit", "exit", "bye"]:
                print("ELIZA: Goodbye. Take care of yourself.")
                break
            print(f"ELIZA: {self.respond(user)}")


# Function for compatibility with chat_comparison.py
def get_eliza_response(user_input: str) -> str:
    """Wrapper function to maintain compatibility with the GUI."""
    eliza = CustomELIZA()
    return eliza.respond(user_input)


if __name__ == "__main__":
    eliza = CustomELIZA()
    eliza.converse()