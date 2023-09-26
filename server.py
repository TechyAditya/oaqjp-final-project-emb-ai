"""
Program server.py that handles Emotion Detector API calls
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    del response['dominant_emotion']
    
    if dominant_emotion is None:
        return "Invalid input! Try again. "
    else:
        score = response[dominant_emotion]
        output = "For the given statement, the system response is:<br>"
        output += "<br>".join([f"{key}: {value}" for key, value in response.items()])
        output += f"<br><br>The dominant emotion is {dominant_emotion} with a score of {score}.<br>"
        return output
    
@app.route("/")
def render_index_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)