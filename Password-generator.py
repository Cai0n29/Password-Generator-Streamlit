import streamlit as st 
import random

Questions = st.selectbox(
  "Do you want to create a password?",
  ("YES", "NO"),
  index= None,
  placeholder = "Select Decisions"
)
none = ''
if Questions == "YES":
  numop = st.selectbox(
    "How many characters do you want with your password?",
    (1, 2, 3, 4, 5, 6, 7, 8, 9, 10),
    index=None,
    placeholder = 'Select up to 10',
  )
  numbers = numop
  password = ''
  
  if numbers == None:
    st.write('✨PICK A NUMBER FIRST!✨')
  else:
    allal = 'ABCDEFGHIJKLMNOPQRSTUVWKYZabcdefghijklmnopqrstuvwxyz'
    allsp = 'ABCDEFGHIJKLMNOPQRSTUVWKYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+{}[]<>?|\/'
    ques = st.selectbox(
    "Do you want a passwordwith special Character/Characters ?",
    ("YES", "NO"),
    index = None,
    placeholder = "Select Decisions"
  )
    for i in range(numbers):
      if ques == 'NO':
          password+=random.choice(allal)
      elif ques == 'YES':
          password+=random.choice(allsp)
    st.write('PASSWORD :', password)
elif Questions == 'NO':
  st.write('Nevermind')
else:
  st.write('')