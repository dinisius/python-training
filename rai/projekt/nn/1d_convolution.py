#TODO: WRITE COMMENTS TO EVERY CODE! 

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
NUMBER_OF_LAYERS = 5                                                                    

# Load the datasets
emotions_train = pd.read_csv("preprocessing/data_cleared_train.tsv", sep="\t")
emotions_test = pd.read_csv("preprocessing/data_cleared_test.tsv", sep="\t")            

# Preprocess datasets
emotions_features = emotions_train.copy()                                               # Copy train dataset to and then pop index column
emotions_lables = emotions_features.pop('index')                                        # That's how i obtain features and labels
emotions_features = emotions_features.drop(columns='Unnamed: 0')                        # Drop unusable first column


test_features = emotions_test.copy()                                                    # Copy test dataset to and then pop index column
test_features = test_features.drop(columns='Unnamed: 0')                                # That's how i obtain features and labels
test_lables = test_features.pop('index')                                                # Drop unusable first column

                                                    #######################
                                                    # * CREATE VOCABILARY #
                                                    #######################

# * Almost every step was copied from Tensor Flows "Load text" article: https://www.tensorflow.org/tutorials/load_data/text

# TODO: Change following 3 variables and follow their influence on the nn
batch_size = 32                                                                         
VOCAB_SIZE = 10000                                                                      # Set maximum size of vocaulary (of unique words)
MAX_SEQUENCE_LENGTH = 50                                                                # This parameter sets strict length of input tockens                  

# Standarize, tokenize and vectorize within TextVectorization layer. For 1D conv nn 'int' mode is used.
# * The default vectorization mode is 'int' (output_mode='int'). This outputs integer indices (one per token). \
# * This mode can be used to build models that take word order into account.
int_vectorize_layer = TextVectorization(
    max_tokens=VOCAB_SIZE,
    output_mode='int',
    output_sequence_length=MAX_SEQUENCE_LENGTH)

# Create vocabulary based on train dataset
int_vectorize_layer.adapt(emotions_features[emotions_features.columns[0]])              

                                                    #######################
                                                    # * "HAWKEYE" CONTROL #
                                                    #######################

# Show one sample of the vocabilary
print("Emotional text in human format", emotions_features[emotions_features.columns[0]].loc[emotions_features.index[0]])
print("Emotional label in human format", emotions_lables[0])
print("Emotional text in 'int' vectorized format", \
       int_vectorize_layer(emotions_features[emotions_features.columns[0]].loc[emotions_features.index[0]]).numpy())    # ? Looks like .numpy() is \
                                                                                                                        # ? mandatory in this case 

                                                    ########################
                                                    # * SET NEURAL NETWORK #
                                                    ########################

# * 1D Convolutional case (no freaking way, see the name of this source file)

# TODO Useful articles:
                        # * layers.Embedding: https://www.tensorflow.org/api_docs/python/tf/keras/layers/Embedding
                        # * Conv1D: https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv1D

def create_model(vocab_size, num_labels, vectorizer=None):
    my_layers =[]
    if vectorizer is not None:
        my_layers = [vectorizer]

    my_layers.extend([
        layers.Embedding(vocab_size, output_dim=16, mask_zero=True),                       # TODO: Play with output_dim=16 parameter to compare results               
        layers.Dropout(0.7),                                                                        # TODO: Play with Dropout parameter
        layers.Conv1D(filters=64, kernel_size=5, strides=2, padding="valid", activation="relu"),    # TODO: Play with all the parameters (PAT strides)
        layers.GlobalMaxPooling1D(),                                                        # TODO: return to this method for better understanding
        layers.Dense(num_labels)                                                            # Just my regular densely-connected NN layer.
    ])

    model = tf.keras.Sequential(my_layers)
    return model

# 'vocab_size' is 'VOCAB_SIZE + 1' since '0' is used additionally for padding.
int_model = create_model(vocab_size=VOCAB_SIZE + 1, num_labels=NUMBER_OF_LAYERS, vectorizer=int_vectorize_layer)

int_model.compile(
    loss=losses.SparseCategoricalCrossentropy(from_logits=True),                            # TODO: Find out, what is logit
    optimizer='adam',
    metrics=['accuracy'])

                                                    ######################
                                                    # * LEARNING PROCESS #
                                                    ######################

# 1. Vytvoření "hlídače", který zastaví trénink
early_stop = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=2, restore_best_weights=True)

# 2. Tvůj upravený příkaz fit (přidal jsem parametr "callbacks" nakonec)
int_history = int_model.fit(
    emotions_features[emotions_features.columns[0]].to_numpy(), 
    emotions_lables, 
    batch_size=batch_size, 
    epochs=50, # Teď můžeš s klidem nastavit hodně epoch
    validation_data=(test_features[test_features.columns[0]].to_numpy(), test_lables), 
    callbacks=[early_stop]
)

                                                    ######################
                                                    # * CONFUSION MATRIX #
                                                    ######################

# 1. Necháme model tipnout emoce pro všechna testovací data
# (Nezapomněli jsme na náš .to_numpy() trik)
raw_predictions = int_model.predict(test_features[test_features.columns[0]].to_numpy())

# 2. Model vrací tzv. logits (syrová čísla pro každou z 5 emocí). 
# Potřebujeme vybrat tu emoci, která dostala nejvyšší skóre.
predicted_labels = np.argmax(raw_predictions, axis=1)

# 3. Spočítáme matici záměn (porovnáme skutečnost s tipy modelu)
cm = confusion_matrix(test_lables, predicted_labels)

# 4. Vykreslení matice
# Tady si pak můžeš do display_labels dopsat reálné názvy svých emocí ve správném pořadí (0-4)
emotions_names = ['Emoce 0', 'Emoce 1', 'Emoce 2', 'Emoce 3', 'Emoce 4'] 

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=emotions_names)
disp.plot(cmap=plt.cm.Blues)

# Zvětšíme obrázek, ať je to hezky čitelné
fig = plt.gcf()
fig.set_size_inches(8, 8)
plt.title("Matice záměn (Confusion Matrix)")
plt.show()


# accuracy: 0.9113 - loss: 0.3019 - val_accuracy: 0.8687 - val_loss: 0.3816

# int_history = int_model.fit(emotions_features[emotions_features.columns[0]].to_numpy(), emotions_lables, batch_size=batch_size, epochs=10, validation_data=(test_features[test_features.columns[0]].to_numpy(), test_lables))