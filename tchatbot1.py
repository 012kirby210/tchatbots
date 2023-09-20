# FAQ TchatBot 
# feature extraction via text vectorization
# similarities analysis then take the max as the output
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq_dataframe = pd.read_csv('../assets/frequently_asked_questions.csv')
vectorizer = TfidfVectorizer()
vectorizer.fit(np.concatenate( (faq_dataframe.Question,
                                faq_dataframe.Answer)))
vectorized_questions = vectorizer.transform(faq_dataframe.Question)

NUMBER_OF_QUESTION = 5

for i in range(1,NUMBER_OF_QUESTION):
    print("--------------------------")
    print("What is is your question ?\n")
    user_question = input()
    print("\n")
    vectorized_user_question = vectorizer.transform([user_question])
    similarities = cosine_similarity(vectorized_user_question, vectorized_questions)
    closest_question = np.argmax(similarities, axis=1)
    answer = faq_dataframe.Answer.iloc[closest_question].values[0]
    print("{}\n".format(answer))
print("it was your last question, bye.")