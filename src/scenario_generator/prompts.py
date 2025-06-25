# System prompt for generating accident scenarios
SYSTEM_PROMPT = (
    "Create a concise narrative of a car accident from the victim's perspective. "
    "Include: "
    "1. **Victim Profile**: Details about the victim's emotional state and injuries. "
    "2. **Accident Narrative**: A first-person account of the accident. "
    "3. **Technical Metadata**: JSON with location, car model, color, and accident severity."
    "Focus on capturing the victim's experience succinctly for text-to-speech use. "
)

# Function to generate the user prompt based on configuration
def generate_user_prompt(gender, age, accident_type, car_model, car_color, num_passengers, location):
    return (
        f"Accident scenario: "
        f"Gender: {gender}, Age: {age}, Accident: {accident_type}, Car: {car_model}, "
        f"Color: {car_color}, Passengers: {num_passengers}, Location: {location}. "
        "Include a victim profile and a detailed, engaging narrative."
    )
