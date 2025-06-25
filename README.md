# Scenario Generator

This application generates detailed accident scenarios using Streamlit and Azure OpenAI. It provides a user-friendly interface to configure various parameters and generates a narrative from the victim's perspective.

## How to Run

1. **Ensure Python 3.13 is Installed**
   
   Verify that Python 3.13 is installed on your system:
   
   ```bash
   python3.13 --version
   ```

2. **Install Dependencies**
   
   Make sure you have [Poetry](https://python-poetry.org/docs/#installation) installed and then run:
   
   ```bash
   poetry install
   ```

3. **Set Environment Variables**

   Create a `.env` file in the root directory and add your Azure OpenAI API key:
   
   ```
   OPENAI_API_KEY=<your-api-key>
   ```

4. **Activate the Virtual Environment**

   Use the following command to activate the virtual environment:
   
   ```bash
   source $(poetry env info --path)/bin/activate
   ```

5. **Run the Application**

   Use Streamlit to run the app:
   
   ```bash
   poetry run streamlit run src/scenario_generator/main.py
   ```

6. **Using the Application**

   - Configure the scenario parameters using the sidebar.
   - Click "Generate Accident Scenario" to create a narrative.
   - Use the "Save to Markdown" button to download the scenario.

This application is designed to produce outputs that are directly consumable by text-to-speech generators, focusing on creating an engaging and realistic narrative from the victim's perspective.