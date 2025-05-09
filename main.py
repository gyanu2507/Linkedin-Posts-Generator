import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

# Page configuration
st.set_page_config(
    page_title="LinkedIn Post Generator",
    page_icon="📝",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #0A66C2;
        color: white;
        font-weight: bold;
        padding: 0.5rem;
        margin-top: 2rem;
    }
    .title {
        text-align: center;
        color: #0A66C2;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

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
        <div style="text-align: center; color: #666;">
            Made with ❤️ by Codebasics
        </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
