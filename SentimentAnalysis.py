
conda install -c conda-forge spacy
import spacy
!python -m spacy download en_core_web_sm
nlp = spacy.load('en_core_web_sm')
import re #library for regular expressions

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

### Text cleaning 

# Tokenization and remove punctuations
words = [str(token) for token in nlp(text) if not token.is_punct] 

# Expanding Contractions
# dictionary consisting of the contraction and the actual value
Apos_dict = {"'s":" is","n't":" not","'m":" am","'ll":" will",
           "'d":" would","'ve":" have","'re":" are"}
# replace the contractions
for key,value in Apos_dict.items():
    if key in words:
        words = words.replace(key,value)

# Remove digits and other symbols except "@"--used to remove email
words = [re.sub(r"[^A-Za-z@]", "", word) for word in words]

# Remove websites and email address
words = [re.sub(r"\S+com", "", word) for word in words]
words = [re.sub(r"\S+@\S+", "", word) for word in words]

# Remove hyperlinks
words = [re.sub(r'https?:\/\/.\S+', "", word) for word in words]

# Remove empty spaces 
words = [word for word in words if word !=' ']

# Remove old style retweet text "RT"
words = [re.sub(r'^RT[\s]+', '', word) for word in words]

# Split attached words
words = " ".join([s for s in re.split("([A-Z][a-z]+[^A-Z]*)",words) if s])

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
# to count the appearance of each word, it is essential to remove grammar tense and transform each word into its original form. 
# For example, if we want to calculate how many times the word ‘open’ appears in a news article,
# we need to count the appearances of ‘open’, ‘opens’, ‘opened’. Thus, lemmatization is an essential step for text transformation. 
# Another way of converting words to its original form is called stemming. Lemmatization is taking a word into its original lemma, 
# and stemming is taking the linguistic root of a word.

# .lemma_ function from spacy 

# Let's summarize the steps in a function and apply the function in all texts:

def text_preprocessing(str_input): 
     #tokenization, remove punctuation, lemmatization
     words = [token.lemma_ for token in nlp(str_input) if not token.is_punct]
 
     # remove symbols, websites, email addresses 
     words = [re.sub(r"[^A-Za-z@]", '', word) for word in words] 
     words = [re.sub(r'@[A-Za-z0-9]+','',word) for word in words]
     words = [re.sub(r"\S+com", '', word) for word in words]
     words = [re.sub(r"\S+@\S+", '', word) for word in words]
     words = [word for word in words if word!='']
     words = [word for word in words if len(word)!=0] 
 
     #remove stopwords     
     words=[word.lower() for word in words if word.lower() not in stopwords]
    
     #combine a list into one string   
     string = " ".join(words)
     return string
    

