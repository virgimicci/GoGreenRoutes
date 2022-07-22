### Using VADER lexicon for SA with nltk ###
# VADER ( Valence Aware Dictionary for Sentiment Reasoning) is a model used for text sentiment analysis that is sensitive to both polarity (positive/negative) 
# and intensity (strength) of emotion. 
# It is available in the NLTK package and can be applied directly to unlabeled text data.

import plotly.io as pio
import plotly.express as px
pio.renderers.default='browser' # devo fare il render nel browser perchè in spyder non si aprono i plot
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

count = df_green["Sentiment"].value_counts()
# Positive    626
# Neutral     386
# Negative     90

VADERsent_df = pd.DataFrame.from_dict(count)
VADERsent_df = VADERsent_df.reset_index()
VADERsent_df = VADERsent_df.rename(columns={'index' : 'Sentiment value' , "Sentiment": 'Sentiment count'})
VADER_fig = px.bar(VADERsent_df, x='Sentiment count', y='Sentiment value', color = 'Sentiment value', orientation='h',
             width = 800, height = 400, color_discrete_sequence=px.colors.qualitative.Set3)
VADER_fig.show()

pol_score = px.line(df_green, x="text1", y="Polarity Score")
pol_score.show()

### NRC Word-Emotion Association Lexicon (aka EmoLex) ###
# The NRC Word-Emotion Association Lexicon (often shortened to NRC Emotion Lexicon, and originally called EmoLex) 
# is a list of English words and their manually annotated associations with eight basic emotions (anger, fear, anticipation, trust, surprise, sadness, joy, and disgust) 
# and two sentiments (negative and positive). Translations of the lexicon in other languages are available.

## LeXmo package
emo = df_green['text1'].apply(lambda x:LeXmo.LeXmo(x))

# NRC Word-Emotion Association Lexicon without package but importing the .txt file
filepath = "C:/Users/micci/Downloads/NRC-Suite-of-Sentiment-Emotion-Lexicons/NRC-Suite-of-Sentiment-Emotion-Lexicons/NRC-Sentiment-Emotion-Lexicons/NRC-Emotion-Lexicon-v0.92/NRC-Emotion-Lexicon-Wordlevel-v0.92.txt"
emolex_df = pd.read_csv(filepath,  names=["word", "emotion", "association"], skiprows=45, sep='\t')
emolex_df.head(12)

###### creation of a column where I convert the tweets in list of words # NON USATO
#df_green["token"] = [i.split() for i in df_green["text1"]]

## USING NRClex 
## Is based on the National Research Council Canada (NRC) affect lexicon 
# and the NLTK library's WordNet synonym sets

print(df_green['text1'].astype('string'))

# Since our data frame contains separate tweet strings, 
# we will join them to create a string object containing all of our tweets
str_tweet = ",".join(df_green["text1"])
text_object = NRCLex(str_tweet)

# Once we have our text object, we can efficiently utilise the library to extract 
# the raw emotion scores from our tweets.

data = text_object.raw_emotion_scores

# {'anticipation': 864, 'positive': 1429, 'trust': 735, 'negative': 401, 'anger': 191, 
# 'joy': 798, 'sadness': 221, 'surprise': 395, 'disgust': 99, 'fear': 192}

# Let’s convert these results into a data frame and plot them to visualise them more easily.
emotionNRClex_df = pd.DataFrame.from_dict(data, orient='index')

# creation of an index
emotionNRClex_df = emotionNRClex_df.reset_index()

# Changing the name of the columns 
emotionNRClex_df = emotionNRClex_df.rename(columns={'index' : 'Emotion Classification' , 0: 'Emotion Count'})

# Sorting vount values
emotionNRClex_df = emotionNRClex_df.sort_values(by=['Emotion Count'], ascending=False)

fig = px.bar(emotionNRClex_df, x='Emotion Count', y='Emotion Classification', color = 'Emotion Classification', orientation='h',
             width = 800, height = 400, color_discrete_sequence=px.colors.qualitative.Set3)
fig.show()

# Frequencies of each emotion within our tweets
text_object.affect_frequencies

# {'fear': 0.036056338028169016,
# 'anger': 0.03586854460093897,
# 'anticip': 0.0,
# 'trust': 0.13802816901408452,
# 'surprise': 0.07417840375586854,
# 'positive': 0.26835680751173707,
# 'negative': 0.07530516431924883,
# 'sadness': 0.041502347417840375,
# 'disgust': 0.018591549295774647,
# 'joy': 0.14985915492957746,
# 'anticipation': 0.16225352112676056}

# Let's create a df as before for the frequencies 

freqNRClex_df = pd.DataFrame.from_dict(text_object.affect_frequencies, orient='index')
freqNRClex_df = freqNRClex_df.reset_index()
freqNRClex_df = freqNRClex_df.rename(columns={'index' : 'Emotion Classification' , 0: 'Emotion Freq'})
freqNRClex_df = freqNRClex_df.sort_values(by=['Emotion Freq'], ascending=True)
fig2 = px.bar(freqNRClex_df, x='Emotion Freq', y='Emotion Classification', color = 'Emotion Freq', orientation='h',
             width = 800, height = 400, color_continuous_scale=px.colors.sequential.Viridis)
fig2.show()

