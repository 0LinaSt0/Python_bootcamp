"""
EXAMPLES OF SCENARIOS (aswer[reactions], ...):
	replicant scenario:
		- 2 [11, 5, 2, 4], 3 [66, 50, 1, 2],
			1 [7, 100, 3, 4], 2 [15, 70, 4, 4],
			1 [17, 5, 2, 5], 1 [33, 12, 3, 7],
			2 [15, 60, 1, 2], 1 [2, 120, 2, 2],
			1 [9, 30, 3, 5], 1 [13, 66, 3, 3]
		- all answers and reactions 2
	human scenario:
		- 3 [11, 77, 5, 8], 3 [15, 90, 4, 6],
			1 [107, 100, 6, 7], 2 [15, 70, 3, 4],
			2 [17, 50, 3, 5], 2 [16, 74, 5, 7],
			2 [15, 60, 3, 8], 1 [13, 110, 5, 4],
			3 [11, 99, 5, 5], 3 [13, 66, 3, 5]
		- all answers 3, reactions [15, 65, 5, 7]
"""


from questions import Questions
from answers import Answers
from reactions import Reactions
from interview_conducting import interviewer
from customException import customException


def who_are_you(answers, reactions, questions_counter):
	if questions_counter == 0:
		return 
	print("\t ~~~~~~~ Verdict ~~~~~~~")
	verdict = (
		answers.is_human()
		+ reactions.is_respiration_norm(questions_counter)
		+ reactions.is_heartRate_norm(questions_counter)
		+ reactions.is_blushingLevel_norm(questions_counter)
		+ reactions.is_pupillaryDilation_norm(questions_counter)
	)

	(print("YOU'R A HUMAN. YOU CAN BE FREE") if verdict > 0
		else print("!DANGER! REPLICANT WAS DETECTED"))


if "__main__" == __name__:
	try:
		questions = Questions("questions.json")
		answers = Answers()
		reactions = Reactions()
		interviewer(questions, answers, reactions)
		who_are_you(answers, reactions, questions.questions_count)
		answers.write_answers()
	except customException as e:
		details = e.args[0]
		print(details)

