from flask import Flask, request, jsonify, render_template
from model import llama_response, granite_response, mistral_response
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_message = data.get('message')
    model = data.get('model')
    
    if not user_message or not model:
        return jsonify({"error": "Missing message or model selection"}), 400
    
    system_prompt = "You are an AI assistant helping with customer inquiries. Provide a helpful and concise response."
    
    start_time = time.time()
    
    try:
        if model == 'llama':
            result = llama_response(system_prompt, user_message)
        elif model == 'granite':
            result = granite_response(system_prompt, user_message)
        elif model == 'mistral':
            result = mistral_response(system_prompt, user_message)
        else:
            return jsonify({"error": "Invalid model selection"}), 400
        
        result['duration'] = time.time() - start_time
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)



# //```
# We import necessary modules from Flask.
# We create a Flask application instance.
# We define a route /generate that will handle POST requests. This is where our AI logic will go.
# For now, it returns a simple JSON response.
# The if __name__ == '__main__': block ensures the Flask development server runs when we execute this file directly.



# Let's break down the changes:

# We import our model-specific response functions.
# In the /generate route, we now expect JSON input with 'message' and 'model' fields.
# We add error handling for missing inputs.
# We use a try-except block to handle potential errors in AI processing.
# We measure and include the processing time in the response.
# This setup allows us to handle requests for different models and provides robust error handling.


# ```//