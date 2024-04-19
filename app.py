import google.generativeai as genai
import streamlit as st

f = open("key.txt")
key = f.read()

genai.configure(api_key=key)

st.title("AI Tutor For DataScience 📝💻")
ai=genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                         system_instruction="""You are helpful ai Teaching Assistant .Give a answer for the user query when it is related to datascience topics otherwise tell sorry, i don't know and if user says hi then say Hi! how can i help you""")
if "chat_history" not in st.session_state:
    st.session_state["chat_history"]=[]

chat = ai.start_chat(history=st.session_state['chat_history'])
for msg in chat.history:

    st.chat_message(msg.role).write(msg.parts[0].text)

user_prompt=st.chat_input()

if user_prompt:
    st.chat_message("user").write(user_prompt)
    response=chat.send_message(user_prompt)
    st.chat_message("ai").write(response.text)
    print(chat.history)
    st.session_state["chat_history"]=chat.history
