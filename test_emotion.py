# ==============================
# 4. test_emotion.py
# ==============================

import unittest
from emotion_detector import format_emotion_result


class TestEmotion(unittest.TestCase):

    def test_dominant_emotion(self):
        sample = {
            "emotion": {
                "document": {
                    "emotion": {
                        "joy": 0.9,
                        "sadness": 0.1,
                        "anger": 0.0,
                        "fear": 0.0,
                        "disgust": 0.0
                    }
                }
            }
        }

        result = format_emotion_result(sample)
        self.assertEqual(result["dominant_emotion"], "joy")


if __name__ == "__main__":
    unittest.main()