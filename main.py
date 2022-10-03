import streamlit as st
import newspaper
import nltk

# st.markdown('<style> .css-1v0mbdj {margin:0 auto; width:50%; </style>', unsafe_allow_html=True)


st.title('Article Summarizer')

url = st.text_input('', placeholder='Paste the URL of the article amd press Enter')

if url:
    try:
        article = newspaper.Article(url)

        article.download()
        # article.html
        article.parse()

        img = article.top_image
        st.image(img)

        title = article.title
        st.subheader(title)

        authors = article.authors
        st.text(','.join(authors))


        article.nlp()

        keywords = article.keywords
        st.write('Keywords:')
        st.write(', '.join(keywords))

        st.subheader('Summary')
        summary = article.summary
        st.write(summary)
    except:
        st.error('Sorry something went wrong')
