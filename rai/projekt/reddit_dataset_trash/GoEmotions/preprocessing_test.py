import copy
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/GoEmotions/data/test.tsv", sep="\t",        # Read dataset
                  names=["text", "index", "reddit_name"])

print(df.head())                                            # Print original dataset

rows, columns = df.shape                                    # Get the size of original dataset

multi_emotion_index_list = []                               # Init empty list of indexes with multi emotion text

# Init tupple with emotions(indexes) that will be used in my neural network
my_nn_emotions = (2, 14, 15, 17, 25)                        # * 2 = Anger, 14 = Fear, 15 = Gratitude, 17 = Joy, 25 = Sadness                        

not_my_nn_emotions = []                                     # Init empty list of indexes of emotions, that is out of my scope

for index in range(rows):                                   #TODO: Try to implement enumerate() fashion loop here

    stop = False                                            # Support variable for braking for loop

    # Detects multi emotion text
    if len(df[df.columns[1]].loc[df.index[index]]) >= 3:    # Dataset has only 28 emotion classes. Max length of 1-emotion text = 2 

            # Copy value of the particular cell to tmp variable
            tmp = df[df.columns[1]].loc[df.index[index]]    # Cell contains values like '8,20', its type is str                                                            

            for multy in tmp.split(','):                    # Iterate "subvalues"(emotions) of splitted with comma tmp value  
                 
                # If at least one "subvalue" is in my emotion scope, rewrite value with current "subvalue" and break the for loop.
                # * So, I rewrite whole multi emotion value with the first detected "in my scope" emotion.
                # * E.g., if original value was '2,14,25', cell would be rewritten with '2'.
                if int(multy) in my_nn_emotions:            # Type cast for detection multy in my_nn_emotions
                    stop = True  
                    df.replace(df[df.columns[1]].loc[df.index[index]], multy, inplace = True)
                    break
                
                if stop == True:
                    continue

            multi_emotion_index_list.append(index)          # Otherwise, add current index to the list.

df_cleared = df.drop(index=multi_emotion_index_list)        # Drop rows with multi emotion vaules without my scope emotions 
df_cleared = df_cleared.drop(columns="reddit_name")         # Drop reddit_name column due to unusability
print(df_cleared.head())                                    # Print "cleared" dataset


                                #####################################################
                                # * NOW TEXTS OF DATASET HAVE ONLY 1 ASSIGNED VALUE #
                                #####################################################


# df_cleared = df.drop(df.index[not_my_nn_emotions])        # Drop indexes with multi emotion at once. 
                                                            # ? Which way of dropping is correct? 

# Print original dataset size
print("Raw rows:", rows, "Raw columns", columns)            # * 5427 rows, 3 columns
                                                             
cleared_rows, cleared_columns = df_cleared.shape            # Get "cleared" dataset size and print it
print("Cleared rows:", cleared_rows, "Cleared columns", cleared_columns)    # * 4868 rows, 2 columns 

# Get indexes of text, that is out of my emotions scope
for index in range(cleared_rows):                           
        
    # Type cast for detection index in my_nn_emotions
    if (int)(df_cleared[df_cleared.columns[1]].loc[df_cleared.index[index]]) not in my_nn_emotions: 

        not_my_nn_emotions.append(index)                    # If index is out of my emotions scope add it to not_my_nn_emotions

# Print how many text is out of my emotions scope
print("not_my_nn_emotions length: ", len(not_my_nn_emotions))   # * not_my_nn_emotions length:  3939 
                                                                
df_tmp = copy.deepcopy(df_cleared)                              # ? Copy df_cleared in df_tmp for more ensurance

df_cleared = df_tmp.drop(df_tmp.index[not_my_nn_emotions])      # Drop indexes of text with emotions that are out of scope at once. 

cleared_rows, cleared_columns = df_cleared.shape            # Get "cleared" dataset size and print it
print("Cleared rows:", cleared_rows, "Cleared columns", cleared_columns)    # * 929  rows and 2 columns

df_cleared['index'] = df_cleared['index'].astype('category')                # ? Perform this for easy bar plotting of pd.Series type

df_cleared['index'] = df_cleared['index'].cat.rename_categories({           # Rename indexes to appropiate emotions for better readability
                                                                '2':'Anger', 
                                                                '14':'Fear', 
                                                                '15':'Gratitude', 
                                                                '17':'Joy', 
                                                                '25':'Sadness'
                                                                })

emotions_frequency = df_cleared['index'].value_counts()                     # Count frequency of each emotion text in preprocessed dataset

# Print frequency of emotions
print(emotions_frequency)                                   # * Gratitude: 350
                                                            # * Anger:     198
                                                            # * Joy:       153
                                                            # * Sadness:   150
                                                            # * Fear:       78

# Plot the bar graf
emotions_frequency.plot(kind='bar')                         
plt.title('Emotions frequency in preprocessed dataset')
plt.xlabel('Emotions')
plt.ylabel('Frequency')
plt.grid(True)                                                                            
plt.show()

# Rename indexes with their original name due to Tensor Flow requirements
df_cleared['index'] = df_cleared['index'].cat.rename_categories({           
                                                                'Anger':'0', 
                                                                'Fear':'1', 
                                                                'Gratitude':'2', 
                                                                'Joy':'3', 
                                                                'Sadness':'4'
                                                                })

print(emotions_frequency)                                   # Print emotions frequency values

df_cleared.to_csv('data_cleared_test.tsv', sep="\t")        # Save cleared dataset