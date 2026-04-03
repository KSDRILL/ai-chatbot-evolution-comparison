"""
Modern LLM Chatbot using Hugging Face Transformers
Model: Qwen/Qwen2.5-1.5B-Instruct
"""

from transformers import pipeline
import warnings
warnings.filterwarnings("ignore")

class ModernLLM:
    def __init__(self, model_name="Qwen/Qwen2.5-1.5B-Instruct"):
        print(f"Loading model: {model_name}...")
        print("This may take a few minutes on first run...")
        self.chatbot = pipeline(
            "text-generation",
            model=model_name
        )
        print("Model ready!")
    
    def get_response(self, user_input: str, max_tokens: int = 150) -> str:
        """
        Generate response using instruction-tuned LLM.
        """
        prompt = f"User: {user_input}\nAssistant:"
        
        try:
            response = self.chatbot(
                prompt,
                max_new_tokens=max_tokens,
                do_sample=True,
                temperature=0.7,
                top_p=0.9,
                repetition_penalty=1.1
            )
            
            # Extract only the assistant's response
            full_text = response[0]["generated_text"]
            assistant_part = full_text.split("Assistant:")[-1]
            
            return assistant_part.strip()
        
        except Exception as e:
            return f"[Model error: {str(e)}]"
    
    def converse(self):
        """Interactive conversation loop."""
        print("Modern LLM: Hello! I'm an AI assistant. How can I help you?")
        print("Type 'quit' to exit.\n")
        
        while True:
            user = input("You: ")
            if user.lower() in ["quit", "exit", "bye"]:
                print("LLM: Goodbye! Feel free to return anytime.")
                break
            
            print(f"LLM: {self.get_response(user)}")


# Singleton instance for performance
_llm_instance = None

def get_llm_response(user_input: str) -> str:
    """Wrapper function for compatibility with chat_comparison.py."""
    global _llm_instance
    if _llm_instance is None:
        _llm_instance = ModernLLM()
    return _llm_instance.get_response(user_input)


if __name__ == "__main__":
    llm = ModernLLM()
    llm.converse()