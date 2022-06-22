
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
df_lim_nat['text1'] = [re.sub(r'^rt[\s]+', '', x) for x in df_lim_nat['text1']]

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

def space(tweet):
    doc = nlp(tweet)
    return " ".join([token.lemma_ for token in doc])
df_lim_nat['text1'] = df_lim_nat['text1'].apply(space)

## Check which are the most common words
# token dividen
token_ = [i.split() for i in df_lim_nat["text1"]]
# token joined in one list
tokens = [item for sublist in token_ for item in sublist]

# Print most common word
n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(tokens)
for word, count in word_counter.most_common(n_print):
    print(word, ": ", count)

# Create a data frame of the most common words 
# Draw a bar chart
lst = word_counter.most_common(n_print)
df_most_common = pd.DataFrame(lst, columns = ['Word', 'Count'])
df_most_common.plot.bar(x='Word',y='Count')

