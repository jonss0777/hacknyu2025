import streamlit as st

# Record audio using st.audio_input
audio_data = st.audio_input("Record your audio")

if audio_data is not None:
    # The returned audio_data is an UploadedFile object
    # Read the audio data into bytes
    audio_bytes = audio_data.read()

    # Save the audio data to a file
    with open("recorded_audio.wav", "wb") as f:
        f.write(audio_bytes)

    # Optionally, play the recorded audio
    st.audio(audio_bytes, format='audio/wav')
