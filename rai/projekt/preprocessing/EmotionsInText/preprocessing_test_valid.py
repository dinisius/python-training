import math
import pandas as pd

# * Separate validation and test data
# * 0.6 for test, 0.4 for validation

df_valid = pd.read_csv("preprocessing/EmotionsInText/data_cleared_test.tsv", sep="\t")

df_valid = df_valid.drop(columns='Unnamed: 0')                        # Drop unusable first column

print(df_valid.head())

happy = df_valid[df_valid['Emotion'] == 2]
sadness = df_valid[df_valid['Emotion'] == 3]
anger = df_valid[df_valid['Emotion'] == 0]
fear = df_valid[df_valid['Emotion'] == 1]

happy_to_drop = math.floor((happy.shape[0]) * (0.6))
index_happy_to_drop = happy.sample(happy_to_drop).index
happy_df_test = happy.loc[index_happy_to_drop]
df_valid = df_valid.drop(index_happy_to_drop)

emotions_frequency = df_valid['Emotion'].value_counts()                     # Count frequency of each emotion text in preprocessed dataset
print(emotions_frequency)

sadness_to_drop = math.floor((sadness.shape[0]) * (0.6))
index_sadness_to_drop = sadness.sample(sadness_to_drop).index
sadness_df_test = sadness.loc[index_sadness_to_drop]
df_valid = df_valid.drop(index_sadness_to_drop)

emotions_frequency = df_valid['Emotion'].value_counts()                     # Count frequency of each emotion text in preprocessed dataset
print(emotions_frequency)

anger_to_drop = math.floor((anger.shape[0]) * (0.6))
index_anger_to_drop = anger.sample(anger_to_drop).index
anger_df_test = anger.loc[index_anger_to_drop]
df_valid = df_valid.drop(index_anger_to_drop)

emotions_frequency = df_valid['Emotion'].value_counts()                     # Count frequency of each emotion text in preprocessed dataset
print(emotions_frequency)

fear_to_drop = math.floor((fear.shape[0]) * (0.6))
index_fear_to_drop = fear.sample(fear_to_drop).index
fear_df_test = fear.loc[index_fear_to_drop]
df_valid = df_valid.drop(index_fear_to_drop)

emotions_frequency = df_valid['Emotion'].value_counts()                     # Count frequency of each emotion text in preprocessed dataset
print(emotions_frequency)

# Spojení dataframe do jednoho velkého
df_test = pd.concat(
    [happy_df_test, sadness_df_test, anger_df_test, fear_df_test],
    axis=0
)

# Zamíchání pořadí řádků
df_test = df_test.sample(frac=1)

# Reset indexů
df_test = df_test.reset_index(drop=True)
df_valid = df_valid.reset_index(drop=True)

df_test.to_csv('preprocessing/EmotionsInText/data_test.tsv', sep="\t")        # Save cleared dataset
df_valid.to_csv('preprocessing/EmotionsInText/data_valid.tsv', sep="\t")        # Save cleared dataset