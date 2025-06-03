# # from langdetect import detect

# # text = input("Enter text to detect language: ")
# # print(detect(text))



# import streamlit as st
# from langdetect import detect, LangDetectException

# # --- Streamlit UI ---

# st.set_page_config(
#     page_title="Language Detector",
#     layout="centered",
#     # icon="🌐"
# )

# st.title("🌐 Language Detector")
# st.write("Enter text in any language below to detect it.")

# st.markdown("---")

# # Streamlit ka text input widget
# text_to_detect = st.text_area(
#     "📝 Enter text here:",
#     height=150,
#     placeholder="Type or paste text here (e.g., 'Hello world', 'नमस्ते दुनिया', '你好世界')",
#     help="Enter the text whose language you want to detect."
# )

# st.markdown("---")

# if st.button("🔍 Detect Language", use_container_width=True):
#     if text_to_detect:
#         with st.spinner("Detecting..."):
#             try:
#                 # Language detection
#                 detected_language = detect(text_to_detect)
#                 st.success(f"**Detected Language:** `{detected_language.upper()}`")
#                 st.info("Note: `langdetect` may return 'un' for some less common or very short texts.")
#             except LangDetectException as e:
#                 st.error(f"Could not detect language. Please enter more text or try different text. Error: {e}")
#             except Exception as e:
#                 st.error(f"An unexpected error occurred: {e}")
#     else:
#         st.warning("Please enter some text to detect its language.")

# st.markdown("""
# <style>
# .footer {
#     position: fixed;
#     left: 0;
#     bottom: 0;
#     width: 100%;
#     background-color: #f0f2f6;
#     color: #888;
#     text-align: center;
#     padding: 10px;
#     font-size: 0.8em;
# }
# </style>
# <div class="footer">
#     Created with ❤️ using Streamlit and langdetect.
# </div>
# """, unsafe_allow_html=True)



import streamlit as st
from langdetect import detect, LangDetectException

# --- Streamlit UI ---

st.set_page_config(
    page_title="Language Detector",
    layout="centered",
    # icon="🌐"
)

st.title("🌐 Language Detector")
st.write("Enter text in any language below to detect it.")

st.markdown("---")

# Streamlit ka text input widget
text_to_detect = st.text_area(
    "📝 Enter text here:",
    height=150,
    placeholder="Type or paste text here (e.g., 'Hello world', 'नमस्ते दुनिया', '你好世界')",
    help="Enter the text whose language you want to detect."
)

st.markdown("---")

if st.button("🔍 Detect Language", use_container_width=True):
    if text_to_detect:
        with st.spinner("Detecting..."):
            try:
                # Language detection
                detected_language = detect(text_to_detect)

                # --- MODIFICATION START ---
                if detected_language: # Check if detected_language is not None or empty
                    st.success(f"**Detected Language:** `{detected_language.upper()}`")
                    st.info("Note: `langdetect` may return 'un' for some less common or very short texts.")
                else:
                    st.warning("Could not confidently detect a language. Please try more text or different text.")
                # --- MODIFICATION END ---

            except LangDetectException as e:
                st.error(f"Could not detect language. This often happens with very short or ambiguous text. Please enter more text or try different text. Error: {e}")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
    else:
        st.warning("Please enter some text to detect its language.")

st.markdown("""
<style>
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #f0f2f6;
    color: #888;
    text-align: center;
    padding: 10px;
    font-size: 0.8em;
}
</style>
<div class="footer">
    Created by Hadiqa Gohar ❤️ .
</div>
""", unsafe_allow_html=True)
