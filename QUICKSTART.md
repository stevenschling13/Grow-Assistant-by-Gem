# Quick Start Guide

Get up and running with Grow Assistant in 5 minutes!

## Prerequisites

- Python 3.8+
- Google AI Studio API key ([Get one free here](https://aistudio.google.com/app/apikey))

## Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/stevenschling13/Grow-Assistant-by-Gem.git
cd Grow-Assistant-by-Gem

# 2. Create a virtual environment (recommended)
python -m venv venv

# 3. Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Set up your API key
cp .env.example .env
# Edit .env and replace 'your_api_key_here' with your actual API key

# 6. Run the application
python grow_assistant.py
```

## First Use

Once the application starts, you can ask questions like:

- "What are the best plants for low light conditions?"
- "How often should I water my succulents?"
- "My tomato plant leaves are turning yellow, what should I do?"
- "What soil mix is best for growing herbs indoors?"

Type `exit` or `quit` to end the conversation.

## Programmatic Use

You can also use Grow Assistant in your own Python scripts:

```python
from grow_assistant import initialize_gemini, ask_grow_assistant

# Initialize
model = initialize_gemini()

# Ask a question
response = ask_grow_assistant(model, "How do I propagate basil?")
print(response)
```

See `example.py` for more examples.

## Troubleshooting

**Error: "GOOGLE_API_KEY not found"**
- Make sure you created a `.env` file from `.env.example`
- Verify your API key is correctly pasted in the `.env` file

**Error: "ModuleNotFoundError"**
- Make sure you installed the dependencies: `pip install -r requirements.txt`
- Verify your virtual environment is activated

**Need Help?**
- Check the full [README.md](README.md) for detailed documentation
- Review [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines
- Open an issue on GitHub if you encounter problems

## What's Next?

- ⭐ Star the repository if you find it helpful
- 🍴 Fork it to customize for your needs
- 🤝 Contribute improvements back to the project
- 📢 Share it with other plant enthusiasts!

Happy Growing! 🌱