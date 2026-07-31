from EmotionDetection import emotion_detector


def test_emotion_detector():

    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for statement, expected in test_cases.items():
        response = emotion_detector(statement)
        actual = response["dominant_emotion"]

        if actual == expected:
            print(f"PASS: '{statement}' -> {actual}")
        else:
            print(f"FAIL: '{statement}' -> Expected {expected}, Got {actual}")


test_emotion_detector()