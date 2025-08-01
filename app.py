import streamlit as st
import base64

# Function to add background image with light blur & overlay
def add_subtle_bg(image_path):
    with open(image_path, "rb") as file:
        encoded = base64.b64encode(file.read()).decode()
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        .main::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.3); /* light white overlay */
            z-index: -1;
        }}
        </style>
    """, unsafe_allow_html=True)

# Use your uploaded background image
add_subtle_bg("bg.jpg")  # Make sure it's in the same folder

# App content
st.title("🚀 CAREER COMPA$$")
st.write("Step into your future with confidence!")

# Inputs
name = st.text_input("👤 What is your name?")
hobbies = st.text_input("🎯 What are your hobbies?")
skills = st.text_input("🛠️ List your top skills")
interests = st.text_input("📚 What subjects or fields interest you most?")
goals = st.text_input("🎯 What are your future goals?")

# Career Suggestion Logic
if st.button("🔍 Suggest Career"):
    suggestion = f"Hey {name if name else 'there'}! Based on your responses, you might be interested in "

    if "data" in skills.lower():
        suggestion += "Data Science or Business Analytics 📊."
        st.image("Coding.jpg")
    elif "design" in hobbies.lower() or "creativity" in skills.lower():
        suggestion += "Graphic Design or UI/UX Design 🎨."
        st.image("artistic.jpg")
    elif "helping" in goals.lower() or "teaching" in hobbies.lower():
        suggestion += "Education or Social Work 🧠."
        st.image("teacher.jpg")
    elif "code" in skills.lower() or "programming" in hobbies.lower():
        suggestion += "Software or Web Development 👨‍💻 / 👩‍💻."
    elif "stock market" in goals.lower() or "trading" in skills.lower():
        suggestion += "Finance or Trading 📈."
        st.image("trader.jpg")
    elif "combat skills" in skills.lower() or "outdoor" in hobbies.lower():
        suggestion += "Military Services or Sports 🏃‍♂️🏅."
        st.iamge("officer.jpg")
    elif "writing" in hobbies.lower() or "storytelling" in skills.lower():
        suggestion += "Content Writing, Journalism, or Script Writing ✍️."
        st.image("writer.jpg") 
    elif "speaking" in skills.lower() or "debating" in hobbies.lower():
        suggestion += "Public Speaking, Politics, or Law 🎙️⚖️."
        st.image("speaker.jpg")
    elif "music" in hobbies.lower() or "instruments" in skills.lower():
        suggestion += "Music Production or Performing Arts 🎵."
        st.image("music.jpg")
    elif "animals" in hobbies.lower() or "pets" in goals.lower():
        suggestion += "Veterinary Science or Animal Welfare 🐾."
        st.image("vet.jpg")
    elif "travel" in hobbies.lower() or "cultures" in goals.lower():
        suggestion += "Travel Blogging, Hospitality, or Tourism ✈️."
        st.image("travel.jpg")
    elif "cooking" in hobbies.lower() or "baking" in skills.lower():
        suggestion += "Culinary Arts or Hospitality 🍳."
        st.image("chef.jpg")
    elif "leadership" in skills.lower() or "management" in goals.lower():
       suggestion += "Business Management or Entrepreneurship 💼."
       st.image("leader.jpg")
    elif "research" in goals.lower() or "experiments" in hobbies.lower():
       suggestion += "Scientific Research or Lab Technology 🔬."
       st.image("lab.jpg")
    elif "languages" in skills.lower() or "multilingual" in hobbies.lower():
        suggestion += "Translator, Interpreter, or Diplomat 🌍."
        st.image("languages.jpg")
    else:
        suggestion += "a wide range of careers — consider speaking with a counselor."

    # Show the final suggestion message after image
    st.success(suggestion)
