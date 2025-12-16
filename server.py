from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    #Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    #Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)
    
    #Handling an error case from emotion_detector where the dominant emotion is none or empty
    if response.get("dominant_emotion") is None:
        return "Invalid text! Please try again.", 400

    #Extract the emotion scores
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    #Formatting the response
    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, "
        f"'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000''' 
    app.run(host="0.0.0.0", port=5000)