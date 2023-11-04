import json
import requests

def emotion_detector(text_to_analyse):
    '''
    The function sends the provided text to a emotion detector service via an API request
    and extracts necessary emotion scores and the dominant emotion from the response.
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotion_data = formatted_response['emotionPredictions'][0]['emotion']
        anger = emotion_data['anger']
        disgust = emotion_data['disgust']
        fear = emotion_data['fear']
        joy = emotion_data['joy']
        sadness = emotion_data['sadness']
        dominant_emotion = max(emotion_data, key=emotion_data.get)

    elif response.status_code == 400:
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None

    emotions = {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }
    return emotions
