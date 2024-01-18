
import streamlit as st
import streamlit.components.v1 as components
import time
import hydralit as hy
import json
import requests
from streamlit_lottie import st_lottie
from streamlit.components.v1 import html
from streamlit_card import card

from streamlit.source_util import (
    page_icon_and_name, 
    calc_md5, 
    get_pages,
    _on_pages_changed
)


import sqlite3
from streamlit_star_rating import st_star_rating
connection = sqlite3.connect('Modified SQL Database.db')
connection.isolation_level = None 
cursor = connection.cursor()

# Replace 'lottie_url' with the actual URL of your Lottie JSON animation
lottie_url = "https://lottie.host/embed/2e9086c6-9faf-451a-9880-af787469a8b1/F9hsq1ytrf.json"

container_style = """
    width:100px;
    height:100px;
    position:relative;
    margin-left:auto;
    margin-right:auto;
"""

button_style = """
    background-color: transparent; 
    border: 2px solid white;
    border-radius: 15px;
    color: white;
    padding-left: 10px;
    padding-right:10px;
    text-decoration: none;
    font-size: 16px;
"""

spacing_style = """
    width:100px;
    height:800px;
    position:relative;
    
"""

def typewriter(text: [str,str], speed: int):
    
    container = st.empty()
    for i in text:
        tokens = i.split()
        
        

        for index in range(len(tokens) + 1):
            curr_full_text = " ".join(tokens[:index])
            container.markdown(curr_full_text, unsafe_allow_html=True)
            time.sleep(1/speed)

    


   

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def edit_page_name(main_script_path_str):

    current_pages = get_pages(main_script_path_str)
  

    for key, value in current_pages.items():
        
        if value['page_name'] == "streamlit_app":
            value['page_name'] = "Mellon City Mysteria"

    _on_pages_changed.send()

    

lottie_coding = load_lottiefile("detective.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://lottie.host/7867624f-734c-48fd-8407-94a8f54fbb63/cEi3XEcPWT.json")


edit_page_name('HeathVn/streamlit-example/pages/')


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


col1, col2, col3 = st.columns([1,6,1])

with col1:
    pass
with col2:
    st.markdown('# SQL - Mellon City Mysteria')
with col3 :
    pass

st.markdown(f"""<div style='{container_style}'>{st_lottie(lottie_coding,key="lottie1")}</div>""",unsafe_allow_html=True)
    
#st_lottie(lottie_coding, width=500, height=500)
typewriter(text=["<h2 style='text-align:center;'>Hello! Welcome to Murder Mystery Detectives!</h1>","<h2 style='text-align:center;'>Your journey begins here</h1>","<h2 style='text-align:center;'>Press the button below to start your game</h1>"], speed=2.5)


col1, col2, col3,col4,col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col3 :
    st.markdown(f""" <a target='_self' href='https://detectivegame.streamlit.app/Play_Game'><button style='{button_style}'>Start Game</button> </a>""", unsafe_allow_html=True)
with col4 :
    pass
with col5 :
    pass

# Use st.markdown to display the HTML content
#st.markdown(f"""<div style='{button_style}'>{st.button(label="Start Game",key="button1")}</div>""", unsafe_allow_html=True)
 
#st.markdown("<div style='height: 50px;margin-top:110px; position:relative;'></div>", unsafe_allow_html=True)

#st.write("Hello! Welcome to Murder Mystery Detectives! ")

connection.commit()
connection.close()

#




