import pickle
import numpy as np
import streamlit as st

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

mode = pickle.load(open('prediction.pkl', 'rb'))
input_list = []

st.title("App name")
st.header("Slow learner prediction")

int_val = st.slider('Enter the age', min_value=5, max_value=10, step=1)
input_list.append(int_val)

disability = st.radio("Choose a disability",
                      ('NA', 'Physical ', 'Sensory', 'Developmental', 'Behavioural'), index=0)
if disability == 'NA':
    input_list.append(0)
elif disability == 'Physical':
    input_list.append(1)
elif disability == 'Sensory':
    input_list.append(2)
elif disability == 'Developmental':
    input_list.append(3)
elif disability == 'Behavioural':
    input_list.append(4)

input_iq = st.number_input("enter the IQ score", min_value=0)
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

attention_span = st.number_input("What is the attention span of the child", min_value=0)
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

    try:
        result = mode.predict(resList)[0]
    except:
        st.error("Please input correct number of elements")

    if result == 1:
        st.header("Slow Learner")
    else:
        st.header("Not a slow learner")
