# Scenario Generator

This is a simple chatbot application using Streamlit and Azure OpenAI.

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

3. **Set Azure OpenAI API Key**

   Replace `<your-api-key>` in `src/scenario_generator/main.py` with your actual Azure OpenAI API key.

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

This will start the application on a local server, and you can interact with the chatbot through the Streamlit UI.