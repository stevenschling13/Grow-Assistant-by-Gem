"""
Example: Using Grow Assistant Programmatically

This script demonstrates how to use the Grow Assistant
as a library in your own Python code.
"""

from grow_assistant import initialize_gemini, ask_grow_assistant


def main():
    """Example of using Grow Assistant programmatically."""
    
    # Initialize the Gemini model
    print("Initializing Grow Assistant...")
    model = initialize_gemini()
    print("✓ Initialized successfully!\n")
    
    # Example questions to ask
    questions = [
        "What are the best indoor plants for beginners?",
        "How do I know if I'm overwatering my plants?",
        "What is the ideal temperature for growing tomatoes?"
    ]
    
    # Ask each question and display the response
    for i, question in enumerate(questions, 1):
        print(f"Question {i}: {question}")
        print("-" * 60)
        
        try:
            response = ask_grow_assistant(model, question)
            print(f"Answer: {response}")
            print("\n" + "=" * 60 + "\n")
            
        except Exception as e:
            print(f"Error: {e}\n")
    
    print("Example completed!")


if __name__ == "__main__":
    main()