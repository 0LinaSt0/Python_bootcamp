"""
EXAMPLES OF SCENARIOS (aswer[reactions], ...):
	replicant scenarios:
		- 2 [11, 5, 2, 4], 3 [66, 50, 1, 2],
			1 [7, 100, 3, 4], 2 [15, 70, 4, 4],
			1 [17, 5, 2, 5], 1 [33, 12, 3, 7],
			2 [15, 60, 1, 2], 1 [2, 120, 2, 2],
			1 [9, 30, 3, 5], 1 [13, 66, 3, 3]
		- all answers and reactions 2
	human scenarios:
		- 3 [11, 77, 5, 8], 3 [15, 90, 4, 6],
			1 [107, 100, 6, 7], 2 [15, 70, 3, 4],
			2 [17, 50, 3, 5], 2 [16, 74, 5, 7],
			2 [15, 60, 3, 8], 1 [13, 110, 5, 4],
			3 [11, 99, 5, 5], 3 [13, 66, 3, 5]
		- all answers 3, reactions [15, 65, 5, 7]
"""


from Reader import Reader
from Writer import Writer
from Interviewer import Interviewer


QUESTIONS_JSON_PATH = "questions.json"
ANSWERS_JSON_PATH = "answers.json"


def take_questions(path):
	try:
		reader = Reader()
		readed_dict = reader.read_file(path)
		return readed_dict
	except Reader.ReaderException as e:
		exit(e)


def write_answers(answers: dict, path):
	try:
		writer = Writer()
		writer.write_to_file(path, answers)
	except Writer.WriterException as e:
		print(e)


def programm_process():
	questions = take_questions(QUESTIONS_JSON_PATH)
	interviewer = Interviewer(questions)
	interviewer.interview_process()
	interviewer.verdict()
	write_answers(interviewer.answers.answers, ANSWERS_JSON_PATH)


if "__main__" == __name__:
	programm_process()
