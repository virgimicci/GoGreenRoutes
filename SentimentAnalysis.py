
# Using Scikit-learn to built the model

# Trying standard sentiment analysis
# Let’s import all the packages used in building our model

from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split 
from sklearn.base import TransformerMixin
from sklearn.svm import LinearSVC 
from sklearn.pipeline import Pipeline 

# 1. CountVectorizer = transform the texts in our dataset into numeric values that are in vectors. 
# 2. TfidfVectorizer = is a statistical measure that evaluates how relevant a word is in a collection of documents.
#    If a word is common in a given document and common in other documents, it indicates that it has less power when making a prediction.
# 3. accuracy_score = This package is used to calculate the model’s accuracy when making a prediction.
# 4. train_test_split = This is used to split our dataset into a training set and testing set.
# 5. TransformerMixin = This is used to fit the model into the dataset during the training phase. It ensures that our model learns the patterns in the dataset.
# 6. LinearSVC = This is the support vector machine algorithm used in building the model. 
# 7. Pipeline = It automates functions such as CountVectorizer, TfidfVectorizer, TransformerMixin, and LinearSVC
#    This makes model building process faster and easier since all the stages are bundled together into one unit process.





