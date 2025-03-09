import streamlit as st
import re
import string
import random

def generate_password(length=12):
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Ensure at least one character from each set
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    # Fill the rest of the password
    for _ in range(length - 4):
        password.append(random.choice(lowercase + uppercase + digits + symbols))
    
    # Shuffle the password
    random.shuffle(password)
    return ''.join(password)

def check_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []
    
    # Check length
    if len(password) < 8:
        feedback.append("❌ Password should be at least 8 characters long")
    else:
        score += len(password) // 2
        feedback.append("✅ Good length")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 2
        feedback.append("✅ Contains uppercase letters")
    else:
        feedback.append("❌ Add uppercase letters")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 2
        feedback.append("✅ Contains lowercase letters")
    else:
        feedback.append("❌ Add lowercase letters")
    
    # Check for numbers
    if re.search(r'\d', password):
        score += 2
        feedback.append("✅ Contains numbers")
    else:
        feedback.append("❌ Add numbers")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
        feedback.append("✅ Contains special characters")
    else:
        feedback.append("❌ Add special characters")
    
    # Check for common patterns
    common_patterns = ['123', 'abc', 'password', 'qwerty', 'admin']
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 3
        feedback.append("❌ Contains common patterns")
    
    # Calculate strength category
    if score < 5:
        strength = ("Very Weak", "red")
    elif score < 8:
        strength = ("Weak", "orange")
    elif score < 12:
        strength = ("Moderate", "yellow")
    elif score < 15:
        strength = ("Strong", "light green")
    else:
        strength = ("Very Strong", "green")
    
    return strength, feedback

def main():
    # Custom CSS with light green background
    st.markdown("""
        <style>
        .stApp {
            background-color: #e8f5e9;  /* Light green background */
        }
        .main-header {
            text-align: center;
            background-color: #c8e6c9;  /* Slightly darker green for header */
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
        }
        .password-input {
            margin-bottom: 20px;
        }
        .strength-meter {
            padding: 10px;
            border-radius: 5px;
            margin: 10px 0;
            text-align: center;
            font-weight: bold;
        }
        .feedback-container {
            background-color: white;  /* White background for contrast */
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown('<div class="main-header"><h1>🔒 Password Strength Meter</h1></div>', unsafe_allow_html=True)

    # Password input
    password = st.text_input("Enter your password", type="password", key="password_input")

    # Generate password button
    if st.button("Generate Strong Password"):
        generated_password = generate_password()
        st.code(generated_password, language=None)
        st.info("👆 Copy this password and use it in the password field above to check its strength!")

    if password:
        strength, feedback = check_password_strength(password)
        
        # Display strength
        st.markdown(f"""
            <div class="strength-meter" style="background-color: {strength[1]}">
                Password Strength: {strength[0]}
            </div>
        """, unsafe_allow_html=True)

        # Display feedback
        st.markdown('<div class="feedback-container">', unsafe_allow_html=True)
        st.markdown("### Password Analysis:")
        for item in feedback:
            st.write(item)
        st.markdown('</div>', unsafe_allow_html=True)

        # Password suggestions
        st.markdown("### 💡 Tips for a Strong Password:")
        st.info("""
        - Use at least 12 characters
        - Mix uppercase and lowercase letters
        - Include numbers and special characters
        - Avoid common words and patterns
        - Don't use personal information
        - Use different passwords for different accounts
        """)
       
        st.markdown("<div style='text-align: center; color: #666;'>Made with ❤️ by Shahid Qasim</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main() 
