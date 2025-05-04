'''
Program designed to contain function for running emotion detection.
'''

import json
import requests


def emotion_detector(text_to_analyze):
    '''
    Function to run emotion detection via Watson LP Library (already embedded in this IDE).
    '''
    text = text_to_analyze

    formatted_empty_result = f"<b>Error:</b> No input text provided. Use ?text=your%20text <p>'anger': <i>None</i>, disgust': <i>None</i>, 'fear': <i>None</i>, 'joy': <i>None</i> and 'sadness': <i>None</i>. The dominant_emotion is None.</p>"
    
    if not text:
        return formatted_empty_result, 400

    try: 
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        myobj = { "raw_document": { "text": text_to_analyze } }
        header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
        response = requests.post(url, json = myobj, headers = header)
        formatted_response = json.loads(response.text)

        emotions_set = formatted_response['emotionPredictions'][0]['emotion']
        result = dict(sorted(emotions_set.items(), key= lambda x:x[1], reverse= True))
        result.update({'dominant emotion': next(iter(result))})

        formatted_result = (
            f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}, "
            f"'joy': {result['joy']} and 'sadness': {result['sadness']}. "
            f"The <b>dominant emotion</b> is {result['dominant emotion']}."
        )
        return formatted_result
    
    except Exception as e:

        print("Error:", e)
        return f"<h1>Server Error: {e}</h1>", 500
