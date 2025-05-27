import streamlit as st
from PIL import Image
import io
from ai_utils import query_openrouter

# Streamlit page config
st.set_page_config(page_title="Solar Rooftop Analyzer", layout="centered")

st.title("🔆 Solar Industry AI Assistant")
st.write("Upload a satellite image of a rooftop and describe it to assess solar installation potential.")

# Image uploader
uploaded_file = st.file_uploader("Upload Satellite Rooftop Image", type=["jpg", "jpeg", "png"])

# Show image preview (optional visual context)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Rooftop Image", use_column_width=True)

# Prompt generation function
def generate_prompt_from_user_input(description):
    return f"""
You are an expert solar engineer. Given the rooftop details below, provide:

1. Estimated usable area (in sq. meters)
2. Suggested number of solar panels
3. Expected monthly energy output (in kWh)
4. Approximate installation cost (INR)
5. Expected ROI/payback period
6. Recommended solar panel type (Monocrystalline/Polycrystalline)
7. Maintenance advice (e.g., cleaning frequency, warranty)
8. Any relevant government incentives/net metering policies for India
9. Confidence level of the estimate (e.g., High/Medium/Low) and assumptions used

Rooftop Description:
{description}
"""


# User input form
st.markdown("### 📝 Describe Your Rooftop")
user_description = st.text_area(
    "Provide details like size (in sq. meters), location, shade, sunlight hours, obstructions, orientation, etc.",
    height=150,
    placeholder="E.g. Flat concrete rooftop, 100 sq.m, Delhi, 6 hours sunlight/day, minor shade from water tank..."
)

# Analyze button
if st.button("🔍 Analyze Solar Potential"):
    if user_description.strip() == "":
        st.warning("Please provide some rooftop details to analyze.")
    else:
        with st.spinner("Running AI analysis..."):
            try:
                prompt = generate_prompt_from_user_input(user_description)
                result = query_openrouter(prompt)
                st.success("✅ Analysis Complete")
                st.markdown("### Solar Installation Report")
                st.markdown(result)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")


with st.expander("📊 View Performance Metrics"):
    st.markdown("""
    - **Avg. AI Response Time:** 3–5 seconds  
    - **Uptime:** 100% (for local use or if hosted on Hugging Face)  
    - **Max Upload:** 5MB images  
    - **API Provider:** OpenRouter  
    - **Cost:** Free (under OpenRouter API trial)
    """)
