import requests
import json

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyse}}
    response = requests.post(url, json=myobj, headers=headers)
    formatted_response = json.loads(response.text)

    dominant_emotion = None
    dominant_score = 0
    emotions = {}

    if response.status_code == 200:
        emotions = formatted_response["emotionPredictions"][0]["emotion"]
        for key, value in emotions.items():
            if value > dominant_score:
                dominant_emotion = key
                dominant_score = value
        emotions["dominant_emotion"] = dominant_emotion
        emotions["code"] = 200
        return emotions
    else:
        # It will return error status codes
        return {"code": response.status_code}
