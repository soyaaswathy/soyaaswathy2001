import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Study Buddy", page_icon="📚")

client = Groq(api_key="dsk_hwgdweiudhe7y23erh2rbjhfbdugdwehdfihw")

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a friendly AI tutor who explains clearly."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300
    )
    return response.choices[0].message.content.strip()

st.title("📚 AI Study Buddy")
st.caption("Your simple personal learning assistant")

option = st.selectbox(
    "What do you want to do?",
    ["Explain a Topic", "Summarize Notes", "Generate Quiz"]
)

text = st.text_area("Enter your topic or notes:")

if st.button("Ask AI"):
    if not text.strip():
        st.warning("Please enter some text.")
    else:
        with st.spinner("Thinking..."):
            if option == "Explain a Topic":
                prompt = f"Explain this simply for a student:\n{text}"
            elif option == "Summarize Notes":
                prompt = f"Summarize this clearly:\n{text}"
            else:
                prompt = f"Create 5 quiz questions with answers from this text:\n{text}"

            result = ask_ai(prompt)

        st.success("Done!")
        st.write(result)