import streamlit as st

import sqlite3
from streamlit_star_rating import st_star_rating
connection = sqlite3.connect('Modified SQL Database.db')
connection.isolation_level = None 
cursor = connection.cursor()

from streamlit.source_util import (
    page_icon_and_name, 
    calc_md5, 
    get_pages,
    _on_pages_changed
)  

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
        st_star_rating(label='', maxValue = 5, defaultValue = ratings[0][0], key = "rating", dark_theme = True , size=20, read_only = True)


st.title('''Welcome to SQL - Mellon City Mysteria!''')
    
st.markdown('''SQL - Mellon City Mysteria is the brainchild of two Carnegie Mellon University (CMU) graduate students with a passion for data and a shared love for mystery-solving adventures! 💻❤

Here's how this game came to life: In the pursuit of honing our SQL skills, we stumbled upon the SQL Murder Mystery: https://mystery.knightlab.com/, a self-directed lesson for mastering SQL commands and concepts. Captivated by the challenge, we envisioned taking this concept to the next level by making it accessible even to those unfamiliar with SQL Programming.

Recognizing a lack of one-player murder mystery games online, we embarked on this journey of blending our love for programming with the excitement of murder mystery. We took this as a challenge to seamlessly integrate two programming languages that we are familiar with - SQL and Python! In addition, we also explored using Streamlit, an open-source Python framework used to create interactive data apps, to bring our vision to reality.

Our commitment to innovation led us to modify the original SQL game and its database to suit our vision. This venture provided an opportunity for us to showcase not just our programming skills but also our artistic and creative talent. We have skillfully incorporated interactive elements such as secret codes and puzzles, with the aim of transforming the gameplay into a dynamic and engaging experience for our players.

We invite you to experience our game firsthand and share any thoughts, feedback, and suggestions you may have. As active members of the data community, we value collaboration and continuous learning.


Thank you for embarking on this SQL mystery adventure with us. We sincerely hope you enjoyed playing the game as much as we enjoyed creating it! 🕵️‍♂️🔍''')

connection.commit()
connection.close()