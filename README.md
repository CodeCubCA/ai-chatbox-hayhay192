# AI Chatbox - Gaming Assistant

An intelligent AI-powered chatbot built with Streamlit and Groq API. This interactive assistant helps gamers with recommendations, strategies, tips, and answers to all gaming-related questions.

## Live Demo

Try the live app: [AI Gaming Assistant](https://ai-chatbox-haydrian-codecub.streamlit.app)

## Features

- **Real-time AI Conversation** - Powered by Groq's advanced language models
- **Multiple Personalities** - Choose between Friendly, Professional, or Humorous chat styles
- **Gaming Focus** - Specialized in game recommendations, strategies, and gaming advice
- **Context-Aware Responses** - Maintains conversation history for coherent interactions
- **Beautiful UI** - Clean Streamlit interface with custom styling
- **Cloud Deployed** - Hosted on Streamlit Cloud for easy access

## Technologies Used

- **Python** - Backend programming language
- **Streamlit** - Web application framework
- **Groq API** - AI language model integration
- **python-dotenv** - Environment variable management
- **Git** - Version control

## Installation

### Prerequisites

- Python 3.8 or higher
- A Groq API key (get one at [console.groq.com](https://console.groq.com))

### Setup Steps

1. Clone the repository
```bash
git clone https://github.com/CodeCubCA/ai-chatbox-hayhay192.git
cd ai-chatbox-hayhay192
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Set up environment variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your Groq API key
# GROQ_API_KEY=your_api_key_here
```

4. Run the application
```bash
streamlit run app.py
```

5. Open your browser and navigate to `http://localhost:8501`

## Configuration

### Personality Modes

The AI assistant offers three distinct personality modes:

1. **Friendly** 😊 - Warm and friendly, like chatting with a gaming buddy
2. **Professional** 🎯 - Rigorous and expert, provides detailed analysis
3. **Humorous** 😄 - Fun and entertaining with gaming jokes and banter

### Environment Variables

Required environment variables (see `.env.example`):

- `GROQ_API_KEY` - Your Groq API key for AI model access

## Usage

1. Launch the app
2. Select your preferred AI personality from the sidebar
3. Start chatting with the AI assistant
4. Ask about game recommendations, strategies, tips, or any gaming questions
5. Use the "Clear Chat History" button to start a fresh conversation

## Project Structure

```
ai-chatbox-hayhay192/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variable template
├── .gitignore            # Git ignore rules
├── README.md             # This file
└── .github/              # GitHub configuration
```

## Features in Detail

### AI-Powered Conversations
- Uses Groq's Llama 3.3 70B Versatile model
- Maintains conversation context for natural interactions
- Provides knowledgeable responses about gaming topics

### User Interface
- Clean, modern design with Streamlit
- Sidebar for personality selection
- Chat history display
- Easy-to-use message input
- Clear chat functionality

## Deployment

This project is deployed on Streamlit Cloud. To deploy your own version:

1. Fork this repository
2. Sign up at [streamlit.io](https://streamlit.io)
3. Connect your GitHub repository
4. Add your `GROQ_API_KEY` to Streamlit Cloud secrets
5. Deploy!

## Contributing

This is a personal project, but feedback and suggestions are welcome! Feel free to open an issue or reach out.

## Author

**Haydrian**
- Age: 13
- School: KLO
- GitHub: [@CodeCubCA](https://github.com/CodeCubCA)

## Acknowledgments

- Groq for providing the AI API
- Streamlit for the amazing web framework
- GitHub Classroom for the assignment structure
- Claude Code for development assistance

## License

This project is open source and available for educational purposes.

---

Made with passion by Haydrian | 2025
