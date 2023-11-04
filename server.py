'''
This the main server file which runs on the terminal and
generates the app with appropriate instructions.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    '''
    This function receives text from the HTML interface and
    performs emotion detection using emotion_detector().
    It returns all the important emotion scores 
    and the dominant emotion for the provided text.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    #else:
    return "For the given statement, the system response is 'anger': " + \
        str(response['anger']) + ", 'disgust': " + str(response['disgust']) + \
        ", 'fear': " + str(response['fear']) + ", 'joy': " + str(response['joy']) + \
        " and 'sadness': " + str(response['sadness']) + ". The dominant emotion is " + \
        str(response['dominant_emotion']) + "."


@app.route("/")
def render_index_page():
    '''
    This function renders the html document with appropriate message.
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)

# run this using "python3.11 server.py"
