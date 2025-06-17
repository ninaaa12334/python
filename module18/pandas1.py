import streamlit as st
import pandas as pd

df = pd.dataframe({
    'Name':["Alice", "John", "Josh"]
    'Age': [24,27,22]
    'City':["New York", "Berlin", "Prishtine"]

})


import streamlit as st
import pandas as pd


book_df = pd.read_csv('book.csv')
st.title('Best Selling Books')
st.write('This app analyzes the Amazon Top selling books from 2009-2022')

st.subheader("Summary statistics")

total_books = books_df.shape[0]
unique_titles = books_df['Name'].unique()
average_rating= books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total books", total_books)
col1.metric("unique_titles", unique_titles)
col1.metric("average_rating", average_rating)
col1.metric("average_price", average_price)