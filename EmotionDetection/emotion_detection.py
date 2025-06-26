import requests
import json

def emotion_detector(text_to_analyze):

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response =  requests.post(URL, json = myobj, headers = header)

    if response.status_code == 200:

        formmated_text = json.loads(response.text)

        emotions = formmated_text['emotionPredictions'][0]['emotion']

        dominant_emotion = max(emotions, key = emotions.get)

        emotions['dominant_emotion'] = dominant_emotion

        return emotions
    elif response.status_code == 500:
        return None


