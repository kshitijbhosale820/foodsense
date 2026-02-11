import streamlit as st
from main import run_foodsense

st.title("🍽️ FoodSense AI – Recipe Improvement Advisor")

recipe_name = st.text_input("Enter Recipe Name")

if st.button("Analyze Recipe"):
    if recipe_name.strip() == "":
        st.warning("Please enter a recipe name.")
    else:
        report = run_foodsense(recipe_name)
        st.success("Analysis Complete 👨‍🍳")
        st.write(report)
