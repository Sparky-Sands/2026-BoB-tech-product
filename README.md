# 2026-BoB-tech-product
# LLM Accuracy & Discrepancy Tracker

### What your application does
This application is a dashboard mockup designed to help businesses audit how major Large Language Models (LLMs) interpret their company data. It simulates comparing the outputs of three major AI models (GPT 5.4, Sonnet 4.6, and Gemini 3.1) against a company's official website (the "Source of Truth"). 

The dashboard dynamically calculates accuracy percentages, highlights data discrepancies (like hallucinated addresses or fake store hours) in a color-coded matrix, and provides actionable SEO and content recommendations to help the business correct these AI hallucinations.

### What tech/frameworks does it use
* **Python 3.x:** The core programming language.
* **Streamlit:** The frontend framework used to instantly turn the Python scripts into an interactive web dashboard.
* **Pandas:** Used for data manipulation, styling the discrepancy matrix, and dynamically calculating the accuracy metrics.

### What the judge should do to navigate/interpret your application
Once the application is running in your browser, please take the following steps to evaluate it:
1.  **Sidebar (Left):** Observe the "Company Profile" inputs. These parameters define the context for the simulated AI outputs.
2.  **Section 1 (AI Outputs):** Review the raw AI responses and their attributed sources. Notice the large "Accuracy vs. Company Website" metrics; these are dynamically calculated based on how well the AI's data matches the ground truth in Section 2.
3.  **Section 2 (Discrepancy Matrix):** This is the core analytical view. The blue column represents the "Source of Truth" (official website data). Look at the AI model columns: green cells indicate the AI successfully matched the truth, while red cells indicate an AI hallucination or data discrepancy.
4.  **Section 3 (Recommendations):** Read the actionable business intelligence provided at the bottom, which instructs the business on how to fix their website schema and content based on the errors found in the matrix.

### How to run your application
**Using the automated script (Recommended):**
We have included a `run.sh` script that installs the necessary dependencies and starts the Streamlit server automatically.
1. Open your terminal and navigate to the root directory of this project.
2. Make the script executable: `chmod +x run.sh`
3. Execute the script: `./run.sh`

**Manual execution:**
If you prefer to run it manually, ensure Python is installed, then run:
1. `pip install streamlit pandas`
2. `streamlit run Project-Mockup.py` (ensure the filename matches the script in the directory).

### A way to tell if the app started successfully
Once the execution command is run, you will see output in your terminal similar to this:

```text
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: [http://192.168.1.](http://192.168.1.)X:8501
