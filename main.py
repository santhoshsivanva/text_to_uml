import streamlit as st
from functions import *
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin' # to be removed in production

text = st.text_area("Hello World", height=300)
b = st.button("Generate")

if b:
    if not text.endswith("."): text += "." 
    uml, inheritance, relationship, object, object_inh = text_to_uml(text)
    graph = graph_from_uml(uml, inheritance, relationship, object, object_inh)
    image_url = "graphs/" + get_random_id(5) + ".png"
    graph.write_png(image_url)
    st.image(image_url)
    os.remove(image_url)