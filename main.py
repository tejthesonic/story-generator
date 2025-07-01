import os
from secret_key import gem_ai_key
from prompt import llmprompt
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st


os.environ["GOOGLE_API_KEY"] = gem_ai_key
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=gem_ai_key)

def generate_story(text, Category1, Category2, Category3, Category4):
    prompt_template = ChatPromptTemplate.from_messages(
        [
    ("system", llmprompt),
    ("user", f"{text}, Length: {Category1} | Genre: {Category2} | Tone: {Category3} | Audience: {Category4} ")
    ]
    )
    pt = prompt_template.invoke({"text":text,"Category1":Category1,"Category2":Category2,"Category3":Category3,"Category4":Category4})
    response = llm.invoke(pt)
    return response.content


st.title("The Lexicon", width="content")
st.header("Story Writing Assistant", width="content")

text = st.text_input("Describe your story")
#st.write(text)


Category1 = st.sidebar.selectbox(
    "Category 1: Classification by Length (Word Count)",
    ("Flash Fiction", "Short Story", "Novelette", "Novella", "Novel", "Large Novel", "Epic")
)

Category2 = st.sidebar.selectbox(
    "Category 2: Classification by Genre",
    ("Fantasy", "Science Fiction", "Adventure", "Mystery", "Thriller/Suspense", "Horror", "Romance", "Historical Fiction", "Literary Fiction")
)

Category3 =st.sidebar.selectbox(
    "Category 3: Classification by Tone",
    ("Comedic", "Tragic", "Dramatic", "Satirical")
)

Category4 = st.sidebar.selectbox(
    "Category 4: Classification by Target Audience",
    ("Children's", "Young Adult", "Adult")
)   


#response = generate_story(text, Category1, Category2, Category3, Category4)
#st.write(response)

#def generate_and_display_story():
#    response = generate_story(text, Category1, Category2, Category3, Category4)
#    st.markdown(response)
#st.button("Generate Story", on_click= generate_and_display_story)
#'''

if st.button("Generate Story"):
    response = generate_story(text, Category1, Category2, Category3, Category4)
    st.markdown(response)



