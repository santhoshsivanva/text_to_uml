import streamlit as st
from functions import *
import os

st.title("Text to UML Diagram Generator")

text = st.text_area("Write your specification here", height=200)
btn = st.button("Generate")

if btn:
    if not text.endswith("."): text += "." 
    uml, inheritance, relationship, object, object_inh = text_to_uml(text)
    graph = graph_from_uml(uml, inheritance, relationship, object, object_inh)
    image_url = "graphs/" + get_random_id(5) + ".png"
    graph.write_png(image_url)
    st.image(image_url)
    os.remove(image_url)
