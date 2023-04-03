import streamlit
import pandas
streamlit.title('My Parents new Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('Salad')
streamlit.text('Fruit Bowl')
streamlit.text('🥣 🥗 🐔 🥑🍞')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
