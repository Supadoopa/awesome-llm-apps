# 🏥 Medical Imaging Diagnosis Agent

An AI-powered medical imaging analysis tool that provides professional-grade analysis of medical images using advanced computer vision and radiological expertise.

## ⚠️ Important Disclaimer

**This tool is for educational and informational purposes only. All analyses should be reviewed by qualified healthcare professionals. Do not make medical decisions based solely on this analysis.**

## 🚀 Features

- **Multi-modal Image Support**: Analyzes X-rays, MRIs, CT scans, ultrasounds, and other medical imaging formats
- **Comprehensive Analysis**: Provides detailed findings, diagnostic assessments, and patient-friendly explanations
- **Research Integration**: Uses DuckDuckGo search to find relevant medical literature and treatment protocols
- **Professional Interface**: Clean, intuitive Streamlit interface for easy image upload and analysis
- **Safety Warnings**: Built-in disclaimers and safety notifications
- **Secure API Key Management**: Secure handling of API keys with session state

## 📋 Prerequisites

- Python 3.8 or higher
- Google AI Studio API key (for Gemini model access)
- Internet connection (for research and search functionality)

## 🛠️ Installation

1. **Clone or download this repository**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your Google API Key**:
   - Visit [Google AI Studio](https://aistudio.google.com/apikey)
   - Create a new API key
   - Copy the key for use in the application

## 🔐 Security Notes

- **Never commit API keys to version control**
- The application uses session state to store API keys temporarily
- API keys are cleared when you reset them or close the session
- A `.gitignore` file is included to prevent accidental commits of sensitive files

## 🎯 Usage

1. **Run the application**:
   ```bash
   streamlit run ai_medical_imaging.py
   ```

2. **Configure API Key**:
   - Enter your Google API key in the sidebar
   - The key will be securely stored in the session
   - You can reset the key anytime using the reset button

3. **Upload Medical Image**:
   - Supported formats: JPG, JPEG, PNG, DICOM
   - Click "Upload Medical Image" to select your file
   - The image will be automatically resized for optimal processing

4. **Analyze Image**:
   - Click "🔍 Analyze Image" to start the analysis
   - Wait for the AI to process the image and generate results

5. **Review Results**:
   - The analysis includes:
     - Image type and region identification
     - Key findings and abnormalities
     - Diagnostic assessment with confidence levels
     - Patient-friendly explanations
     - Research context with medical literature references

## 📊 Analysis Components

### 1. Image Type & Region
- Identifies imaging modality (X-ray, MRI, CT, Ultrasound, etc.)
- Specifies anatomical region and positioning
- Assesses image quality and technical adequacy

### 2. Key Findings
- Systematic listing of primary observations
- Detailed description of abnormalities
- Measurements, densities, and characteristics
- Severity ratings (Normal/Mild/Moderate/Severe)

### 3. Diagnostic Assessment
- Primary diagnosis with confidence level
- Differential diagnoses in order of likelihood
- Evidence-based analysis
- Critical or urgent findings identification

### 4. Patient-Friendly Explanation
- Clear, jargon-free explanations
- Visual analogies where helpful
- Addresses common patient concerns

### 5. Research Context
- Recent medical literature references
- Standard treatment protocols
- Technological advances
- Relevant medical links

## 🔧 Technical Details

- **AI Model**: Gemini 1.5 Flash
- **Framework**: Streamlit for web interface
- **Image Processing**: PIL (Python Imaging Library)
- **Search Integration**: DuckDuckGo Search
- **Media Handling**: Agno framework
- **Agent Framework**: CrewAI

## 🛡️ Safety & Privacy

- **No Data Storage**: Images are processed temporarily and not stored
- **Local Processing**: Image analysis happens locally with secure API calls
- **Professional Review**: All results should be reviewed by healthcare professionals
- **Educational Use**: Designed for learning and research purposes
- **Secure API Handling**: API keys are managed securely in session state

## 🐛 Troubleshooting

### Common Issues:

1. **API Key Error**:
   - Ensure your Google API key is valid and has sufficient credits
   - Check that the key is properly entered in the sidebar
   - Try resetting the API key if issues persist

2. **Image Upload Issues**:
   - Verify the image format is supported (JPG, JPEG, PNG, DICOM)
   - Ensure the image file is not corrupted

3. **Analysis Failures**:
   - Check your internet connection for research functionality
   - Verify the image quality is sufficient for analysis
   - Ensure all dependencies are properly installed

4. **Dependency Issues**:
   - Run `pip install -r requirements.txt` to ensure all packages are installed
   - Check Python version compatibility (3.8+)
   - If using a virtual environment, ensure it's activated

5. **Search Functionality Issues**:
   - Ensure internet connection is available
   - Check if DuckDuckGo search is accessible in your region

## 📝 License

This project is for educational purposes. Please ensure compliance with local regulations regarding medical software and AI tools.

## 🤝 Contributing

Contributions are welcome! Please ensure any modifications maintain the safety and educational focus of this tool.

## 📞 Support

For issues or questions, please refer to the troubleshooting section above or create an issue in the repository. 