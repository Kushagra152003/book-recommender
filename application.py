import streamlit as st
import pandas as pd
import pickle 

book_name = pickle.load(open("c:/Users/Hp/Desktop/book-recommender/.venv/book_list.pkl",'rb'))
similarity = pickle.load(open("c:/Users/Hp/Desktop/book-recommender/.venv/similarity.pkl",'rb'))
book = pd.DataFrame(book_name)

def recommend(book_name):
    index = book[book['Title'] == book_name].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])

    recommendations=[]
    for i in distances[1:6]:
        recommendations.append(book.iloc[i[0]].Title)
    return recommendations



st.title("Book recommender system")

book_name_selector = st.selectbox(
    "Book name",
    book_name,
)

if st.button("Recommend", type="primary"):
    recommend=recommend(book_name_selector)
    for i in recommend:
        st.write(i)