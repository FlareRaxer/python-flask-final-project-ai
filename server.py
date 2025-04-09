"""
Flask web server for emotion detection using Watson NLP API.
Handles GET and POST requests and displays the dominant emotion.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """
    Route to handle emotion detection from user input.
    Accepts GET and POST methods.
    """
    if request.method == "POST":
        text_to_analyze = request.form['textToAnalyze']
    else:
        text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    if result is None or result.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is 'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, "
        f"and 'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}."
    )
    return response


@app.route("/")
def index():
    """Route to serve the homepage."""
    return render_template("index.html")


# Start the Flask development server
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)
