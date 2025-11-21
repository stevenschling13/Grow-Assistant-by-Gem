"""
Grow Assistant - A plant care assistant powered by Google Gemini AI

This application helps users with plant growing advice, care tips,
and troubleshooting using Google's Gemini AI model.
"""

import os
import google.generativeai as genai
from dotenv import load_dotenv


def initialize_gemini():
    """Initialize the Gemini API with the API key from environment variables."""
    load_dotenv()
    
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found. Please set it in your .env file.\n"
            "Get your API key from: https://aistudio.google.com/app/apikey"
        )
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel('gemini-pro')


def create_grow_assistant_prompt(user_question):
    """
    Create a specialized prompt for the grow assistant.
    
    Args:
        user_question: The user's question about plant growing
        
    Returns:
        A formatted prompt string
    """
    system_context = """You are an expert plant growing assistant with deep knowledge of:
- Plant care and maintenance
- Indoor and outdoor gardening
- Soil composition and nutrients
- Pest control and disease management
- Optimal growing conditions (light, water, temperature, humidity)
- Plant propagation and germination
- Troubleshooting common plant problems

Provide helpful, practical, and encouraging advice to help users successfully grow healthy plants.
"""
    
    return f"{system_context}\n\nUser Question: {user_question}\n\nAssistant:"


def ask_grow_assistant(model, question):
    """
    Ask the grow assistant a question and get a response.
    
    Args:
        model: The Gemini model instance
        question: The user's question
        
    Returns:
        The assistant's response
    """
    prompt = create_grow_assistant_prompt(question)
    response = model.generate_content(prompt)
    return response.text


def main():
    """Main function to run the Grow Assistant."""
    print("=" * 60)
    print("Welcome to Grow Assistant - Powered by Google Gemini")
    print("=" * 60)
    print("\nYour AI-powered plant care companion!")
    print("Ask me anything about growing plants, gardening, and plant care.")
    print("Type 'quit' or 'exit' to end the conversation.\n")
    
    try:
        # Initialize the Gemini model
        model = initialize_gemini()
        print("✓ Gemini AI initialized successfully!\n")
        
        # Interactive loop
        while True:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("\nThank you for using Grow Assistant! Happy growing! 🌱")
                break
            
            try:
                print("\nGrow Assistant: ", end="", flush=True)
                response = ask_grow_assistant(model, user_input)
                print(response)
                print()
                
            except Exception as e:
                print(f"\nError getting response: {e}")
                print("Please try asking your question again.\n")
                
    except ValueError as e:
        print(f"\n❌ Configuration Error: {e}")
        print("\nSetup Instructions:")
        print("1. Copy .env.example to .env")
        print("2. Get your API key from https://aistudio.google.com/app/apikey")
        print("3. Add your API key to the .env file")
        
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
