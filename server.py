from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # Allow frontend to call backend

# Predefined responses
responses = {
    "hello": "Hello! How can I help you?",
    "where do you want to go?": "I can suggest amazing places! Type a city name like 'Jaipur' or 'Delhi'.",
    "jaipur": {
        "name": "Jaipur, Rajasthan",
        "description": "Jaipur, the 'Pink City' of India, is known for its rich history and palaces.",
        "attractions": [
            "🏰 Hawa Mahal - The iconic palace with 953 windows.",
            "🏯 Amber Fort - A majestic fort with elephant rides.",
            "📜 City Palace - A blend of Mughal and Rajasthani architecture.",
        ],
        "food": ["🍛 Dal Baati Churma", "🥟 Pyaaz Kachori", "🍰 Ghewar"],
        "best_time": "October to March (pleasant weather)",
        "transport": "Jaipur has an airport, railway, and bus services."
    },
    "delhi": {
        "name": "Delhi, India",
        "description": "Delhi, the capital of India, is a mix of modernity and history, known for its monuments and street food.",
        "attractions": [
            "🇮🇳 India Gate - A war memorial and major landmark.",
            "🏰 Red Fort - A UNESCO World Heritage Site.",
            "🕌 Qutub Minar - The tallest brick minaret in the world.",
        ],
        "food": ["🍲 Chole Bhature", "🥞 Paratha", "🍗 Butter Chicken"],
        "best_time": "October to March (comfortable for sightseeing)",
        "transport": "Delhi has an international airport, metro, buses, and taxis."
    }
}

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").strip().lower()
    
    # Simulating chatbot thinking time
    time.sleep(2)

    # Check predefined responses
    if user_input in responses:
        if isinstance(responses[user_input], dict):  # If it's a city
            data = responses[user_input]
            response_text = (
                f"📍 {data['name']}\n"
                f"ℹ️ {data['description']}\n\n"
                f"🏛️ **Top Attractions:**\n" + "\n".join(data["attractions"]) +
                f"\n\n🍽️ **Must-Try Food:**\n" + "\n".join(data["food"]) +
                f"\n\n🗓️ **Best Time to Visit:** {data['best_time']}\n"
                f"🚗 **Transport Options:** {data['transport']}"
            )
        else:
            response_text = responses[user_input]
    else:
        response_text = "🤖 Sorry, I don't understand that. Please ask another question."

    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
