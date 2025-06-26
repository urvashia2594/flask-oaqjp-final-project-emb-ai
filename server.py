''' This is main server file '''
from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector App")

@app.route("/emotionDetector")
def get_emotion_detection():
    """
    Get the detected emotion for a given input statement.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    if result is None:
        return "Invalid text! Please try again!."
    dominant = result.pop('dominant_emotion')

    scores_str = ', '.join([f"'{k}': {v:.9f}" for k, v in result.items()])

    response = (
        f"For the given statement, the system response is {scores_str}. "
        f"The dominant emotion is <b>{dominant} </b>."
    )
    return  response

@app.route("/")
def index():
    """
    Load index.html.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True, port= 5000)
