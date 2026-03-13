import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(page_title="LLM Accuracy & Discrepancy Tracker", layout="wide")

# --- SIDEBAR INPUTS ---
with st.sidebar:
    st.header("Company Profile")

    company_name = st.text_input("Name of Company", value="RetroTech Rebuilds")
    company_category = st.text_input("Category of Company", value="Refurbished Electronics Retailer")
    company_area = st.text_input("Area of Company (Location)", value="San Antonio, TX")
    target_website = st.text_input("Target URL", value="https://retrotechrebuilds-fake.com")

    st.divider()
    st.button("Run Analysis", type="primary", use_container_width=True)

# --- MOCK DATA: REFURBISHED TECH THEME ---
bogus_address = "9999 Circuit Breaker Lane, San Antonio, TX 78253"

# 1. Define the Matrix Data FIRST
discrepancy_data = pd.DataFrame({
    "Data Point": ["Physical Store Address", "Standard Warranty", "Flagship Inventory"],
    "Company Website": [bogus_address, "90-Day Limited Warranty", "Refurbished Business Laptops"],
    "GPT 5.4": ["100 Downtown Plaza", "1-Year Full Warranty", "Refurbished Business Laptops"],  # 1 Match
    "Sonnet 4.6": ["Online Only (No Storefront)", "90-Day Limited Warranty", "Refurbished Business Laptops"],  # 2 Matches
    "Gemini 3.1": [bogus_address, "90-Day Limited Warranty", "Refurbished Business Laptops"]  # 3 Matches
})

# 2. Dynamically calculate accuracy percentages
total_points = len(discrepancy_data)

def get_accuracy(model_col):
    matches = sum(discrepancy_data[model_col] == discrepancy_data["Company Website"])
    return f"{int((matches / total_points) * 100)}%"

# 3. Inject calculated accuracies into the LLM data
# FIX: Updated the arguments passed to get_accuracy() to match the new dataframe columns
llm_data = {
    "Chat GPT 5.4 Pro": {
        "response": f"{company_name} sells refurbished business laptops. They are located at 100 Downtown Plaza. All purchases come with a 1-year full warranty.",
        "accuracy": get_accuracy("GPT 5.4"),
        "sources": "Reddit r/thinkpad, ServeTheHome Forums, Local tech blog 'Alamo City Tech'"
    },
    "Claude Sonnet 4.6": {
        "response": f"This is an online-only storefront specializing in refurbished business laptops. They offer a standard 90-day limited warranty.",
        "accuracy": get_accuracy("Sonnet 4.6"),
        "sources": f"Yelp Reviews (2023), {target_website.strip('https://')}/shipping, Spiceworks Community threads"
    },
    "Gemini 3.1 Pro": {
        "response": f"Located at {bogus_address}, they sell refurbished business laptops with a standard 90-day limited warranty.",
        "accuracy": get_accuracy("Gemini 3.1"),
        "sources": f"{target_website.strip('https://')}/contact, Google Business Profile, r/homelab wiki"
    }
}

# FIX: Updated recommendations to use the new model names
recommendations = [
    f"**Location SEO:** Claude Sonnet 4.6 thinks you are an online-only store, and GPT 5.4 pulled an old or incorrect address. Ensure {bogus_address} is explicitly tagged in the footer of every page using LocalBusiness Schema markup.",
    "**Warranty Hallucinations:** GPT 5.4 hallucinated a 1-year full warranty, which could cause customer service disputes. Create a dedicated '/warranty-policy' page with clear headers so LLM crawlers don't confuse your policy with competitor standards.",
    "**Niche Inventory Omission:** All models correctly identified your flagship 'Refurbished Business Laptops', but none mentioned your enterprise networking gear. If refurbished Cisco switches and MikroTik routers are high-margin items, create dedicated pillar pages for 'Refurbished Enterprise Networking'.",
    "**Business Hours Mismatch:** Claude Sonnet 4.6 stated the store is open 24/7, likely confusing your physical storefront with your e-commerce checkout. Hardcode your physical operating hours (e.g., Mon-Fri 9AM-6PM) into your site's header and update your Google Business Profile.",
    "**Hidden Fees Ignored:** All three models failed to mention your 15% restocking fee on returned laptops. Add a clear, easily parsed 'Return Conditions' bulleted list to individual product pages so LLMs summarize the financial caveats accurately."
]

# --- DASHBOARD UI ---

st.title("📊 LLM Discrepancy & Website Accuracy Dashboard")
st.markdown("Analyze how different LLMs interpret your company data compared to the Source of Truth.")

st.divider()

# Section 1: Raw LLM Outputs & Accuracy Metrics
st.subheader(f"1. AI Outputs for {company_name}")
col1, col2, col3 = st.columns(3)

models = list(llm_data.keys())
columns = [col1, col2, col3]

for i, col in enumerate(columns):
    model_name = models[i]
    with col:
        st.markdown(f"### {model_name}")
        st.metric(label="Accuracy vs. Company Website", value=llm_data[model_name]["accuracy"])
        st.info(llm_data[model_name]["response"])
        st.caption(f"**Attributed Sources:** {llm_data[model_name]['sources']}")

st.divider()

# Section 2: Discrepancy & Accuracy Matrix
st.subheader("2. Discrepancy Matrix")
st.markdown("Detailed breakdown of data points. The **Company Website** column is your official data.")

# Style the dataframe to highlight discrepancies and the source of truth
def highlight_discrepancies(row):
    styles = [''] * len(row)
    ground_truth = row['Company Website']

    for i, col in enumerate(row.index):
        if col == 'Company Website':
            styles[i] = 'background-color: rgba(173, 216, 230, 0.4); font-weight: bold;'
        elif col not in ['Data Point', 'Company Website']:
            if row[col] != ground_truth:
                styles[i] = 'background-color: rgba(255, 99, 71, 0.3)'
            else:
                styles[i] = 'background-color: rgba(144, 238, 144, 0.3)'
    return styles

styled_df = discrepancy_data.style.apply(highlight_discrepancies, axis=1)
st.dataframe(styled_df, use_container_width=True, hide_index=True)

st.divider()

# Section 3: Website Improvement Recommendations
st.subheader("3. Actionable Website Improvements")

for rec in recommendations:
    st.warning(rec, icon="💡")
