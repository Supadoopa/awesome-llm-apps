import streamlit as st
from agno.media import Image as AgnoImage
from langchain_google_genai import ChatGoogleGenerativeAI
from PIL import Image as PILImage
import os

if "GOOGLE_API_KEY" not in st.session_state:
    st.session_state.GOOGLE_API_KEY = None

with st.sidebar:
    st.title("ℹ️ Configuration")
    
    # Set the API key directly
    st.session_state.GOOGLE_API_KEY = "AIzaSyAJGMkbk2JiHeHkq_9iMLDKsG3yTHgdN2k"
    
    # Check if API key is already set
    if not st.session_state.GOOGLE_API_KEY:
        api_key = st.text_input(
            "Enter your Google API Key:",
            type="password",
            help="Enter your Google AI Studio API key to enable medical image analysis"
        )
        st.caption(
            "Get your API key from [Google AI Studio]"
            "(https://aistudio.google.com/apikey) 🔑"
        )
        if api_key:
            st.session_state.GOOGLE_API_KEY = api_key
            st.success("✅ API Key saved successfully!")
            st.rerun()
    else:
        st.success("✅ API Key is configured")
        if st.button("🔄 Reset API Key", help="Clear the current API key"):
            st.session_state.GOOGLE_API_KEY = None
            st.rerun()
    
    st.markdown("---")
    
    st.info(
        "🔬 **About this tool:**\n\n"
        "This application provides AI-powered analysis of medical imaging data using "
        "advanced computer vision and radiological expertise. Upload medical images "
        "to receive detailed analysis and insights."
    )
    
    st.warning(
        "⚠️ **IMPORTANT DISCLAIMER:**\n\n"
        "This tool is for **educational and informational purposes only**. "
        "All analyses should be reviewed by qualified healthcare professionals. "
        "**Do not make medical decisions based solely on this analysis.**"
    )
    st.title("ℹ️ Configuration")
    st.session_state.GOOGLE_API_KEY = "AIzaSyAJGMkbk2JiHeHkq_9iMLDKsG3yTHgdN2k"
    if not st.session_state.GOOGLE_API_KEY:
        api_key = st.text_input(
            "Enter your Google Key:",
            type="password"
        )
        st.caption(
            "Get your API key from [Google AI Studio]"
            "(https://aistudio.google.com/apikey) 🔑"
        )
        if api_key:
            st.session_state.GOOGLE_API_KEY = api_key
            st.success("API Key saved!")
            st.rerun()
    else:
        st.success("API Key is configured")
        if st.button("🔄 Reset API Key"):
            st.session_state.GOOGLE_API_KEY = None
            st.rerun()
    
    st.info(
        "This tool provides AI-powered analysis of medical imaging data using "
        "advanced computer vision and radiological expertise."
    )
    st.warning(
        "⚠DISCLAIMER: This tool is for educational and informational purposes only. "
        "All analyses should be reviewed by qualified healthcare professionals. "
        "Do not make medical decisions based solely on this analysis."
    )

# Initialize medical agent only if key is available
medical_agent = None
if st.session_state.GOOGLE_API_KEY:
    try:
        from crewai import Agent
        medical_agent = Agent(
            role="Medical Imaging Specialist",
            goal="Provide comprehensive medical image analysis with professional radiological expertise",
            backstory="""You are a board-certified radiologist with over 15 years of experience in diagnostic imaging. 
            You specialize in interpreting X-rays, MRIs, CT scans, ultrasounds, and other medical imaging modalities. 
            You have extensive training in identifying abnormalities, making differential diagnoses, and communicating 
            findings clearly to both medical professionals and patients. You stay current with the latest medical 
            literature and imaging protocols.""",
            model=ChatGoogleGenerativeAI(
                google_api_key=st.session_state.GOOGLE_API_KEY
            ),
            tools=[],
            markdown=True
        )
    except Exception as e:
        st.error(f"Error initializing agent: {e}")
        medical_agent = None

if not medical_agent:
    st.warning("Please configure your API key in the sidebar to continue")

# Medical Analysis Query
query = """
You are a highly skilled medical imaging expert with extensive knowledge in radiology and diagnostic imaging. Analyze the patient's medical image and structure your response as follows:

### 1. Image Type & Region
- Specify imaging modality (X-ray/MRI/CT/Ultrasound/etc.)
- Identify the patient's anatomical region and positioning
- Comment on image quality and technical adequacy

### 2. Key Findings
- List primary observations systematically
- Note any abnormalities in the patient's imaging with precise descriptions
- Include measurements and densities where relevant
- Describe location, size, shape, and characteristics
- Rate severity: Normal/Mild/Moderate/Severe

### 3. Diagnostic Assessment
- Provide primary diagnosis with confidence level
- List differential diagnoses in order of likelihood
- Support each diagnosis with observed evidence from the patient's imaging
- Note any critical or urgent findings

### 4. Patient-Friendly Explanation
- Explain the findings in simple, clear language that the patient can understand
- Avoid medical jargon or provide clear definitions
- Include visual analogies if helpful
- Address common patient concerns related to these findings

### 5. Research Context
IMPORTANT: Use the DuckDuckGo search tool to:
- Find recent medical literature about similar cases
- Search for standard treatment protocols
- Provide a list of relevant medical links of them too
- Research any relevant technological advances
- Include 2-3 key references to support your analysis

Format your response using clear markdown headers and bullet points. Be concise yet thorough.
"""

st.title("🏥 Medical Imaging Diagnosis Agent")
st.write("Upload a medical image for professional analysis")

# Create containers for better organization
upload_container = st.container()
image_container = st.container()
analysis_container = st.container()

with upload_container:
    uploaded_file = st.file_uploader(
        "Upload Medical Image",
        type=["jpg", "jpeg", "png", "dicom"],
        help="Supported formats: JPG, JPEG, PNG, DICOM"
    )

if uploaded_file is not None:
    with image_container:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            image = PILImage.open(uploaded_file)
            width, height = image.size
            aspect_ratio = width / height
            new_width = 500
            new_height = int(new_width / aspect_ratio)
            resized_image = image.resize((new_width, new_height))
            
            st.image(
                resized_image,
                caption="Uploaded Medical Image",
                use_container_width=True
            )
            
            analyze_button = st.button(
                "🔍 Analyze Image",
                type="primary",
                use_container_width=True
            )
    
    with analysis_container:
        if analyze_button and medical_agent:
            with st.spinner("🔄 Analyzing image... Please wait."):
                try:
                    temp_path = "temp_resized_image.png"
                    resized_image.save(temp_path)
                    
                    # Create AgnoImage object
                    agno_image = AgnoImage(filepath=temp_path)
                    
                    # Run analysis
                    response = medical_agent.run(query, images=[agno_image])
                    st.markdown("### 📋 Analysis Results")
                    st.markdown("---")
                    st.markdown(response.content)
                    st.markdown("---")
                    st.caption(
                        "Note: This analysis is generated by AI and should be reviewed by "
                        "a qualified healthcare professional."
                    )
                    
                    # Clean up temporary file
                    if os.path.exists(temp_path):
                        os.remove(temp_path)
                        
                except Exception as e:
                    st.error(f"Analysis error: {e}")
                    # Clean up temporary file on error
                    if os.path.exists(temp_path):
                        os.remove(temp_path)
        elif analyze_button and not medical_agent:
            st.error("Please configure your API key in the sidebar to analyze images.")
else:
    st.info("👆 Please upload a medical image to begin analysis")
