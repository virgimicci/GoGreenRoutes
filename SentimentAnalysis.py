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

import plotly.express as px

fig_pie = px.pie(df_green, names='Sentiment', title='Tweets Classifictaion', height=250,
                 hole=0.7, color_discrete_sequence=px.colors.qualitative.T10)
fig_pie.update_traces(textfont=dict(color='#fff'))
fig_pie.update_layout(margin=dict(t=80, b=30, l=70, r=40),
                      plot_bgcolor='#2d3035', paper_bgcolor='#2d3035',
                      title_font=dict(size=25, color='#a5a7ab', family="Lato, sans-serif"),
                      font=dict(color='#8a8d93'),
                      legend=dict(orientation="h", yanchor="bottom", y=1, xanchor="right", x=0.8)
                      )



# NRC Word-Emotion Association Lexicon (aka EmoLex) 
# The NRC Word-Emotion Association Lexicon (often shortened to NRC Emotion Lexicon, and originally called EmoLex) 
# is a list of English words and their manually annotated associations with eight basic emotions (anger, fear, anticipation, trust, surprise, sadness, joy, and disgust) 
# and two sentiments (negative and positive). Translations of the lexicon in other languages are available.

# LeXmo package
emo = df_green['text1'].apply(lambda x:LeXmo.LeXmo(x))

