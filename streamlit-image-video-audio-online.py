import streamlit as st

st.markdown('## Image Embedded Example')
# st.image('https://www.dreamstime.com/stock-images-tropic-view-image2457614')
st.image('tropic.jpg')  # mporw na valw jpg kai png
st.markdown('## Image credit:')
st.markdown("""
    Creator: User !@#$%%^&& (instagram,twitter,...)
""")

st.markdown('## Video Embedded Example')
st.video('https://youtu.be/bo_efYhYU2A')  # mporw na valw mp3 kai mp4 epishs
st.markdown('## Video credit:')
st.markdown('Lady Gaga-Shallow, on YouTube')

st.markdown('## Audio file Embedded Example')
st.audio('https://soundcloud.com/chopin-frederic/nocturne-op9-no2?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing')
st.markdown('## Audeo credit:')
st.markdown('Chopin, on Soundcloud')

