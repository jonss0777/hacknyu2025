import streamlit as st
import pandas as pd
#import io
import os


def message():
    
    print("user input received")

ref = st.audio_input("Record your voice", key="user_voice", help="record voice", on_change=message, args=None, kwargs=None, disabled=False, label_visibility="visible")

print("*****\n")
print(type(ref))
print("*****\n")
print(ref)
print("*****\n")


file_path = "hacknyu2025"

save_dir = "recorded_audio"
if not os.path.exists(file_path):
    os.makedirs(file_path)
if ref:
    with open(file_path, "wb") as file:
        file.write(ref) 
    
    # Show success message and audio player
    st.success(f"Audio saved to {file}")
    st.audio(file_path)
    
 