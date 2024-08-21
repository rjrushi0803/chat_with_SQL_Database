## creating the application

from dotenv import load_dotenv
load_dotenv() ## load all the environment variable

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

## configure the api key
genai.configure(api_key=os.getenv('google_api_key'))

## create a function to load google gemini model and get sql query as a response
def gemini_response(query, prompt):
    '''
    Here prompt means we are defining how our model should be working
    and query is our question to the model
    '''
    ## loading the gemini pro model
    model = genai.GenerativeModel('gemini-pro')
    full_prompt = f"{prompt}\nQuestion: {query}"
    response = model.generate_content(full_prompt)
    return response.text

## function to retrieve the information from the SQL query
def read_database(sql, db):
    ## first creating the connection with the database
    connect = sqlite3.connect(db)
    curr = connect.cursor()
    curr.execute(sql) ## this will execute the SQL query
    rows = curr.fetchall()
    connect.commit()
    connect.close()

    ## printing the rows
    for row in rows:
        print(row)

    return rows

## defining the prompt
prompt = """
You are an expert in converting English Questions to SQL queries! The SQL database has the name new_student and the following columns - name, class, section, and marks.

Example 1 - How many entries of the record are present? The SQL command will be like this: SELECT COUNT(*) FROM new_student;

Example 2 - Tell me all the students studying in the data science class? The SQL command will be like this: SELECT * FROM new_student WHERE class = 'data science';

The SQL code should not have ''' in the beginning or end, and do not include the word SQL in the output.
"""

########### making streamlit app ########################

st.set_page_config(page_title='I know How to Retrieve SQL Query')
st.header('Gemini PRO based app to retrieve SQL data')

question = st.text_input("Input", key='input')

submit = st.button('Ask Your Question')

## further process when submit button is clicked
if submit:
    ## we will get response from LLM
    response = gemini_response(question, prompt)
    print(response)
    ## we will get data from database using response
    data = read_database(response, 'student.db')
    ## now printing the data we got
    st.subheader('Response For Your Question Is')
    for row in data:
        print(row)
        st.header(row)
