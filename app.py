import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Set page configuration
st.set_page_config(
    page_title="My Gaming AI Assistant",
    page_icon="🎮",
    layout="wide"
)

# Title
st.title("🤖ai assistant")
st.markdown("### Welcome to Your Personal Gaming Companion! 👾")
st.info("🎯 I'm here to help you with game recommendations, strategies, guides, tips & tricks, and answer all your gaming questions. Whether you're a casual player or hardcore gamer, let's level up together!")

# Initialize personality in session state
if "personality" not in st.session_state:
    st.session_state.personality = "Friendly"

# Personality configurations
personality_configs = {
    "Friendly": {
        "icon": "😊",
        "system_prompt": "You are a warm and friendly gaming assistant. Chat with users like a good friend who loves gaming. Be encouraging, supportive, and enthusiastic. Use casual language and share your excitement about games. Make users feel comfortable and welcomed.",
        "description": "Warm and friendly, chat like friends"
    },
    "Professional": {
        "icon": "🎯",
        "system_prompt": "You are a rigorous and professional gaming consultant with deep expertise in game analysis, strategies, and industry knowledge. Provide accurate, well-researched advice with detailed explanations. Be precise, thorough, and objective in your recommendations.",
        "description": "Rigorous and professional, give accurate advice"
    },
    "Humorous": {
        "icon": "😄",
        "system_prompt": "You are a fun and humorous gaming buddy with a great sense of humor. Make conversations entertaining with witty comments, gaming jokes, and playful banter. Keep things light and interesting while still being helpful. Don't take yourself too seriously!",
        "description": "Relaxed and humorous, interesting chat"
    }
}

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Add system prompt based on personality
    current_personality = personality_configs[st.session_state.personality]
    st.session_state.messages.append({
        "role": "system",
        "content": current_personality["system_prompt"]
    })

# Sidebar - Settings
with st.sidebar:
    st.header("⚙️ Settings")

    # AI Personality Selection
    st.subheader("🤖 AI Personality")

    # Create personality options with icons
    personality_options = {
        f"{config['icon']} {name}": name
        for name, config in personality_configs.items()
    }

    selected_display = st.selectbox(
        "Choose AI personality style:",
        options=list(personality_options.keys()),
        index=list(personality_configs.keys()).index(st.session_state.personality),
        help="Select how the AI assistant should interact with you"
    )

    selected_personality = personality_options[selected_display]

    # Display personality description
    st.caption(personality_configs[selected_personality]["description"])

    # Update personality if changed
    if selected_personality != st.session_state.personality:
        st.session_state.personality = selected_personality
        # Update system prompt
        st.session_state.messages[0] = {
            "role": "system",
            "content": personality_configs[selected_personality]["system_prompt"]
        }
        st.success(f"Personality changed to {selected_personality}! 🎉")
        st.rerun()

    st.divider()

    # Clear chat history button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = [st.session_state.messages[0]]  # Keep system prompt
        st.rerun()

    st.divider()

    # Quick question templates
    st.subheader("💡 Quick Questions")
    quick_questions = [
        "🎯 Recommend some good single-player games",
        "🎮 How to improve FPS gaming skills?",
        "🔥 What are the trending games recently?",
        "❓ What's the difference between RPG and MMORPG?"
    ]

    for question in quick_questions:
        if st.button(question, key=question):
            # Add quick question to chat (remove emoji from actual question)
            clean_question = question.split(" ", 1)[1]
            st.session_state.messages.append({"role": "user", "content": clean_question})
            st.rerun()

# Display chat history (skip system prompt)
for message in st.session_state.messages[1:]:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything about gaming..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            # Call Groq API
            stream = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.messages,
                temperature=0.7,
                max_tokens=2048,
                stream=True
            )

            # Stream the response
            for chunk in stream:
                if chunk.choices[0].delta.content is not None:
                    full_response += chunk.choices[0].delta.content
                    message_placeholder.markdown(full_response + "▌")

            # Display complete response
            message_placeholder.markdown(full_response)

        except Exception as e:
            error_message = f"❌ Error occurred: {str(e)}"
            message_placeholder.markdown(error_message)
            full_response = error_message

    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Footer
st.divider()
st.caption("💡 Tip: You can ask about game recommendations, strategies, gaming knowledge, and more! Try different AI personalities for different experiences! 🎮✨")
