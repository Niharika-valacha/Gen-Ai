import streamlit as st
from openai import ChatCompletion
import google.generativeai as genai


def generate_mcqs():
    st.title("MCQ Generator")
    st.markdown("---")

    
    with open("C:/Users/Hp/Desktop/python/genAi/key/key.txt", "r") as f:
        API_KEY_MCQ = f.read().strip()

    
    client_mcq = ChatCompletion(api_key=API_KEY_MCQ)

   
    prompt = st.text_input("Enter any topic")

if st.button("Generate"):
    response = client.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant. Given a Data Science topic, you always generate 3 MCQ questions for a quiz."},
            {"role": "user", "content": prompt}
        ]
    )
    st.markdown("### MCQs Generated:")
    st.write(response.choices[0].text.strip())



def code_reviewer():
    st.title("Code Reviewer")
    st.markdown("---")

    
    with open("C:/Users/Hp/Desktop/python/genAi/key/key.txt", "r") as f:
        API_KEY_CODE = f.read().strip()

    
    client_code = ChatCompletion(api_key=API_KEY_CODE)

    
    prompt = st.text_area("Enter Your code 📝")

    
    if st.button("💡 Generate"):
        response = client_code.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant. Given a code, you need to check the code and find the errors in the code, explain them more clearly with examples, and fix them."},
                {"role": "user", "content": prompt}
            ]
        )
        st.markdown("### Code Review:")
        st.write(response.choices[0]["message"]["content"])

# Function for AI Conversational Tutor
def ai_conversational_tutor():
    st.title("AI Conversational Tutor")
    st.markdown("---")

    
    with open("C:/Users/Hp/Desktop/python/genAi/key/gemini.txt", "r") as f:
        API_KEY_AI_TUTOR = f.read().strip()

    
    genai.configure(api_key=API_KEY_AI_TUTOR)

    
    st.chat_message("ai").write("Hi, How may I help you today?")

    
    user_input = st.chat_input()

    
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                                  system_instruction="""You are a helpful AI Assistant who answers all the user queries politely.
                                  If someone asks your name, tell them that your name is jarvis the Robot.""")

    
    if "memory" not in st.session_state:
        st.session_state["memory"] = []

    chat = model.start_chat(history=st.session_state['memory'])

    
    for message in chat.history:
        st.chat_message(message.role).write(message.parts[0].text)

    
    if user_input:
        st.chat_message("user").write(user_input)
        response = chat.send_message(user_input)
        st.chat_message("ai").write(response.text)
        st.session_state["memory"] = chat.history

# Sidebar navigation
selected_option = st.sidebar.radio("Choose Your GENAI App", ("MCQ Generator", "Code Reviewer", "AI Conversational Tutor"))

# Main content based on selected option
if selected_option == "MCQ Generator":
    generate_mcqs()
elif selected_option == "Code Reviewer":
    code_reviewer()
else:
    ai_conversational_tutor()
