import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import utils
from tensorflow.keras.layers import TextVectorization

conv_model = tf.saved_model.load("1d_conv")


def predict_sentiment(text):

    emotions_weights_vector = conv_model.serve(tf.constant([text])).numpy()
    predicted_emotion = np.argmax(emotions_weights_vector)

    if predicted_emotion == 0:
        print("Predicted emotion is: Anger")
    elif predicted_emotion == 1:
        print("Predicted emotion is: Fear")
    elif predicted_emotion == 2:
        print("Predicted emotion is: Happy")
    elif predicted_emotion == 3:
        print("Predicted emotion is: Sadness")


while True:

    user_input = input("Share your emotion: ")
    if user_input.lower() == "exit":
        break
    predict_sentiment(user_input) 

# # * Evidence examples
# print("##############################################################")
# print("EVIDENCE EXAMPLES")
# print("ANGER        FEAR        HAPPY       SADNESS")
# print(conv_model.serve(tf.constant(['I am upset'])).numpy())                                                                # * Sadness
# print(conv_model.serve(tf.constant(['I still feel fear after everything that happened today'])).numpy())                    # * Fear
# print(conv_model.serve(tf.constant(['I’m going to bed full of joy because today was amazing'])).numpy())                    # * Joy        
# print(conv_model.serve(tf.constant(['I’m still angry about the argument from this afternoon'])).numpy())                    # * Anger
# print(conv_model.serve(tf.constant(['Thank you for your help'])).numpy())                                                   # * Gratitude
# print(conv_model.serve(tf.constant(['I feel sadness tonight after hearing the bad news'])).numpy())                         # * Sandess
# print(conv_model.serve(tf.constant(['I’m ending the day with happiness in my heart'])).numpy())                             # * Joy


# # * Not evidence examples
# print("##############################################################")
# print("NON EVIDENCE EXAMPLES")
# print("ANGER        FEAR        HAPPY       SADNESS")
# print(conv_model.serve(tf.constant(['My feelings are hurt.'])).numpy())                                                         # * Sadness
# print(conv_model.serve(tf.constant(['I keep checking the locks even though I know I already closed everything.'])).numpy())     # * Fear
# print(conv_model.serve(tf.constant(['I can’t stop smiling after everything that happened today.'])).numpy())                    # * Joy        
# print(conv_model.serve(tf.constant(['I’m still thinking about that argument, and it really ruined my evening.'])).numpy())      # * Anger
# print(conv_model.serve(tf.constant(['Tonight, I realize how lucky I am to have such supportive people around me.'])).numpy())   # * Gratitude                                                # * Gratitude
# print(conv_model.serve(tf.constant(['I don’t really feel like talking to anyone tonight.'])).numpy())                           # * Sandess
# print(conv_model.serve(tf.constant(['I’m ending the day with a good feeling in my heart.'])).numpy())                           # * Joy