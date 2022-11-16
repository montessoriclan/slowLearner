import pickle
import numpy as np
import streamlit as st

mode = pickle.load(open('prediction.pkl', 'rb'))
input_list = []

st.title("Slow learner prediction")

input_age = st.number_input("Enter the age")
input_list.append(input_age)

disability = st.radio("Choose a disability",
                      ('NA', 'Visual Impairment', 'Hearing Impairment', 'autism', 'Physical', 'Intellectual'), index=0)
if disability == 'NA':
    input_list.append(0)
elif disability == 'Visual Impairment':
    input_list.append(1)
elif disability == 'Hearing Impairment':
    input_list.append(2)
elif disability == 'autism':
    input_list.append(3)
elif disability == 'Physical':
    input_list.append(4)
elif disability == 'Intellectual':
    input_list.append(5)

input_iq = st.number_input("enter the IQ score")
input_list.append(input_iq)

handwriting = st.radio("How is the handwriting", ('legible', 'illegible'))
if handwriting == 'legible':
    input_list.append(1)
else:
    input_list.append(0)

pencil = st.radio("Can the child hold a pencil properly", ('yes', 'no'))
if pencil == 'yes':
    input_list.append(1)
else:
    input_list.append(0)

speak = st.radio("Can the child speak properly", ('yes', 'no'))
if speak == 'yes':
    input_list.append(1)
else:
    input_list.append(0)

attention = st.radio("Does the child pay attention to what you are saying", ('yes', 'no'))
if attention == 'yes':
    input_list.append(1)
else:
    input_list.append(0)

attention_span = st.number_input("What is the attention span of the child")
input_list.append(attention_span)

jokes = st.radio("Does the child laugh for jokes", ('yes', 'no'))
if jokes == 'yes':
    input_list.append(1)
else:
    input_list.append(0)

answers = st.radio("Does the child answers to the question", ('yes', 'no'))
if answers == 'yes':
    input_list.append(1)
else:
    input_list.append(0)

communication = st.radio('What is the mode of communication', ('gestures', 'words'))
if communication == 'words':
    input_list.append(1)
else:
    input_list.append(0)

if st.button('Check'):
    array = np.asarray(input_list)
    resList = array.reshape(1, -1)

    result = mode.predict(resList)[0]

    if result == 1:
        st.header("Slow Learner")
    else:
        st.header("Not a slow learner")
