import pandas as pd
import tensorflow as tf

from tensorflow.keras import layers
from tensorflow.keras import losses
from tensorflow.keras import utils
from tensorflow.keras.layers import TextVectorization

emotions_train = pd.read_csv("preprocessing/data_cleared_train.tsv", sep="\t")          # Read dataset
emotions_test = pd.read_csv("preprocessing/data_cleared_test.tsv", sep="\t")          # Read dataset

emotions_features = emotions_train.copy()
emotions_features = emotions_features.drop(columns='Unnamed: 0')
emotions_lables = emotions_features.pop('index')

test_features = emotions_test.copy()
test_features = test_features.drop(columns='Unnamed: 0')
test_lables = test_features.pop('index')

batch_size = 32

VOCAB_SIZE = 10000
MAX_SEQUENCE_LENGTH = 50

int_vectorize_layer = TextVectorization(
    max_tokens=VOCAB_SIZE,
    output_mode='int',
    output_sequence_length=MAX_SEQUENCE_LENGTH)

int_vectorize_layer.adapt(emotions_features[emotions_features.columns[0]])

print("Emotional text in human format", emotions_features[emotions_features.columns[0]].loc[emotions_features.index[0]])

print("Emotional text in human format", emotions_lables[0])

print("Emotional text in 'int' vectorized format", int_vectorize_layer(emotions_features[emotions_features.columns[0]].loc[emotions_features.index[0]]).numpy())

def create_model(vocab_size, num_labels, vectorizer=None):
  my_layers =[]
  if vectorizer is not None:
    my_layers = [vectorizer]

  my_layers.extend([
      layers.Embedding(vocab_size, 64, mask_zero=True),
      layers.Dropout(0.5),
      layers.Conv1D(64, 5, padding="valid", activation="relu", strides=2),
      layers.GlobalMaxPooling1D(),
      layers.Dense(num_labels)
  ])

  model = tf.keras.Sequential(my_layers)
  return model

# `vocab_size` is `VOCAB_SIZE + 1` since `0` is used additionally for padding.
int_model = create_model(vocab_size=VOCAB_SIZE + 1, num_labels=5, vectorizer=int_vectorize_layer)

tf.keras.utils.plot_model(int_model, show_shapes=True)

int_model.compile(
    loss=losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer='adam',
    metrics=['accuracy'])
int_history = int_model.fit(emotions_features[emotions_features.columns[0]], emotions_lables, batch_size=batch_size, epochs=10, validation_data=(test_features[test_features.columns[0]], test_lables))