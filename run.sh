```bash
#!/bin/bash

echo "Starting Build Process for LLM Accuracy Tracker..."

# Install required Python packages
echo "Installing dependencies (streamlit, pandas)..."
pip install streamlit pandas

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "Dependencies installed successfully."
else
    echo "Error installing dependencies. Please check your Python/Pip installation."
    exit 1
fi

echo "Starting the Streamlit application..."
# NOTE: Make sure "Project-Mockup.py" matches the exact name of your python file and you are in the correct directory.
streamlit run Project-Mockup.py
