import requests

API_KEY = "YOUR_API_KEY"
URL = "YOUR_WATSON_API_URL"


def detect_emotion(text):
    headers = {"Content-Type": "application/json"}
    params = {"version": "2021-08-01"}

    data = {
        "text": text,
        "features": {"emotion": {}}
    }

    try:
        response = requests.post(
            URL,
            json=data,
            headers=headers,
            params=params,
            auth=("apikey", API_KEY)
        )
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return None


def format_emotion_result(response):
    if not response:
        return {"error": "Unable to analyze emotion"}

    emotions = response["emotion"]["document"]["emotion"]
    dominant = max(emotions, key=emotions.get)

    return {
        "emotions": emotions,
        "dominant_emotion": dominant
    }

