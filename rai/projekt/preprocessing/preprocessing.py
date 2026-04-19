# ! 19.04.2026 8:17
# TODO: Divide each section in code for better readability. Example: Read data, prepocess data etc.

# * Found out, that "rough" preprocessing dataset is not correct attitude to this task \
# * My first idea of improvment is not to drop every row with multi emotional text, \
# * But check, weather one of its category relates to one of my emotion scope.

import copy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/data/train.tsv", sep="\t",        # Read dataset
                  names=["text", "index", "reddit_name"])

print(df.head())                                            # Print original dataset

df_cleared = df.drop(columns="reddit_name")                 # Drop reddit_name column and pass changed dataset to "cleared" copy 

rows, columns = df.shape                                    # Get the size of original dataset

print(df_cleared.head())                                    # Print "cleared" dataset

multivalue_index_list = []                                  # Init list of indexes with multi emotion text

my_nn_emotions = (2, 14, 15, 17, 25)                        # Init tupple with emotions(indexes) that will be used in my neural network. \
                                                            # * 2 = Anger, 14 = Fear, 15 = Gratitude, 17 = Joy, 25 = Sadness

not_my_nn_emotions = []                                     # Init empty list of indexes of text, that is out of my emotions scope

for index in range(rows):                                   #TODO: Try to implement enumerate() fashion loop here

    if len(df[df.columns[1]].loc[df.index[index]]) >= 3:    # Detect multi emotion text with the easiest way.  \
                                                            # Dataaset has only 28 emotion classes, each class \
                                                            # with 1 emotion has a number with maximum len = 2 \ 

        multivalue_index_list.append(index)                 # Add current index to the list.
        
        # print(df_cleared[df_cleared.columns[0]].loc[df_cleared.index[index]]) #Left it here because of .loc method

df_cleared = df.drop(index=multivalue_index_list)         
# df_cleared = df.drop(df.index[not_my_nn_emotions])          # Drop indexes with multi emotion at once. 
                                                            # ? Which way of dropping is correct? 

print("Raw rows:", rows, "Raw columns", columns)            # Print original dataset size \
                                                            # * 43410 rows and 3 columns

cleared_rows, cleared_columns = df_cleared.shape            # Get "cleared" dataset size

print("Cleared rows:", cleared_rows, "Cleared columns", cleared_columns)    # Print "cleared" dataset size \
                                                                            # * # * 36308 rows and 3 columns

for index in range(cleared_rows):                           # Get indexes of text, that is out of my emotions scope
        
    if (int)(df_cleared[df_cleared.columns[1]].loc[df_cleared.index[index]]) not in my_nn_emotions:

        not_my_nn_emotions.append(index)                    # Add index if index is out of my emotions scope

print("not_my_nn_emotions length: ", len(not_my_nn_emotions))   # Print how many text is out of my emotions scope \
                                                                # * not_my_nn_emotions length:  31326
                                                                
df_tmp = copy.deepcopy(df_cleared)                              # ? Copy df_cleared in df_tmp for more ensurance

df_cleared = df_tmp.drop(df_tmp.index[not_my_nn_emotions])      # Drop indexes of text with emotions that are out of scope at once. 

cleared_rows, cleared_columns = df_cleared.shape            # Get "cleared" dataset size
print("Cleared rows:", cleared_rows, "Cleared columns", cleared_columns)    # Print "cleared" dataset size  \
                                                                            # * 4982  rows and 3 columns

df_cleared['index'] = df_cleared['index'].astype('category')                # Perform this for easy bar plotting of pd.Series type
df_cleared['index'] = df_cleared['index'].cat.rename_categories({           # Rename indexes to appropiate emotions for better readability
                                                                '2':'Anger', 
                                                                '14':'Fear', 
                                                                '15':'Gratitude', 
                                                                '17':'Joy', 
                                                                '25':'Sadness'
                                                                })

emotions_frequency = df_cleared['index'].value_counts()                     # Count frequency of each emotion text in preprocessed dataset

print(emotions_frequency)                                   # Print frequency of emotions
                                                            # * Gratitude: 1857
                                                            # * Anger:     1025
                                                            # * Joy:        853
                                                            # * Sadness:    817
                                                            # * Fear:       430

emotions_frequency.plot(kind='bar')                         # Plot the bar graf
plt.title('Emotions frequency in preprocessed dataset')
plt.xlabel('Emotions')
plt.ylabel('Frequency')
plt.grid(True)                                                                            
plt.show()



