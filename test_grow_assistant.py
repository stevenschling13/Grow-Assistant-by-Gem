"""
Basic tests for Grow Assistant

These tests verify the basic functionality without requiring an API key.
"""

import sys
import os

# Add the parent directory to the path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from grow_assistant import create_grow_assistant_prompt


def test_prompt_creation():
    """Test that the prompt creation function works correctly."""
    question = "How do I water my plants?"
    prompt = create_grow_assistant_prompt(question)
    
    # Check that the prompt contains the question
    assert question in prompt, "User question should be in the prompt"
    
    # Check that the prompt contains system context
    assert "plant growing assistant" in prompt.lower(), "Prompt should contain system context"
    assert "plant care" in prompt.lower(), "Prompt should mention plant care"
    
    print("✓ Prompt creation test passed")


def test_imports():
    """Test that all required modules can be imported."""
    try:
        import google.generativeai as genai
        print("✓ google-generativeai module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import google-generativeai: {e}")
        return False
    
    try:
        from dotenv import load_dotenv
        print("✓ python-dotenv module imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import python-dotenv: {e}")
        return False
    
    return True


def test_file_structure():
    """Test that all required files exist."""
    base_path = os.path.dirname(os.path.abspath(__file__))
    
    required_files = [
        'grow_assistant.py',
        'requirements.txt',
        '.env.example',
        '.gitignore',
        'LICENSE',
        'README.md'
    ]
    
    all_exist = True
    for filename in required_files:
        filepath = os.path.join(base_path, filename)
        if os.path.exists(filepath):
            print(f"✓ {filename} exists")
        else:
            print(f"✗ {filename} is missing")
            all_exist = False
    
    return all_exist


if __name__ == "__main__":
    print("=" * 60)
    print("Running Grow Assistant Tests")
    print("=" * 60)
    print()
    
    print("Test 1: File Structure")
    print("-" * 60)
    file_test = test_file_structure()
    print()
    
    print("Test 2: Module Imports")
    print("-" * 60)
    import_test = test_imports()
    print()
    
    print("Test 3: Prompt Creation")
    print("-" * 60)
    try:
        test_prompt_creation()
        prompt_test = True
    except Exception as e:
        print(f"✗ Prompt creation test failed: {e}")
        prompt_test = False
    print()
    
    print("=" * 60)
    print("Test Summary")
    print("=" * 60)
    all_passed = file_test and import_test and prompt_test
    
    if all_passed:
        print("✓ All tests passed!")
        sys.exit(0)
    else:
        print("✗ Some tests failed")
        sys.exit(1)
