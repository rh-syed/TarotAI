import streamlit as st
import tarot

st.title("Unlock the Secrets of Your Future with IntuiTarot")
question = st.text_area(label="What is your question?")
button = st.button("Ask My Spirit Guides")
if button and question:
    st.text("Consulting your spirit guides...hang tight...")
    response = tarot.consultTarot(question)
    st.text("")
    st.text(response)

# Move the title and previous Q&A display outside the if condition
st.title("Your Previous Questions...")
# Display the questions and answers
questionAnswers = tarot.getQAPairs()

for i, (q, a) in enumerate(questionAnswers, 1):
    st.markdown(f"**Q{i}:** {q}")
    st.markdown(f"**A{i}:** {a}\n")
    st.markdown("---")  # Using markdown for a divider for visual clarity
