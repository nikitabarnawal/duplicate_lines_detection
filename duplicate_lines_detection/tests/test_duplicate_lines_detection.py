from django.test import TestCase
from ..duplicate_lines_detection import DuplicateLineDetector


class TestDuplicateLineDetector(TestCase):
	def setUp(self):
		self.duplicate_lines_detector = DuplicateLineDetector('test.txt')

	def test_is_similar_gives_low_score_if_texts_are_different(self):
		text1 = 'Hello world'
		text2 = 'I am going to Home'
		similarity_score = self.duplicate_lines_detector._is_similar(text1,text2)
		self.assertTrue(similarity_score < 0.4)


	def test_is_similar_gives_high_score_if_texts_are_similar(self):
		text1 = 'Hello World'
		text2 = 'Hello World Hello'
		similarity_score = self.duplicate_lines_detector._is_similar(text1,text2)
		self.assertTrue(similarity_score > 0.9)
