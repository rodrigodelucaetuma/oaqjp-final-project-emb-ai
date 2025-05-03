'''
Server file designed to deploy an emotion detector app via flask. 
'''

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def display_emotion_detector_result():
    '''
    Error-handling function to process values produced with emotion_detector and 
    signal error if client input is empty.
    '''
    text = request.args.get('text')
    result = emotion_detector(text)

    str_result = ''.join([str(element) for element in result])

    if 'dominant_emotion is None' in str_result:
        return "<b>Invalid text!</b> Please try again!"

    return f"<p>{result}</p>"+"<p>Given statement:</p>"+f"<p>'{text}'</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
