import streamlit as st
import requests
from pytube import Search

# Load API Key securely
GROQ_API_KEY = "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"  # Replace with your actual API key

# Function to generate quiz questions using Groq API
def generate_question_and_answer(topic, difficulty):
    url = "https://api.groq.com/openai/v1/chat/completions"  # Corrected Groq API URL
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",  # Groq's Llama 3 model
        "messages": [{"role": "user", "content": f"Generate a {difficulty} level multiple-choice quiz question on {topic}. Include four answer choices (A, B, C, D), the correct answer, and a detailed explanation of why it's correct."}],
        "max_tokens": 300  # Increased max tokens for full output
    }

    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        content = response.json()["choices"][0]["message"]["content"]
        
        # Splitting response into parts (assuming structured output)
        try:
            parts = content.split("\n")
            question = parts[0]
            options = "\n".join(parts[1:5])  # Assuming 4 options
            correct_answer = parts[5].replace("Correct Answer:", "").strip()
            explanation = "\n".join(parts[6:])  # Remaining lines as explanation
            return question, options, correct_answer, explanation
        except:
            return content, "", "", "Error in parsing response"
    else:
        return f"Error: {response.json()}", "", "", ""

# Streamlit App
st.title("🎓 Interactive Study Quiz")
st.write("Welcome! Let's test your knowledge.")

# User Inputs
topic = st.text_input("📚 Enter a topic:")
difficulty = st.selectbox("⚡ Select difficulty level:", ["Beginner", "Intermediate", "Advanced"])

# Session state for storing quiz data
if "quiz_data" not in st.session_state:
    st.session_state.quiz_data = []

# Generate Quiz
if st.button("📝 Generate Quiz Question"):
    if topic:
        question, options, correct_answer, explanation = generate_question_and_answer(topic, difficulty)
        st.session_state.quiz_data.append({"question": question, "options": options, "correct_answer": correct_answer, "explanation": explanation})
    else:
        st.warning("⚠️ Please enter a topic!")

# Display Quiz Questions
if st.session_state.quiz_data:
    st.subheader("🧐 Your Quiz")
    for i, quiz in enumerate(st.session_state.quiz_data):
        st.write(f"**Q{i+1}:** {quiz['question']}")
        st.write(quiz["options"])  # Display multiple-choice options

        # User input for answer
        user_answer = st.text_input(f"✍️ Your answer for Q{i+1} (A/B/C/D)", key=f"answer_{i}")

        if user_answer:
            if user_answer.upper() == quiz["correct_answer"]:
                st.success(f"✅ Correct! 🎉 {quiz['explanation']}")
            else:
                st.error(f"❌ Wrong! The correct answer is **{quiz['correct_answer']}**. \n\n📖 Explanation: {quiz['explanation']}")

# YouTube Video Suggestions
if st.button("🎥 Get YouTube Video Suggestions"):
    if topic:
        st.subheader("📺 YouTube Video Suggestions")
        search = Search(f"{topic} {difficulty} tutorial")
        for video in search.results[:5]:
            st.write(f"[{video.title}]({video.watch_url})")
    else:
        st.warning("⚠️ Please enter a topic first!")
