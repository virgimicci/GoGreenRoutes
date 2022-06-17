
conda install -c conda-forge spacy
import spacy
!python -m spacy download en_core_web_sm
nlp = spacy.load('en_core_web_sm')
import re

### Tokenization
# The first step of preprocessing text data is to break every sentence into individual words, 
# which is called tokenization.

# Example for the first post
text = df_lim_nat.iloc[0]["text"]
# "Still time to see our stand at the Great Limerick Run Expo at 
# the UL arena, Limerick.It's open until 6PM. #Neartonature #UL #Limerick"

print([str(token) for token in nlp(text) if not token.is_punct]) # if not token.is_punct removed punctuations 

# ['Still', 'time', 'to', 'see', 'our', 'stand', 'at', 'the', 'Great', 'Limerick', 'Run', 
# 'Expo', 'at', 'the', 'UL', 'arena', 'Limerick', 'It', "'s", 'open', 'until', '6PM', 'Neartonature', 'UL', 'Limerick']


#tokenization and remove punctuations
words = [str(token) for token in nlp(text) if not token.is_punct] 

#remove digits and other symbols except "@"--used to remove email
words = [re.sub(r"[^A-Za-z@]", "", word) for word in words]

#remove websites and email address
words = [re.sub(r"\S+com", "", word) for word in words]
words = [re.sub(r"\S+@\S+", "", word) for word in words]

#remove empty spaces 
words = [word for word in words if word!=' ']

### Stopwords
# The next step is to remove the useless words, namely, the stopwords. Stopwords are words that frequently appear in many articles,
# but without significant meanings. Examples of stopwords are ‘I’, ‘the’, ‘a’, ‘of’.

# spacy stopwords
stopwords = nlp.Defaults.stop_words

print(len(stopwords)) # 326
print(stopwords)

# exclude the stopwords from the text
words = [word.lower() for word in words if word.lower() not in stopwords]

### Lemmatization
