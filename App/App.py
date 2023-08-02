import streamlit as st
import nltk
import spacy
nltk.download('stopwords')
spacy.load('en_core_web_sm')

import pandas as pd
import base64, random
import time, datetime
import io, random
#from streamlit_tags import st_tags
from PIL import Image
import os
from pyresparser import ResumeParser





def run():
    st.title("Smart Resume Analyser")
    st.sidebar.markdown("# Choose User")
    activities = ["Candidate", "HR"]
    choice = st.sidebar.selectbox("Choose among the given options:", activities)
    
    #img = Image.open('./Logo/SRA_Logo.jpg')
    #img = img.resize((250, 250))
    #st.image(img)

    
    
    if choice == 'Candidate':
   
        st.subheader("Resume Parser")
        def file_selector(folder_path='./resumes'):
            filenames = os.listdir(folder_path)
            selected_filename = st.selectbox('Select a file', filenames)
            return os.path.join(folder_path, selected_filename)
        
        
        filename = file_selector()
        st.write("You selected '%s' " % filename)
        
        
        data = ResumeParser(filename).get_extracted_data()
        
        df = pd.DataFrame()
        #df = df.append(data, ignore_index=True)
        
        df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)

        
        
        
        cols = list(df.columns)
        cols.insert(0, cols.pop(cols.index('name')))
        df = df.reindex(columns= cols)
        st.write(df[cols])
        
        
        st.subheader("Skills from resume")
        st.table(df["skills"])
        st.subheader("Experience from resume")
        st.table(df["experience"])
        
                


run()
