# server.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat_handler():
    user_message = request.json.get('message', '')
    
    # Простейшая логика ответа
    if 'привет' in user_message.lower():
        bot_response = "Привет! Как дела?"
    elif 'пока' in user_message.lower():
        bot_response = "До свидания!"
    elif 'нормально' or 'хорошо' or 'шикарно' in user_message.lower():
        bot_response = "Отлично ! "
    elif 'плохо' in user_message.lower():
        bot_response = "Плохо , но вы не расстраивайтесь."
    else:
        bot_response = f"Вы сказали: {user_message}"
    
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)