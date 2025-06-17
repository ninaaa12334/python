# import streamlit as st
#
# col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")
# with col1:
#     st.header("col1")
#
#     st.write("This is column 1")
#
# with col2:
#     st.header("col2")
#     st.write("This is column 2")
#
# with col3:
#     st.header("col3")
#     st.write("This is column 3")
#
# with col4:
#     st.header("col4")
#     st.write("This is column 4")
#
# with col5:
#     st.header("col5")
#     st.write("This is column 5")


st.sidebar.header("Sidebar")

st.sidebar.write("This is a sidebar ")
st.sidebar.selectbox("Choose one option", ["Option 1","Option 2","Option 3" ])
st.sidebar.radio("GO to", ["Home", "Data", "Settings"])

import streamlit as st

col1, col2, col3, col4, col5 = st.columns(5, gap="small", vertical_alignment="center")
with col1:
    st.header("col1")

    st.write("This is column 1")

with col2:
    st.header("col2")
    st.write("This is column 2")

with col3:
    st.header("col3")
    st.write("This is column 3")

with col4:
    st.header("col4")
    st.write("This is column 4")

with col5:
    st.header("col5")
    st.write("This is column 5")



tab1, tab2, tab3, = st.tabs(["News", "Sport"," Economy"])

with tab1:
    st.header("News")
    st.writer("Latest name")

with tab2:
    st.header("Sport")
    st.writer("Latest news about sport ")


with tab3:
    st.header("Economy")
    st.writer("Latest news about economy")


