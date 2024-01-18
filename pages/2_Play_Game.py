
import streamlit as st
import streamlit.components.v1 as components
import time
import hydralit as hy
import json
import requests
from streamlit_lottie import st_lottie
from streamlit.components.v1 import html
from streamlit_card import card
import pandas as pd 
import sqlite3
from PIL import Image
from streamlit_star_rating import st_star_rating

from streamlit.source_util import (
    page_icon_and_name, 
    calc_md5, 
    get_pages,
    _on_pages_changed
)

def edit_page_name(main_script_path_str, page_name):

    current_pages = get_pages(main_script_path_str)
  

    for key, value in current_pages.items():
        
        if value['page_name'] == "streamlit_app":
            value['page_name'] = "Mellon City Mysteria"

    _on_pages_changed.send()

#connection = sqlite3.connect('sql-murder-mystery copy.db')
connection = sqlite3.connect('Modified SQL Database.db')
connection.isolation_level = None 
cursor = connection.cursor()

container_style = """
    width:0px;
    height:0px;
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

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

if 'name' not in st.session_state:
    st.session_state.name = None

if 'loaded' not in st.session_state:
   st.cache_data.clear()
   st.session_state.loaded = True

@st.cache_data(show_spinner=False)
def typewriter(text: [str,str], speed: int):
    container = st.empty()
    for i in text:
        tokens = i.split()

        for index in range(len(tokens) + 1):
            curr_full_text = " ".join(tokens[:index])
            container.markdown(curr_full_text, unsafe_allow_html=True)
            time.sleep(0.1)

@st.cache_data(show_spinner=False)
def lottietypewriter(_text: [st_lottie], speed: int):

    container = st.empty()
    for i in _text:
        container.markdown(f"""<div style='{container_style}'>{i}</div>""",unsafe_allow_html=True)
        time.sleep(1)
        container.empty()


def typewriter2(text: [str, str], speed: int):
    st.markdown("""
    <div id="typewriter-container"></div>
    <script>
        const text = ["{}"];
        const speed = {};
        const container = document.getElementById('typewriter-container');
        
        async function typewriterEffect() {
            for (let i = 0; i < text.length; i++) {
                const tokens = text[i].split(' ');
                for (let j = 0; j <= tokens.length; j++) {
                    const currentText = tokens.slice(0, j).join(' ');
                    container.innerHTML = currentText;
                    await new Promise(resolve => setTimeout(resolve, 1000 / speed));
                }
                await new Promise(resolve => setTimeout(resolve, 1000));
            }
        }

        typewriterEffect();
    </script>
    """.format('", "'.join(text), speed))
#container = st.empty()



col1,col2,col3 = st.columns([1,8,1])

with col1 :
    pass
with col2 :
    #st.markdown(f"""<div style="width: 50%; height: 50%;">{st_lottie(lottie_coding,key="lottie1")}</div>""",unsafe_allow_html=True)
    #st.image('detective-case.jpeg')
    pass
with col3 :
    pass  



col1,col2 = st.columns([1,8])

with col1 :
    st.image('detective-profile.png')
with col2 :
    typ = typewriter(['''Hello and welcome! To kick off our mystery adventure, please enter your name below to begin.'''],3)
    

player_name = st.text_input('Player Name:').capitalize()


if 'click' not in st.session_state:
    st.session_state.click = False

def on_button_click():
    st.session_state.click = True


if 'click2' not in st.session_state:
    st.session_state.click2 = False

def on_button_click2():
    st.session_state.click2 = not st.session_state.click2


if 'start_time' not in st.session_state:
    st.session_state.start_time = 0

if 'end_time' not in st.session_state:
    st.session_state.end_time = 0


def time_difference(start_time, end_time):
    # Calculate the time difference in seconds
    time_diff_seconds = end_time - start_time

    # Extract hours, minutes, and seconds from the time difference
    hours, remainder = divmod(time_diff_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return f'''{int(hours)}: {int(minutes)}: {float(seconds)}'''

#click = False


#def clicked():
    #global click
    #click = True

#delete_page('HeathVn/streamlit-example/pages/','Feedback')

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
    
     
total_time = 0

if player_name:
    #st.session_state.start_time = time.time()
    #if 'name' in st.session_state:
       # st.session_state.name = player_name

    #st.experimental_set_query_params(name=player_name)

    

    
    col1,col2 = st.columns([1,8])

    with col1 :
        st.image('detective-profile.png')
    with col2 :
       st.write(f'''Welcome aboard, Detective {player_name}!''')
       container2 = st.empty()
       typewriter(['''We find ourselves at a critical juncture in Mellon City—a murder on January 15, 2018. The entire city is counting on your super-sleuth skills to crack the case. Before we dive into the nitty-gritty, let's snag the lowdown on the crime scene. Head on over to the police department's database and grab those crime scene reports. The city's counting on you! Good luck!'''],3)

    cursor.execute('''
        SELECT * 
        FROM crime_scene_report
        WHERE type = 'murder' 
        AND city = 'Mellon City' 
    ''')

    rows = cursor.fetchall()

    column_names = [description[0].capitalize() for description in cursor.description]


    if rows and column_names:
        df = pd.DataFrame(data=rows, columns=column_names)
        st.table(df)
        
        col1,col2 = st.columns([1,8])

        with col1 :
            st.image('detective-profile.png')
        with col2 :
            container3 = st.empty()
            typewriter([f'''Well, Detective {player_name}, you've absorbed the details. When you're ready to plunge into the investigation, hit that button and let's unravel this mystery together! '''], 3)
        
        col1,col2 = st.columns([6,1])

        with col1:
            finished = st.button("""Done Reading""", on_click = on_button_click )
        with col2 :
            pass 
    else:
        st.warning('No results found.')

    #st.write(st.session_state.click)

    if st.session_state.click:
        
        lottie_coding = load_lottiefile("running.json")
        lottie_coding1 = load_lottiefile("detective.json")
        col1,col2,col3 = st.columns([1,0.6,1])

        with col1 :
            pass
        with col2 :
            st_lottie(lottie_coding,key="lottie1")
            #st_lottie(lottie_coding,key=f"lottie1")
            
        with col3:
            pass

        

        col1,col2 = st.columns([1,8])

        with col1 :
            st.image('detective-profile.png')
        with col2 :
            typewriter([f'''Uh-oh! Detective {player_name}, we've hit a snag. An elusive culprit has meddled with the crime scene reports, leaving us with a puzzle to solve. The city's faith in your investigative skills has never been more crucial. Decode wisely!'''],3)
        
        col1,col2 = st.columns([1,8])

        with col1 :
            st.image('detective-profile.png')
        with col2 :
            typewriter(['''Now, onto the task at hand. Your first mission is to unravel the secret code and expose the address of Witness 1. Utilize the encryption provided below to crack the mystery code. Are you up for the challenge, Detective? The city awaits your sleuthing expertise.'''],3)

        image = Image.open('secretcode_sqlmystery.png')

        st.image(image) 
        
        user_guess = st.text_input('''Enter the secret code that you have found in the image above: ''')

        if user_guess:
            user_guess = user_guess.strip()

            cursor.execute('''
                SELECT * 
                FROM person
                WHERE LOWER(address_street_name) = ?
                ORDER BY name DESC
            ''', (user_guess.lower(),))  # Using a placeholder and passing the variable as a parameter

        
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            if rows:
                df = pd.DataFrame(data=rows, columns=column_names)
                st.table(df)

                col1,col2 = st.columns([1,8])

                with col1 :
                    st.image('detective-profile.png')
                with col2 :
                    typewriter(['''Based on the clues found in the crime scene report, can you deduce the identity of Witness 1? Kindly enter the name below.'''],3)

                user_W1name = st.text_input('''Who is Witness 1? Write the name here:''')
                user_W1name = user_W1name.strip()

                if user_W1name.lower() in ['morty schapiro', 'morty', 'schapiro']:

                    col1,col2 = st.columns([1,8])

                    with col1 :
                        st.image('detective-profile.png')
                    with col2 :
                        typewriter(['''Excellent work, Detective! Morty Shapiro is indeed Witness 1.'''],3)

                    cursor.execute('''
                        SELECT * 
                        FROM person
                        WHERE LOWER(address_street_name) = 'northwestern dr' 
                        ORDER BY address_number DESC
                        LIMIT 1
                    ''')

                    rows = cursor.fetchall()

                    column_names = [description[0] for description in cursor.description]

                    if rows:
                        df = pd.DataFrame(data=rows, columns=column_names)
                        st.table(df)
                    
                    

                    col1,col2 = st.columns([1,8])

                    with col1 :
                        st.image('detective-profile.png')
                    with col2 :
                        typewriter(['''Now, onto the next challenge. It seems the culprit has tampered with the identification of Witness 2. Three letters crucial to the witness's name are concealed behind the image. Can you unveil these hidden letters and reveal the identity of Witness 2? Your keen observation skills are key to solving this puzzle. Good luck!'''],3)

                    image = Image.open('spooky-house2.png')

                    st.image(image, caption='Crime Scene',width=700)

                    user_W2name = st.text_input("What letters do you see in the image? Type it here, so we can find the identity of Witness 2!")
                    user_W2name = user_W2name.strip()

                    if user_W2name.lower() in ['ann', 'nna']:
                        
                        col1,col2 = st.columns([1,8])

                        with col1 :
                            st.image('detective-profile.png')
                        with col2 :
                            typewriter(['''Fantastic job, Detective! Your sharp eyes have unveiled the hidden letters, pointing us to Annabel Miller as Witness 2. Good going!'''],3)
                    
                        cursor.execute('''
                            SELECT * 
                            FROM person
                            WHERE address_street_name = 'Franklin Ave'
                            AND LOWER(name) LIKE ?
                        ''', ('%' + user_W2name.lower() + '%',))

                        rows = cursor.fetchall()
                        column_names = [description[0] for description in cursor.description]

                        if rows:
                            df = pd.DataFrame(data=rows, columns=column_names)
                            st.table(df)

                        col1,col2 = st.columns([1,8])

                        with col1 :
                            st.image('detective-profile.png')
                        with col2 :
                            typewriter(['''Building on your exceptional work, we have now gathered details from the witnesses, obtaining intriguing statements about the suspect. To proceed further, kindly input the ID numbers of both witnesses below to unlock access to their statements. We're on the verge of cracking this case wide open, Detective! '''],3)
                        
                        user_W1id = st.text_input("What is the ID number of Witness 1?")
                        user_W1id = user_W1id.strip()

                        user_W2id = st.text_input("What is the ID number of Witness 2?")
                        user_W2id = user_W2id.strip()
                        
                        
                        

                        if user_W1id and user_W2id:


                            cursor.execute('''
                                SELECT *
                                FROM interview
                                WHERE person_id IN (?, ?)
                            ''', (user_W1id, user_W2id))

                            rows = cursor.fetchall()
                            column_names = [description[0] for description in cursor.description]

                            if rows:
                                df = pd.DataFrame(data=rows, columns=column_names)
                                st.table(df)

                                col1,col2 = st.columns([1,8])

                                with col1 :
                                    st.image('detective-profile.png')
                                with col2 :
                                    typewriter(['''Witness 2 has submitted a photo to the case file. To view the image, please click the button below.'''],3)

                                #typewriter(text=["<h3 style='text-align:center;'>Witness 2 submitted a photo to the case file</h3>","<h3 style='text-align:center;'>Access the photo by clicking the button below.</h3>"], speed=3)
                                
                                #st.write('Access the photo by clicking the button below.')

                                #add button
                                col1,col2 = st.columns([6,1])

                                with col1:
                                    finished = st.button("""View Photo""", on_click = on_button_click2 )
                                with col2 :
                                    pass 

                                #add picture
                                if st.session_state.click2:
                                    image = Image.open('red-tesla-car.png')

                                    st.image(image, caption='Car photo submitted to case file')

                                    col1,col2 = st.columns([1,8])

                                    with col1 :
                                        st.image('detective-profile.png')
                                    with col2 :
                                        typewriter(['''Buckle up, Detective! I've got the lowdown on our suspects and all the details we've squeezed out of them. Now, armed with the witness reports, can you channel your inner detective and make a wild guess at who the murderer might be? Let the suspense unfold, Detective!'''],3)

                                    cursor.execute('''
                                        SELECT p.name, dl.*, gym.membership_start_date, gym.membership_status
                                        FROM drivers_license dl
                                        INNER JOIN person p ON dl.id = p.license_id 
                                        INNER JOIN get_fit_now_member as gym
                                        ON p.id = gym.person_id 
                                        ORDER BY dl.id DESC
                                        LIMIT 20 
                                    ''')

                                    rows = cursor.fetchall()
                                    column_names = [description[0] for description in cursor.description]

                                    if rows:
                                        df = pd.DataFrame(data=rows, columns=column_names)
                                        st.table(df)

                                    user_murderer = st.text_input('Who are you accusing of murder?')
                                    user_murderer = user_murderer.strip()

                                    if user_murderer.lower() in ['jeremy', 'jeremy bowers', 'bowers', 'jeremybowers']:
                                        
                                        col1,col2 = st.columns([1,8])

                                        with col1 :
                                            st.image('detective-profile.png')
                                        with col2 :
                                            typewriter([f'''Incredible detective work! {user_murderer.capitalize()} is indeed the murderer. Mellon City extends its deepest gratitude; this case wouldn't have been cracked without your skillful unraveling.'''],3)
                                            
                                        cursor.execute('''
                                            SELECT p.name, dl.*, gym.membership_start_date, gym.membership_status
                                            FROM drivers_license dl
                                            INNER JOIN person p 
                                            ON dl.id = p.license_id 
                                            INNER JOIN get_fit_now_member as gym
                                            ON p.id = gym.person_id
                                            INNER JOIN get_fit_now_check_in as checkin
                                            ON gym.id = checkin.membership_id
                                            WHERE plate_number LIKE '%H42W%' 
                                            AND membership_status = 'gold'
                                            AND check_in_date = '20180109' 
                                        ''')

                                        rows = cursor.fetchall()
                                        
                                        column_names = [description[0] for description in cursor.description]

                                        if rows:
                                            df = pd.DataFrame(data=rows, columns=column_names)
                                            st.table(df)

                                            
                                            time.sleep(1)
                                            st.balloons()
                                            
                                            

                                            col1,col2,col3,col4 = st.columns([2,2,2,2])

                                            with col1:
                                                
                                                conclude = st.markdown(f""" <a target='_self' href='https://detectivegame.streamlit.app/Feedback'><button style='{button_style}'>Finish Game</button> </a>""", unsafe_allow_html=True)
                                                #conclude = st.button("""Finish Game""", on_click = on_button_click )  
                                                
 
                                                if conclude:
                                                    if games:
                                                        total_games = games[0][0] + 1
                                                        cursor.execute('''INSERT INTO Games VALUES (?)''', (total_games,))
                                                    else:
                                                        cursor.execute('''INSERT INTO Games VALUES (?)''', (1))

                                                    connection.commit()
                                                    connection.close()

                                            with col2 :
                                                pass
                                            with col3:
                                                pass
                                                #continue_game = st.button("""Continue""", on_click = on_button_click )
                                            with col4:
                                                pass
                                        else:
                                            st.warning(f'Oh no! Your guess does not seem to be right. {user_murderer.capitalize()} is not the murderer. Please try again!') 

            
            
            
                                

                            else:
                                st.warning('Oh no, that does not seem correct. Please try again! Are you sure you got the codes right?')

                        else:
                            st.warning('Make sure that the ids for both Witness 1 and Witness 2 are entered')

                    elif user_W2name.lower() == 'nan':
                        st.warning('No results found. Try again! Maybe you can try switching the order?')
                            
                    elif user_W2name.lower() not in ['morty schapiro', 'morty', 'schapiro'] and user_W2name != "":
                        st.warning("Oh no! That seems to be incorrect. Please try again! Make sure there are no spaces between each letter, and you are looking for the right clue!")
                
                elif user_W1name.lower() not in ['morty schapiro', 'morty', 'schapiro'] and user_W1name != "":
                                st.warning('Oh no! That seems to be incorrect. Please try again! Make sure there are no spelling mistakes, and you are looking for the right clue!')
            else:
                st.warning('No results found. Try again!')



