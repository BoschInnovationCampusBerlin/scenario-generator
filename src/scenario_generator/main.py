import streamlit as st
from openai import AzureOpenAI
from prompts import SYSTEM_PROMPT, generate_user_prompt
from configs.scenario_config import GENDER_OPTIONS, AGE_RANGE, ACCIDENT_TYPE_OPTIONS, CAR_MODEL_OPTIONS, CAR_COLOR_OPTIONS, NUM_PASSENGERS_RANGE, LOCATION_OPTIONS
from configs.model_config import MODEL_CONFIG
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize Azure OpenAI client
client = AzureOpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
    api_version=MODEL_CONFIG['api_version'],
    azure_endpoint=MODEL_CONFIG['endpoint']
)

st.title("Accident Scenario Generator")
st.write("This application generates an accident scenario based on your configuration settings on the left. Once configured, press the 'Generate Accident Scenario' button to see the generated scenario.")

st.sidebar.header("Configure Scenario")
gender = st.sidebar.selectbox("Gender:", GENDER_OPTIONS)
age = st.sidebar.number_input("Age:", **AGE_RANGE)
accident_type = st.sidebar.selectbox("Type of Accident:", ACCIDENT_TYPE_OPTIONS)
car_model = st.sidebar.selectbox("Car Model:", CAR_MODEL_OPTIONS)
car_color = st.sidebar.selectbox("Car Color:", CAR_COLOR_OPTIONS)
num_passengers = st.sidebar.number_input("Number of Passengers:", **NUM_PASSENGERS_RANGE)
location = st.sidebar.selectbox("Location:", LOCATION_OPTIONS)

if st.button("Generate Accident Scenario", key="generate_button", help="Click to generate a scenario", use_container_width=True):
    prompt = generate_user_prompt(gender, age, accident_type, car_model, car_color, num_passengers, location)
    response = client.chat.completions.create(
        model=MODEL_CONFIG['engine'],
        messages=[{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": prompt}],
        max_tokens=MODEL_CONFIG['max_tokens'],
        temperature=MODEL_CONFIG['temperature'],
        top_p=MODEL_CONFIG['top_p']
    )
    
    # Extract content from the response
    content = response.choices[0].message.content

    st.text_area("Result:", content.strip(), height=800, max_chars=None, key=None, help=None, on_change=None, args=None, kwargs=None, placeholder=None, disabled=False, label_visibility="visible")
    
    # Button to save output to a markdown file and open in a new tab
    st.download_button(
        label="Save to Markdown",
        data=content.strip(),
        file_name="accident_scenario.md",
        mime="text/markdown"
    )
