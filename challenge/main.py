# main.py (Streamlit frontend)
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"  # URL of your FastAPI backend

st.title("Tasks Manager")

# --- Create Task ---
st.header("Create a new task")
title = st.text_input("Title")
description = st.text_area("Description")
if st.button("Add Task"):
    if title and description:
        response = requests.post(f"{API_URL}/tasks/", json={"title": title, "description": description})
        if response.status_code == 200:
            st.success("Task created successfully!")
        else:
            st.error(f"Error: {response.text}")
    else:
        st.warning("Please enter both title and description")

# --- List Tasks ---
st.header("All Tasks")
response = requests.get(f"{API_URL}/tasks/")
if response.status_code == 200:
    tasks = response.json()
    for task in tasks:
        st.subheader(f"{task['id']}: {task['title']}")
        st.write(task["description"])
        col1, col2 = st.columns(2)

        # Delete button
        if col1.button(f"Delete {task['id']}"):
            del_resp = requests.delete(f"{API_URL}/tasks/{task['id']}")
            if del_resp.status_code == 200:
                st.success("Task deleted!")
                st.experimental_rerun()
            else:
                st.error(f"Error: {del_resp.text}")

        # Update button
        new_title = col2.text_input(f"New title {task['id']}", value=task['title'])
        new_desc = col2.text_area(f"New description {task['id']}", value=task['description'])
        if col2.button(f"Update {task['id']}"):
            update_resp = requests.put(
                f"{API_URL}/tasks/{task['id']}",
                json={"title": new_title, "description": new_desc}
            )
            if update_resp.status_code == 200:
                st.success("Task updated!")
                st.experimental_rerun()
            else:
                st.error(f"Error: {update_resp.text}")
else:
    st.error("Failed to fetch tasks")
