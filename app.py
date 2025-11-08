import streamlit as st

# ---------------- IPL THEME SETUP ----------------
st.set_page_config(page_title="IPL Win Predictor", page_icon="🏏", layout="wide")

# Background + Style (No logic modified)
st.markdown("""
    <style>
    .main {
        background-image: url('https://wallpapers.com/images/featured/ipl-stadium-1l2b8f5tx1e6t7q0.jpg');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }
    h1, h2, h3 {
        color: #00FFFF;
        text-align: center;
        font-family: 'Arial Black';
        text-shadow: 1px 1px 3px #000;
    }
    .stSelectbox label, .stNumberInput label {
        color: #FFFFFF !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🏏 IPL Win Predictor</h1>", unsafe_allow_html=True)

# ---------------- YOUR ORIGINAL CODE (UNCHANGED) ----------------
import pickle
import pandas as pd

teams =['Mumbai Indians',
 'Kolkata Knight Riders',
 'Rajasthan Royals',
 'Chennai Super Kings',
 'Sunrisers Hyderabad',
 'Delhi Capitals',
 'Punjab Kings',
 'Lucknow Super Giants',
 'Gujarat Titans',
 'Royal Challengers Bengaluru']

cities =['Bangalore', 'Delhi', 'Mumbai', 'Kolkata', 'Hyderabad', 'Chennai',
       'Jaipur', 'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
       'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
       'Ahmedabad', 'Cuttack', 'Nagpur', 'Visakhapatnam', 'Pune',
       'Raipur', 'Ranchi', 'Abu Dhabi', 'Bengaluru', 'Sharjah',
       'Dubai', 'Navi Mumbai', 'Chandigarh', 'Lucknow', 'Guwahati',
       'Dharamsala', 'Mohali']
pipe = pickle.load(open('pipe.pkl','rb'))
st.title('IPL Win Predictor')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Overs completed')
with col5:
    wickets = st.number_input('Wickets out')

if st.button('Predict Probability'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team + "- " + str(round(win*100)) + "%")
    st.header(bowling_team + "- " + str(round(loss*100)) + "%")

# ---------------- TEAM LOGOS (ADDED AFTER ORIGINAL CODE) ----------------
team_logos = {
    'Mumbai Indians': 'https://upload.wikimedia.org/wikipedia/en/2/25/Mumbai_Indians_Logo.svg',
    'Kolkata Knight Riders': 'https://upload.wikimedia.org/wikipedia/en/4/4c/Kolkata_Knight_Riders_Logo.svg',
    'Rajasthan Royals': 'https://upload.wikimedia.org/wikipedia/en/6/60/Rajasthan_Royals_Logo.svg',
    'Chennai Super Kings': 'https://upload.wikimedia.org/wikipedia/en/2/2d/Chennai_Super_Kings_Logo.svg',
    'Sunrisers Hyderabad': 'https://upload.wikimedia.org/wikipedia/en/8/81/Sunrisers_Hyderabad.svg',
    'Delhi Capitals': 'https://upload.wikimedia.org/wikipedia/en/2/2f/Delhi_Capitals_Logo.svg',
    'Punjab Kings': 'https://upload.wikimedia.org/wikipedia/en/d/d4/Punjab_Kings_Logo.svg',
    'Lucknow Super Giants': 'https://upload.wikimedia.org/wikipedia/en/6/6e/Lucknow_Super_Giants_Logo.svg',
    'Gujarat Titans': 'https://upload.wikimedia.org/wikipedia/en/7/7e/Gujarat_Titans_Logo.svg',
    'Royal Challengers Bengaluru': 'https://upload.wikimedia.org/wikipedia/en/0/0a/Royal_Challengers_Bangalore_Logo.svg'
}

try:
    col1, col2 = st.columns(2)
    col1.image(team_logos[batting_team], width=150)
    col2.image(team_logos[bowling_team], width=150)
except:
    pass
