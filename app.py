import streamlit as st
import nltk
import spacy
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag, ne_chunk
from nltk.tree import Tree

# Load spaCy model
nlp_spacy = spacy.load("en_core_web_sm")

st.set_page_config(layout="wide")
st.title("NLP Complete Demo Application")

# Sidebar
st.sidebar.header("NLP Settings")

uploaded_file = st.sidebar.file_uploader("Upload Text File (.txt)", type=["txt"])

tokenizer_option = st.sidebar.selectbox(
    "Select Tokenizer",
    ["NLTK", "spaCy"]
)

remove_stopwords = st.sidebar.checkbox("Remove Stopwords")

top_n = st.sidebar.slider("Top N Frequent Words", 5, 50, 10)

show_tfidf = st.sidebar.checkbox("Show TF-IDF Analysis")

ner_option = st.sidebar.selectbox(
    "Select NER Model",
    ["spaCy", "NLTK"]
)

run_button = st.sidebar.button("Run NLP Pipeline")

# Main Logic
if uploaded_file and run_button:

    text = uploaded_file.read().decode("utf-8")

    st.subheader("Raw Text")
    st.write(text)

    # Tokenization
    if tokenizer_option == "NLTK":
        tokens = word_tokenize(text)
    else:
        doc = nlp_spacy(text)
        tokens = [token.text for token in doc]

    st.subheader("Tokenized Text")
    st.write(tokens)

    # Stopword Removal
    if remove_stopwords:
        stop_words = set(stopwords.words("english"))
        tokens = [word for word in tokens if word.lower() not in stop_words and word.isalpha()]
        st.subheader("After Stopword Removal")
        st.write(tokens)

    # Word Frequency
    st.subheader("Word Frequency")
    word_freq = Counter(tokens)
    freq_df = pd.DataFrame(word_freq.items(), columns=["Word", "Frequency"])
    freq_df = freq_df.sort_values(by="Frequency", ascending=False).head(top_n)
    st.dataframe(freq_df)

    fig, ax = plt.subplots()
    ax.bar(freq_df["Word"], freq_df["Frequency"])
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Word Cloud
    st.subheader("Word Cloud")
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(tokens))
    fig_wc, ax_wc = plt.subplots()
    ax_wc.imshow(wordcloud, interpolation='bilinear')
    ax_wc.axis("off")
    st.pyplot(fig_wc)

    # TF-IDF
    if show_tfidf:
        st.subheader("Top TF-IDF Keywords")
        vectorizer = TfidfVectorizer(stop_words="english")
        tfidf_matrix = vectorizer.fit_transform([text])
        feature_names = vectorizer.get_feature_names_out()
        scores = tfidf_matrix.toarray()[0]

        tfidf_df = pd.DataFrame({
            "Word": feature_names,
            "TF-IDF Score": scores
        })

        tfidf_df = tfidf_df.sort_values(by="TF-IDF Score", ascending=False).head(top_n)
        st.dataframe(tfidf_df)

    # Named Entity Recognition
    st.subheader("Named Entity Recognition")

    if ner_option == "spaCy":
        doc = nlp_spacy(text)
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        ner_df = pd.DataFrame(entities, columns=["Entity", "Label"])
        st.dataframe(ner_df)

    else:
        tokens_nltk = word_tokenize(text)
        tagged = pos_tag(tokens_nltk)
        tree = ne_chunk(tagged)

        entities = []
        for subtree in tree:
            if isinstance(subtree, Tree):
                entity = " ".join([token for token, pos in subtree.leaves()])
                label = subtree.label()
                entities.append((entity, label))

        ner_df = pd.DataFrame(entities, columns=["Entity", "Label"])
        st.dataframe(ner_df)

    # POS Tagging
    st.subheader("Part of Speech Tagging")
    pos_tags = pos_tag(word_tokenize(text))
    pos_df = pd.DataFrame(pos_tags, columns=["Word", "POS"])
    st.dataframe(pos_df)

else:
    st.info("Upload a text file and click 'Run NLP Pipeline' to start.")
