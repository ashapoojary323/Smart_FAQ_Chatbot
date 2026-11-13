import streamlit as st

st.set_page_config(page_title="Smart FAQ Chatbot")

st.title("🎓 Smart FAQ Chatbot")
st.write("Welcome! Ask multiple questions about your course.")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input("Ask your question here...")

def get_answer(question):
    q = question.lower()

    if "python" in q:
        return "Python is a programming language used in AI, ML and web development."

    elif "ai" in q:
        return "Artificial Intelligence enables machines to perform intelligent tasks."

    elif "machine learning" in q:
        return "Machine Learning allows computers to learn from data."

    else:
        return "Sorry, I don't have an answer to that question yet."

if question:
    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    answer = get_answer(question)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

    st.rerun()