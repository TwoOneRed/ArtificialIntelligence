import streamlit as st
import pandas as pd
from PIL import Image


st.title("ARTIFICIAL INTELLIGENCE PROJECT")

st.header("1. GENETIC ALGORITHM")
st.write("Solve a vacation planning problem using Genetic Algorithm (GA).")
image1 = Image.open('ga1.png')
image2 = Image.open('ga2.png')
image3 = Image.open('ga3.png')

imagecsp1 = Image.open('csp1.png')
imagecsp2 = Image.open('csp2.png')
imagecsp3 = Image.open('csp3.png')
imagecsp4 = Image.open('csp4.png')
imagecsp5 = Image.open('csp5.png')

nb = Image.open('nb.png')

depth5 = Image.open('depth5.png')
depth6 = Image.open('depth6.png')
depth7 = Image.open('depth7.png')
depth8 = Image.open('depth8.png')

cluster1 = Image.open('dendro.png')
cluster2 = Image.open('cluster.png')

option = '1'
option = st.selectbox(
     'Choose One Example?',
     ('1', '2', '3'))

if option == '1':
    st.image(image1, caption='Example 1')
elif option == '2':
    st.image(image2, caption='Example 2')
elif option == '3':
    st.image(image3, caption='Example 3')

st.header("2. CONSTRAINT SATISFICATION PROBLEM")
st.write("By using Constraint Satisfication Problem, assign the right vaccine type and amount to the vaccination centre.")
stateop = '1'
stateop = st.selectbox(
     'Choose One State?',
     ('State 1', 'State 2', 'State 3','State 4','State 5'))

if stateop == 'State 1':
    st.image(imagecsp1, caption='State 1')
elif stateop == 'State 2':
    st.image(imagecsp2, caption='State 2')
elif stateop == 'State 3':
    st.image(imagecsp3, caption='State 3')
elif stateop == 'State 4':
    st.image(imagecsp4, caption='State 4')
elif stateop == 'State 5':
    st.image(imagecsp5, caption='State 5')


st.header("3. CLASSIFICATION AND CLUSTERS")
st.subheader('a.) Naive Bayes')
st.image(nb, caption='Naive Bayes')

st.subheader('b.) Decision Tree')
depop = '1'
depop = st.selectbox(
     'Select A Depth For Decision Tree',
     ('5', '6', '7','8'))

if depop == '5':
    st.image(depth5, caption='Depth of 5')
elif depop == '6':
    st.image(depth6, caption='Depth of 6')
elif depop == '7':
    st.image(depth7, caption='Depth of 7')
elif depop == '8':
    st.image(depth8, caption='Depth of 8')

st.subheader('c.) Hierarchical Clustering')
st.image(cluster1, caption='Ddendrogram')
st.image(cluster2, caption='Cluster Diagram')
