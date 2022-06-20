
conda install -c conda-forge spacy
!python -m spacy download en_core_web_sm
import spacy
nlp = spacy.load('en_core_web_sm')
import re #library for regular expressions
import pandas as pd

# my df = df_lim_nat 2380

### Text cleaning 
# It's important to follow this order

# Creation of a new text column called text1 with the first pre-processing step: lower case
df_lim_nat['text1'] = df_lim_nat['text'].apply(lambda x: " ".join(x.lower() for x in x.split()))
df_lim_nat['text1'].head()

# Remove hyperlinks
df_lim_nat['text1'] = [re.sub(r'https?:\/\/.\S+', "", x) for x in df_lim_nat['text1']]

# Remove websites and email address
df_lim_nat['text1'] = [re.sub(r"\S+com", "", x) for x in df_lim_nat['text1']]
df_lim_nat['text1'] = [re.sub(r"\S+@\S+", "", x) for x in df_lim_nat['text1']]

# Remove old style retweet text "RT"
df_lim_nat['text1'] = [re.sub(r'^RT[\s]+', '', x) for x in df_lim_nat['text1']]

# Expanding Contractions
# dictionary consisting of the contraction and the actual value
apos_dict = {"'s":" is","n't":" not","'m":" am","'ll":" will",
           "'d":" would","'ve":" have","'re":" are"}
# replace the contractions
for key,value in apos_dict.items():
    if key in df['text1']:
        df_lim_nat['text1'] = df_lim_nat['text1'].replace(key,value)

# Split attached words
?????

# Remove punctuations (anche hashtag)
df_lim_nat['text1'] = df_lim_nat['text1'].str.replace('[^\w\s]','')
df_lim_nat['text1'].head()


### Stopwords
# The next step is to remove the useless words, namely, the stopwords. Stopwords are words that frequently appear in many articles,
# but without significant meanings. Examples of stopwords are ‘I’, ‘the’, ‘a’, ‘of’.
# spacy stopwords
stopwords = nlp.Defaults.stop_words
print(len(stopwords)) # 326
print(stopwords)

# exclude the stopwords from the text
df_lim_nat['text1'] = df_lim_nat['text1'].apply(lambda x: " ".join(x for x in x.split() if x not in stopwords))


### Lemmatization
# to count the appearance of each word, it is essential to remove grammar tense and transform each word into its original form. 
# For example, if we want to calculate how many times the word ‘open’ appears in a news article,
# we need to count the appearances of ‘open’, ‘opens’, ‘opened’. Thus, lemmatization is an essential step for text transformation. 
# Another way of converting words to its original form is called stemming. Lemmatization is taking a word into its original lemma, 
# and stemming is taking the linguistic root of a word.

# .lemma_ function from spacy 

def space(comment):
    doc = nlp(comment)
    return " ".join([token.lemma_ for token in doc])
df_lim_nat['text1'] = df_lim_nat['text1'].apply(space)



