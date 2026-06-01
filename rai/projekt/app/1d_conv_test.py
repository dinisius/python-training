import pandas as pd
import random
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import streamlit as st

from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import utils
from tensorflow.keras.layers import TextVectorization

conv_model = tf.saved_model.load("1d_conv")

# Dictionary
verse = {   
            0:["Refrain from anger and turn from wrath; do not fret—it leads only to evil. [Psalms 37:8]",
               
                "Get rid of all bitterness, rage and anger, brawling and slander, along with every form of malice. Be kind and compassionate to one another, forgiving each other, just as in Christ God forgave you. [Ephesians 4:31-32]", 

                "because human anger does not produce the righteousness that God desires. [James 1:20]"],


            1:["So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand. [Isaiah 41:10]", 

               "Have I not commanded you? Be strong and courageous. Do not be afraid; do not be discouraged, for the Lord your God will be with you wherever you go. [Joshua 1:9]", 

               "In God, whose word I praise—in God I trust and am not afraid. What can mere mortals do to me? [Psalms 55:4]"],


            2:["Rejoice in the Lord always. I will say it again: Rejoice! Let your gentleness be evident to all. The Lord is near. [Philippians 4:4-5]",

                "The Lord is my strength and my shield; my heart trusts in him, and he helps me. My heart leaps for joy, and with my song I praise him. [Psalms 28:7]",

                "May the God of hope fill you with all joy and peace as you trust in him, so that you may overflow with hope by the power of the Holy Spirit. [Romans 15:13]"],


            3:["The Lord is close to the brokenhearted and saves those who are crushed in spirit. [Psalm 34:18]",
               
                "Come to me, all you who are weary and burdened, and I will give you rest. [Matthew 11:28]", 

                "Peace I leave with you; my peace I give you. I do not give to you as the world gives. Do not let your hearts be troubled and do not be afraid [John 14:27]"]
        }

verse_range = range(len(verse[0]))

def web_predict_sentiment(user_input):

    emotions_weights_vector = conv_model.serve(tf.constant([user_input])).numpy()
    predicted_emotion = np.argmax(emotions_weights_vector)

    if predicted_emotion == 0:
        return ("Predicted emotion is: Anger"), (verse[0][random.choice(verse_range)])
    elif predicted_emotion == 1:
        return ("Predicted emotion is: Fear"), (verse[1][random.choice(verse_range)])
    elif predicted_emotion == 2:
        return ("Predicted emotion is: Happy"), (verse[2][random.choice(verse_range)])
    elif predicted_emotion == 3:
        return ("Predicted emotion is: Sadness"), (verse[3][random.choice(verse_range)])
        
# while True:

#     user_input = input("Share your emotion: ")
#     if user_input.lower() == "exit":
#         break
#     predict_sentiment(user_input) 



if "boolean" not in st.session_state:
    st.session_state.boolean = True

if "input_enable" not in st.session_state:
    st.session_state.input_enable = True

if "predicted_enable" not in st.session_state:
    st.session_state.predicted_enable = True

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

if "predicted_emotion" not in st.session_state:
    st.session_state.predicted_emotion = ""

if "predicted_verse" not in st.session_state:
    st.session_state.predicted_verse = ""

if "wrong" not in st.session_state:
    st.session_state.wrong = False

if "right" not in st.session_state:
    st.session_state.right = False

if "quality_buttons" not in st.session_state:
    st.session_state.quality_buttons = True



if st.session_state.input_enable:
    st.session_state.user_input = st.text_input("What is on your mind right now? ")
    st.session_state.predicted_enable = True
    st.session_state.quality_buttons = True

if (len(st.session_state.user_input) != 0):

    st.session_state.input_enable = False

    if st.session_state.predicted_enable:
        st.session_state.predicted_emotion, st.session_state.predicted_verse = web_predict_sentiment(st.session_state.user_input)
        st.session_state.predicted_enable = False

    if st.session_state.predicted_enable != True:
        st.write(st.session_state.predicted_verse)
        st.write(st.session_state.predicted_emotion)

    st.header("Was predicted emotion right or wrong?")
    column_wrong, column_right = st.columns(2)

    if (st.session_state.quality_buttons):

        with column_wrong:
            if (st.button("Wrong") and (st.session_state.right != True)):
                st.session_state.boolean = False
                st.session_state.wrong = True

                st.session_state.quality_buttons = False
                st.rerun()

        with column_right:
            if (st.button("Right") and (st.session_state.wrong != True)):
                st.session_state.boolean = False
                st.session_state.right = True

                st.session_state.quality_buttons = False
                st.rerun()

        

    with column_wrong:
        if ((st.session_state.wrong) and (st.session_state.boolean == False)):
            if(st.button("Restart")):
                st.session_state.boolean = True
                st.session_state.wrong = False
                st.session_state.user_input = ""
                st.session_state.input_enable = True
                st.rerun()

    with column_right:
        if ((st.session_state.right) and (st.session_state.boolean == False)):
            if(st.button("Restart")):
                st.session_state.boolean = True
                st.session_state.wrong = False
                st.session_state.user_input = ""
                st.session_state.input_enable = True
                st.rerun()

"nevim, nevim", st.session_state

            # flag = False
            # st.write("Yupi! Hope the verse was helpfull :)")
            # st.write(flag)
            # st.button("Restart")
                