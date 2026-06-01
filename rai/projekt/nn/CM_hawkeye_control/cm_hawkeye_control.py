import pandas as pd
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import utils
from tensorflow.keras.layers import TextVectorization

                                                    ###################
                                                    # * READ DATASETS #
                                                    ###################                                                        

# Load the datasets
emotions_test = pd.read_csv("preprocessing/EmotionsInText/data_test.tsv", sep="\t")       

test_features = emotions_test.copy()                                                    # Copy test dataset to and then pop index column
test_lables = test_features.pop('Emotion')                                              # Drop unusable first column
test_features = test_features.drop(columns='Unnamed: 0')                                # Drop unusable first column


                                                    ######################
                                                    # * CONFUSION MATRIX #
                                                    ######################

int_model = tf.saved_model.load("1d_conv")

raw_predictions = int_model.serve(test_features[test_features.columns[0]].to_numpy())

# * Find maxarg indice in each row
predicted_labels = np.argmax(raw_predictions, axis=1)           

predicted_labels = pd.DataFrame(predicted_labels)

                                                    #########################
                                                    # * STORING PREDICTIONS #
                                                    # * WITH REAL SENTENCES #
                                                    #########################

stored_data = pd.concat([test_features, test_lables, predicted_labels], axis=1)
stored_data = stored_data.rename(columns={'Text':'Test text', 'Emotion':'Test emotions', 0:'Predicted emotions'})

stored_data['Test emotions'] = stored_data['Test emotions'].map({           
                                                    0:'anger', 
                                                    1:'fear', 
                                                    2:'happy',  
                                                    3:'sadness'
                                                    })

stored_data['Predicted emotions'] = stored_data['Predicted emotions'].map({           
                                                    0:'anger', 
                                                    1:'fear', 
                                                    2:'happy',  
                                                    3:'sadness'
                                                    })

print(stored_data.head())

stored_data.to_csv('nn/CM_hawkeye_control/hawkeye_control_data.csv', sep="\t")        # Save cleared dataset