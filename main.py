import streamlit as st
import datetime

st.write('Hello World') # Hello World print ho jaey ga

st.header('Tariq Khan') # Tariq Khan
# Title k liye
st.title('This is Streamlit Tutorial')

# st mark sown ka use 
st.markdown('# GIAIC Class-4, 14-03-2022')  # <h1>
st.markdown('## GIAIC Class-4, 14-03-2022') # <h2>

# Bold text by **  **, __  __
st.markdown('**Battery Terminal**') # Bold Text
st.markdown('*Python with streamlit*') # Italic text
# for color the text
st.markdown('<span style="color:blue">blue text</span>', unsafe_allow_html=True)
# Color and heading
st.markdown('<h1 style="color:red;">GIAIC class-4,  14-03-2025</h1>', unsafe_allow_html=True)

# for Caption 
st.caption('This is Caption tag')

st.code('age=30')

# INPUT FIELDS  Max_chars=20 ka matlab ye 20 se zada charac nae lay ga
st.text_input("Name", placeholder="Enter Your Name", max_chars=20)
st.text_input(label="Your DOB")

st.date_input(label="Your DOB", max_value=datetime.date.today())



# For Chatting
user_chat = st.chat_input("type...")
st.write("User typed:", user_chat)

# To Make the Text-area
st.text_area("Text here")

# Slider in the Streamlit
#st.slider("Your age:", min_value=11, max_value=92)

# one more method of Slider
age = st.slider("Your age:", min_value=11, max_value=92)
st.write("User age is :" , age)

# To Show the Gender with Radio Button
genders = ["Infant","kids","Man","Women"]
st.radio(label="Your Gender", options=genders)
st.checkbox(label="Active")

# Fruits 
fruits = ['Mango','Apple','Banana','Peach','Oranges','Grapes','Pineapples']
user_fruit = st.selectbox(label='Please select fruit', options=fruits)
st.write('user fruit :', user_fruit)

# Ab agar 2 ya zyada fruits select karnay k liye
user_fruit = st.multiselect(label='Please select fruit', options=fruits)
st.write('user fruit :', user_fruit)