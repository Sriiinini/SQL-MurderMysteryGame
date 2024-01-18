import streamlit as st
from streamlit_star_rating import st_star_rating
import sqlite3

connection = sqlite3.connect('Modified SQL Database.db')
connection.isolation_level = None 
cursor = connection.cursor()

cursor.execute('''
        SELECT COUNT(*)
        FROM Players 
''')

rows = cursor.fetchall()

cursor.execute('''
        SELECT AVG(rating)
        FROM Players
''')

ratings = cursor.fetchall()

cursor.execute('''
    SELECT COUNT(games_completed)
    FROM Games
''')

games = cursor.fetchall()

with st.sidebar:
    st.title('About SQL - Mellon City Mysteria')
    
    st.markdown('SQL - Mellon City Mysteria is an SQL based problem solver game developed by two Carnegie Mellon Graduate students.')
    st.text('')
    st.text('Developer: Srinidhi Manikantan')
    st.text('Developer: Heathvonn Styles')
    st.text('Developed: Nov 2023')

    st.divider()

    st.title('Game Statistics')

    if games:
        st.text(f'Total Games Played: {games[0][0]}')
    else:
        st.text('Total Games Played: 0')

    
    if rows:
        st.text(f'Total Feedback: {rows[0][0]} players')
    else:
        st.text('Total Feedback: 0 players')

    if ratings:
        st.text('Average Rating Received:')
        st_star_rating(label='', maxValue = 5, defaultValue = ratings[0][0], key = "rating3", dark_theme = True , size=20, read_only = True)

header = st.columns([0.8,1.5,0.5])
header[1].title('Feedback Form')

#col = st.columns([0, 18 ,0])
st.markdown('''Welcome to our Feedback Form! 

Thank you for being a part of our programming adventure. Your insights are highly 
valued, and we would be grateful if you could take a moment to share your thoughts 
with us. Your feedback will drive our continuous efforts to enhance and refine 
this experience.''')

with st.form("user_feedback"):
    

   # st.markdown('''Please enter your name:''')
    name = st.text_input('Please enter your name:')


    st.markdown(f'''<p style="font-size:14px;">On a scale of 1 to 5, how would you rate your overall experience with our game ?</p>''',unsafe_allow_html=True)
    stars = st_star_rating(label = "", maxValue = 5, defaultValue = 0, key = "rating", dark_theme = True , size=20)

    st.markdown(f'''<p style="font-size:14px;">On a scale of 1 to 5, how likely are you to recommend our game to your 
friends/family ?''',unsafe_allow_html=True)

    stars2 = st_star_rating(label = "", maxValue = 5, defaultValue = 0, key = "rating2", dark_theme = True , size=20)
    
    #st.markdown(f'''<p style="font-size:14px;">Were you satisfied with the overall experience? If so, we'd love to hear about 
#the specific elements or features that you particularly enjoyed ? ''',unsafe_allow_html=True)

    performance = st.text_area(label=" Were you satisfied with the overall experience? If so, we'd love to hear about the specific elements or features that you particularly enjoyed ?", value="", height=None, max_chars=None, key="text_area1")
    
    #st.markdown(f'''<p style="font-size:14px;">Do you have any suggestions for improvement or features you would like to see 
#in future updates ? ''',unsafe_allow_html=True)

    suggestion = st.text_area(label=" Do you have any suggestions for improvement or features you would like to see in future updates ?  ", value="", height=None, max_chars=None, key="text_area2")

    submit = st.form_submit_button('Submit')

    if submit:
        cursor.execute('''INSERT INTO Players VALUES (?,'','','',?,?,?,?)''', (name, stars,stars2,performance,suggestion))
        connection.commit()
        connection.close()
        st.success('Your feedback was successfully submitted!')
                                         
