import string
import random
import streamlit as st
import re

# Step 1: Function to generate password
def generate_password(length):
    characters = string.digits + string.ascii_letters + "!@#$%^&*()_+"
    return "".join(random.choice(characters) for i in range(length))

# Step 2: Function to check password strength
def check_password_strength(password):
    score = 0
    common_passwords = ["12345678", "abc123", "khan123", "pakistan123", "password"]
    if password in common_passwords:
        return "This password is too common. Choose a more unique one.", "weak"
    
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password length should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add at least one special character (!@#$%^&*).")

    if score == 4:
        return "Strong Password", "Strong"      
    elif score == 3:
        return "Moderate Password - Consider adding more security features.", "Moderate"  
    else:
        return "\n".join(feedback), "weak"

# Streamlit input for checking password strength
input_password = st.text_input("Enter your password", type="password")

if st.button("Check Strength"):
    if input_password:
        result, strength = check_password_strength(input_password)
        if strength == "Strong":
            st.success(result)
            st.balloons()
        elif strength == "Moderate":
            st.warning(result)
        else:
            st.error("Weak Password - Improve it using these tips:")
            for tip in result.split("\n"):
                st.write(tip)
    else:
        st.warning("Please enter a password")

# Streamlit input for generating password
password_length = st.number_input("Enter the length of password", min_value=8, max_value=20, value=10)

if st.button("Generate Password"):
    password = generate_password(password_length)     
    st.success(f'Generated Password: {password}')
