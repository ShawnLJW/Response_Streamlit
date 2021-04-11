import streamlit as st
from joblib import load
from nlpEngine import find_root_words

industry_vectorizer = load('industry_vectorizer.sav')
industry_classifier = load('industry_classifier.sav')
school_vectorizer = load('school_vectorizer.sav')
school_classifier = load('school_classifier.sav')

st.write("""# FutureMe Response Tagger
## Enter the student's responses of the following questions
""")

industry_response = st.text_input('The industry I\'m most interested in is')
industry_prediction = ' '.join(find_root_words(industry_response))
industry_prediction = industry_vectorizer.transform([industry_prediction]).toarray()
industry_prediction = industry_classifier.predict(industry_prediction)[0]

school_response = st.text_input('What is your 1st choice school?')
school_prediction = ' '.join(find_root_words(school_response))
school_prediction = school_vectorizer.transform([school_prediction]).toarray()
school_prediction = school_classifier.predict(school_prediction)[0]

st.write('This student wants to go to **{}** and enter the **{}** industry'.format(school_prediction,industry_prediction))