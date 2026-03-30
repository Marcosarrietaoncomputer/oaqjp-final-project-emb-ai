from EmotionDetection.emotion_detection import emotion_detector

import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        joy_statement = emotion_detector('I am glad this happened')
        self.assertEqual(joy_statement['dominant_emotion'], "joy")

        anger_statement = emotion_detector('I am really mad about this')
        self.assertEqual(anger_statement['dominant_emotion'], "anger")

        disgust_statement = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(disgust_statement['dominant_emotion'], "disgust")

        sadness_statement = emotion_detector('I am so sad about this')
        self.assertEqual(sadness_statement['dominant_emotion'], "sadness")

        fear_statement = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(fear_statement['dominant_emotion'], "fear")

        

unittest.main()

