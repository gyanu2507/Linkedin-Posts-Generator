import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
import os

# Page configuration
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="📝",
    layout="centered"
)

# Load external CSS
def load_css():
    css_file = os.path.join("styles", "main.css")
    with open(css_file) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load CSS
load_css()

# Options for length and language
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

def main():
    # Header with LinkedIn-style branding
    st.markdown("<h1 class='title'>📝 LinkedIn Post Generator</h1>", unsafe_allow_html=True)
    
    # Add a description
    st.markdown("""
        Generate engaging LinkedIn posts with AI. Select your preferences below:
        * Choose a topic that matches your content
        * Select the desired length of your post
        * Pick your preferred language
    """)
    
    # Add a divider
    st.markdown("---")

    # Create three columns for the dropdowns
    col1, col2, col3 = st.columns(3)

    fs = FewShotPosts()
    tags = fs.get_tags()
    
    with col1:
        st.markdown("### Topic")
        selected_tag = st.selectbox("Select a topic", options=tags, label_visibility="collapsed")

    with col2:
        st.markdown("### Length")
        selected_length = st.selectbox("Choose length", options=length_options, label_visibility="collapsed")

    with col3:
        st.markdown("### Language")
        selected_language = st.selectbox("Choose language", options=language_options, label_visibility="collapsed")

    # Generate Button with loading state
    if st.button("✨ Generate Post"):
        with st.spinner('Creating your LinkedIn post...'):
            post = generate_post(selected_length, selected_language, selected_tag)
            
            # Display the generated post in a nice container
            st.markdown("### 🎉 Your Generated Post")
            
            # Display post in a code block with copy button
            st.code(post, language=None)

    # Add footer
    st.markdown("---")
    st.markdown("""
        <div class="footer">
            Made with ❤️ by Gyanu
        </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
