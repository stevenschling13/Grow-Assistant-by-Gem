# Grow Assistant by Gemini 🌱

An intelligent plant care assistant powered by Google's Gemini AI. Get expert advice on plant growing, gardening, troubleshooting, and care tips through an interactive conversational interface.

## Features

- 🤖 **AI-Powered Advice**: Leverages Google's Gemini Pro model for intelligent plant care guidance
- 🌿 **Comprehensive Knowledge**: Covers indoor/outdoor gardening, pest control, soil management, and more
- 💬 **Interactive Chat**: Easy-to-use command-line interface for asking questions
- 🔒 **Secure**: Uses environment variables to protect your API key
- 🚀 **Easy Setup**: Simple installation and configuration process

## Prerequisites

- Python 3.8 or higher
- A Google AI Studio API key ([Get one here](https://aistudio.google.com/app/apikey))

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/stevenschling13/Grow-Assistant-by-Gem.git
   cd Grow-Assistant-by-Gem
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your Google API key
   # GOOGLE_API_KEY=your_actual_api_key_here
   ```

## Usage

Run the Grow Assistant:

```bash
python grow_assistant.py
```

### Example Interaction

```
Welcome to Grow Assistant - Powered by Google Gemini
============================================================

Your AI-powered plant care companion!
Ask me anything about growing plants, gardening, and plant care.
Type 'quit' or 'exit' to end the conversation.

✓ Gemini AI initialized successfully!

You: How often should I water my tomato plants?

Grow Assistant: Tomato plants typically need consistent watering...
[detailed response from Gemini AI]

You: What's the best soil for growing herbs indoors?

Grow Assistant: For indoor herb gardening, you'll want to use...
[detailed response from Gemini AI]

You: exit

Thank you for using Grow Assistant! Happy growing! 🌱
```

## Configuration

The application uses environment variables for configuration. See `.env.example` for the required variables:

- `GOOGLE_API_KEY`: Your Google AI Studio API key (required)

## Getting Your API Key

1. Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key
5. Add it to your `.env` file

## Topics You Can Ask About

- 🌱 Plant care and maintenance
- 🏡 Indoor and outdoor gardening
- 🌍 Soil composition and nutrients
- 🐛 Pest control and disease management
- ☀️ Light, water, temperature requirements
- 🌿 Plant propagation and germination
- 🔧 Troubleshooting plant problems
- 🌺 Specific plant species care guides

## Project Structure

```
Grow-Assistant-by-Gem/
├── grow_assistant.py    # Main application file
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variable template
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
└── README.md           # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Powered by [Google Gemini AI](https://ai.google.dev/)
- Built with the [Google Generative AI Python SDK](https://github.com/google/generative-ai-python)

## Support

If you encounter any issues or have questions:
1. Check that your API key is correctly set in the `.env` file
2. Ensure you have an active internet connection
3. Verify your API key has not exceeded its quota
4. Check the [Google AI Studio documentation](https://ai.google.dev/docs)

## Disclaimer

This tool provides general plant care advice based on AI-generated responses. For specific plant diseases or critical situations, please consult with a local gardening expert or agricultural extension service.

---

Happy Growing! 🌱🌿🌻
