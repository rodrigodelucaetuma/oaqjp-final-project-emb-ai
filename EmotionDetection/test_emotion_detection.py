'''
Test module for an emotion detection Ai app called "emotion_detection"
'''

import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    '''
    class to keep things together
    '''

    def test_emotion_detector_one(self):
            self.assertIn('"dominant emotion": "joy"', str(emotion_detector("I am glad this happened")))

    def test_emotion_detector_two(self):
            self.assertIn('"dominant emotion": "anger"', str(emotion_detector("I am really mad about this")))

    def test_emotion_detector_three(self):
            self.assertIn('"dominant emotion": "disgust"', str(emotion_detector("I feel disgusted just hearing about this")))

    def test_emotion_detector_four(self):
            self.assertIn('"dominant emotion": "sadness"', str(emotion_detector("I am so sad about this")))

    def test_emotion_detector_five(self):
            self.assertIn('"dominant emotion": "fear"', str(emotion_detector("I am really afraid that this will happen")))


if __name__ == '__main__':
    unittest.main()
