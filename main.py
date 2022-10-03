import streamlit as st
import newspaper



st.markdown('<style> .css-1v0mbdj {margin:0 auto; width:50%; </style>', unsafe_allow_html=True)


st.title('Article Summarizer')

url = st.text_input('', placeholder='Paste the URL of the article amd press Enter')

if url:
    article = newspaper.Article(url)

    article.download()
    # article.html
    article.parse()

    img = article.top_image
    if img:
        st.image(img)

    title = article.title
    if title:
        st.subheader(title)

    authors = article.authors
    if authors:
        st.text(','.join(authors))

    date = article.publish_date
    if date:
        st.text(date)

    article.nlp()

    keywords = article.keywords
    st.write('Keywords:')
    st.write(', '.join(keywords))

    st.subheader('Summary')
    summary = article.summary
    st.write(summary)
