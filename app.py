from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS extension
import os

app = Flask(__name__)
CORS(app, origins="*")  # Enable CORS for all domains

# Define the folder where you want to save the audio files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/send_audio_to_speechsuper', methods=['POST'])
def receive_audio():
    if 'audioFile' not in request.files:
        return jsonify(error="No audio file provided")

    refText = request.form.get("refText")
    audio_file = request.files['audioFile']

    if audio_file:
        filename = 'audio.wav'

        # Save the audio file to the specified folder
        audio_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        return jsonify(message="recieved")
    else:
        return jsonify(error="No valid audio file received")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
