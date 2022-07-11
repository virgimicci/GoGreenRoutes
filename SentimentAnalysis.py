# Using VADER lexicon for SA with nltk
# VADER ( Valence Aware Dictionary for Sentiment Reasoning) is a model used for text sentiment analysis that is sensitive to both polarity (positive/negative) 
# and intensity (strength) of emotion. 
# It is available in the NLTK package and can be applied directly to unlabeled text data.


import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
SIA = SentimentIntensityAnalyzer()


df_green['text1'] = df_green['text1'].astype(str)

# Applying Model, Variable Creation
df_green['Polarity Score'] = df_green['text1'].apply(lambda x:SIA.polarity_scores(x)['compound'])
df_green['Neutral Score'] = df_green['text1'].apply(lambda x:SIA.polarity_scores(x)['neu'])
df_green['Negative Score'] = df_green['text1'].apply(lambda x:SIA.polarity_scores(x)['neg'])
df_green['Positive Score'] = df_green['text1'].apply(lambda x:SIA.polarity_scores(x)['pos'])

# Converting 0 to 1 Decimal Score to a Categorical Variable
df_green['Sentiment']=''
df_green.loc[df_green['Polarity Score'] >0,'Sentiment']='Positive'
df_green.loc[df_green['Polarity Score'] == 0,'Sentiment']='Neutral'
df_green.loc[df_green['Polarity Score'] <0,'Sentiment']='Negative'
df_green[:5]

df_green["Sentiment"].value_counts()
# Positive    626
# Neutral     386
# Negative     90
