import streamlit as st

# Adding title
st.title('Chatbot by Danyal')

st.write('Welcome to Chatbot by Danyal please state your Question')

# Streamlit input and output
question = st.text_input(' Ask a question :', key = 'unique_key' )

if question:
    if question.lower() == 'hello' :
         st.write('Hello! how may i assist you')
    elif question.lower() == ' 2 + 2 ' :
         st.write('4')
    elif question.lower() == ' what are the name of the planets in our solar system' :
         st.write(' Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune')
    elif question.lower() == 'what is DMAS rule' :
         st.write('In DMAS Rule. First comes Division then Multiplication then Addition and finally Subtraction')
    elif question.lower() == '6 * 4' :
         st.write('24')
    