import streamlit as st



# Record audio using st.audio_input
audio_data = st.audio_input("Record your audio")


# call back to save voice audio
def save_file():
    if audio_data is not None:
        # The returned audio_data is an UploadedFile object
        # Read the audio data into bytes
        audio_bytes = audio_data.read()

        # Save the audio data to a file
        with open("recorded_audio.wav", "wb") as f:
            f.write(audio_bytes)

    
# plays an existing voice audio
def play_audio(filename): 
    st.audio(filename, format='audio/wav')
    




st.button("Save audio as", key=None, help=None, on_click=save_file, args=None, kwargs=None, type="secondary", icon=None, disabled=False, use_container_width=False)