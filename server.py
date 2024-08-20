"""
Flask server for the emotion detection module
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    """
    Analyze the given text for emotions and return the result
    """
    text = request.args.get('textToAnalyze')
    response = emotion_detector(text)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, " 
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, " 
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. " 
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Render the index page
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="localhost", port=5000)
