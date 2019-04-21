import jellyfish
import logging

log = logging.getLogger("duplicate_lines_detection")
log.setLevel(logging.INFO)
ch = logging.StreamHandler()
formatter = logging.Formatter(
	'%(asctime)s - %(name)s, %(lineno)d - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
log.addHandler(ch)


class DuplicateLineDetector(object):
	"""
	class to detect duplicate lines in a file
	by implementing Jaro-Winkler similarity
	using Jellyfish library 
	"""

	def __init__(self, file_name):
		self.file_name = file_name
		self.threshold = 0.7
		self.lines_in_file  = list()


	def _read_file(self):
		with open(self.file_name) as f:
			self.lines_in_file = f.read().splitlines()


	def _is_similar(self, line1, line2):
		similarity_score = jellyfish.jaro_winkler(line1, line2)
		log.debug('companring: ({}, {}) similarity_score: {}'
					.format(line1, line2, similarity_score))
		return similarity_score >= self.threshold


	def detect_duplicates(self):
		self._read_file()
		duplicates = list()
		for i in range(len(self.lines_in_file)):
			duplicate_lines = []
			for j in range(len(self.lines_in_file)):
				if i is not j and self._is_similar(self.lines_in_file[i],self.lines_in_file[j]):
					duplicate_lines.append({
						'line_number' : j + 1,
						'content' : self.lines_in_file[j]
						})

			if duplicate_lines:
				duplicates.append({
					'line_number': i + 1,
					'content' : self.lines_in_file[i],
					'duplicate_line_numbers': list(map(lambda x:x['line_number'], duplicate_lines))
					})

		log.debug('duplicates: {}'.format(duplicates))
		return duplicates


if __name__== '__main__':
	duplicate_detector = DuplicateLineDetector('test.txt')
	print(duplicate_detector.detect_duplicates())
