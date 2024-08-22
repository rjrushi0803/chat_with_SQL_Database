# chat_with_SQL_Database
this is the demo project where we are interacting with the SQL database with the help of prompt given to google Generative AI
# Workflow
1. we created the Dummy database **student.db** using python sqlite3 framework. database contains student names and their marks in respective subjects
2. for using the google Generative AI we need api key, in this case api key was stored in .env file
3. using streamlit we are creating the web app
   1. in the **input** section you should enter your querry as a prompt and press submit button
   2. the function **gemini_response** will take the prompt and generate SQL querry according to it with the help of google generative AI
   3. in app there is a function called **read_database** which is connected to the database **student.db**, it will take response created from **gemini_response** function and pass it to the SQL database
   4. using this SQL querry we will retrive data from database
4. we will get the answer for our input prompt.
