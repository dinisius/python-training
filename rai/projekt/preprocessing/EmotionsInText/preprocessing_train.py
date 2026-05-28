import copy
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/EmotionsInText/Emotion_final.csv")
print(df.head())  

rows, columns = df.shape                                    # Get the size of original dataset

not_my_nn_emotions = []                               # Init empty list of indexes with multi emotion text

my_nn_emotions = ["anger", "fear", "happy", "sadness", ]                    # Try to find "fear" and "sandess" features 
                                                        # to add them to main dataset to achieve equal distribution between features 

# Get indexes of text, that is out of my emotions scope
for index in range(rows):                           
        
    # Type cast for detection index in my_nn_emotions
    if (df[df.columns[1]].loc[df.index[index]]) not in my_nn_emotions: 

        not_my_nn_emotions.append(index)                    # If index is out of my emotions scope add it to not_my_nn_emotions

df_cleared = df.drop(df.index[not_my_nn_emotions])      # Drop indexes of text with emotions that are out of scope at once. 

cleared_rows, cleared_columns = df_cleared.shape            # Get "cleared" dataset size and print it

emotions_frequency = df_cleared['Emotion'].value_counts()                     # Count frequency of each emotion text in preprocessed dataset

# Print frequency of emotions
print(emotions_frequency)                                   # * Happy:      7029
                                                            # * Sadness:    6265
                                                            # * Anger:      2993
                                                            # * Fear:       2652

# Downsampling process

happy = df_cleared[df_cleared['Emotion'] == "happy"]
sadness = df_cleared[df_cleared['Emotion'] == "sadness"]
anger = df_cleared[df_cleared['Emotion'] == "anger"]

happy_to_drop = math.floor((happy.shape[0]) * (3/5))
index_happy_to_drop = happy.sample(happy_to_drop).index
df_cleared = df_cleared.drop(index_happy_to_drop)

sadness_to_drop = math.floor((sadness.shape[0]) * (1 - (43/100))) 
index_sadness_to_drop = sadness.sample(sadness_to_drop).index
df_cleared = df_cleared.drop(index_sadness_to_drop)

anger_to_drop = math.floor((anger.shape[0]) * (1 - 9/10)) 
index_anger_to_drop = anger.sample(anger_to_drop).index
df_cleared = df_cleared.drop(index_anger_to_drop)

emotions_frequency = df_cleared['Emotion'].value_counts()                       # Count frequency of each emotion text in preprocessed dataset
print(emotions_frequency)                                                       # * Happy:      2812
                                                                                # * Sadness:    2694
                                                                                # * Anger:      2694
                                                                                # * Fear:       2652

happy = df_cleared[df_cleared['Emotion'] == "happy"]
sadness = df_cleared[df_cleared['Emotion'] == "sadness"]
anger = df_cleared[df_cleared['Emotion'] == "anger"]
fear = df_cleared[df_cleared['Emotion'] == "fear"]

happy_to_drop = ((happy.shape[0]) // 2)
index_happy_to_drop = happy.sample(happy_to_drop).index
happy_df_test_valid = happy.loc[index_happy_to_drop]
df_cleared = df_cleared.drop(index_happy_to_drop)

sadness_to_drop = ((sadness.shape[0]) // 2)
index_sadness_to_drop = sadness.sample(sadness_to_drop).index
sadness_df_test_valid = sadness.loc[index_sadness_to_drop]
df_cleared = df_cleared.drop(index_sadness_to_drop)

anger_to_drop = ((anger.shape[0]) // 2)
index_anger_to_drop = anger.sample(anger_to_drop).index
anger_df_test_valid = anger.loc[index_anger_to_drop]
df_cleared = df_cleared.drop(index_anger_to_drop)

fear_to_drop = ((fear.shape[0]) // 2)
index_fear_to_drop = fear.sample(fear_to_drop).index
fear_df_test_valid = fear.loc[index_fear_to_drop]
df_cleared = df_cleared.drop(index_fear_to_drop)

emotions_frequency = df_cleared['Emotion'].value_counts()                       # Count frequency of each emotion text in preprocessed dataset
print(emotions_frequency)                                                       # * Happy:      1406
                                                                                # * Sadness:    1347
                                                                                # * Anger:      1347
                                                                                # * Fear:       1326

# Spojení dataframe do jednoho velkého
df_test_valid = pd.concat(
    [happy_df_test_valid, sadness_df_test_valid, anger_df_test_valid, fear_df_test_valid],
    axis=0
)

# Zamíchání pořadí řádků
df_test_valid = df_test_valid.sample(frac=1)

# Reset indexů
df_cleared = df_cleared.reset_index(drop=True)
df_test_valid = df_test_valid.reset_index(drop=True)

print(df_test_valid.head())

df_cleared['Emotion'] = df_cleared['Emotion'].map({           
                                                    'anger':'0', 
                                                    'fear':'1', 
                                                    'happy':'2',  
                                                    'sadness':'3'
                                                    })

df_test_valid['Emotion'] = df_test_valid['Emotion'].map({           
                                                    'anger':'0', 
                                                    'fear':'1', 
                                                    'happy':'2',  
                                                    'sadness':'3'
                                                    })

df_cleared.to_csv('preprocessing/EmotionsInText/data_cleared_train.tsv', sep="\t")        # Save cleared dataset
df_test_valid.to_csv('preprocessing/EmotionsInText/data_cleared_test.tsv', sep="\t")        # Save cleared dataset

print(df_test_valid.head())