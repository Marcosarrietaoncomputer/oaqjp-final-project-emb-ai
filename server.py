"""
This app serves the user to detect and extract emotions from a sentence,
while also showcasing what's the dominant emotion
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion detector")

@app.route("/emotionDetector")
def emot_detector():
    """ 
    Detects the emotion from the user input and returns
    the pondered emotion detected plus the main emotion for the sentence
    """

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text!. Please try again!"

    return f"""For the given statement, the system response is
    'anger': {response['anger']},
    'disgust': {response['disgust']},
    'fear': {response['fear']},
    'joy': {response['joy']},
    'sadness': {response['sadness']}.
    The dominant emotion is {response['dominant_emotion']}"""


@app.route("/")
def render_index_page():
    """
    Renders the home page for the web
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
