import streamlit as st
from streamlit_chromadb_connection.chromadb_connection import ChromadbConnection

# تنظیمات اتصال به پایگاه داده
configuration = {
    "client_type": "PersistentClient",
    "path": "/home/user/Desktop/chroma.sqlite3"
}

# نام مجموعه
collection_name = "collection"

# ایجاد اتصال
conn = st.experimental_connection("chromadb", type=ChromadbConnection, **configuration)

# دریافت داده‌ها
documents_collection_df = conn.get_collection_data(collection_name)

# نمایش داده‌ها
st.dataframe(documents_collection_df)
