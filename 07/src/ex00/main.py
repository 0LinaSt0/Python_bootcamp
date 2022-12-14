"""
EXAMPLES OF SCENARIOS (aswer[reactions], ...):
	replicant scenario:
		- 2 [11, 5, 2, 4], 3 [66, 50, 1, 2],
			1 [7, 100, 3, 4], 2 [15, 70, 4, 4],
			1 [17, 5, 2, 5], 1 [33, 12, 3, 7],
			2 [15, 60, 1, 2], 1 [2, 120, 2, 2],
			1 [9, 30, 3, 5], 1 [13, 66, 3, 3]
	human scenario:
		- 3 [11, 77, 5, 8], 3 [15, 90, 4, 6],
			1 [107, 100, 6, 7], 2 [15, 70, 3, 4],
			2 [17, 50, 3, 5], 2 [16, 74, 5, 7],
			2 [15, 60, 3, 8], 1 [13, 110, 5, 4],
			3 [11, 99, 5, 5], 3 [13, 66, 3, 5]
"""


from questions import Questions
from answers import Answers
from reactions import Reactions
from interview_conducting import interviewer


def who_are_you(answers, reactions):
	print("\n\n\t\t ~~~~~~~ Verdict ~~~~~~~")
	verdict = (
		answers.is_human()
		+ reactions.is_respiration_norm()
		+ reactions.is_heartRate_norm()
		+ reactions.is_blushingLevel_norm()
		+ reactions.is_pupillaryDilation_norm()
	)

	(print("YOU'R A HUMAN. YOU CAN BE FREE") if verdict > 0
		else print("!REPLICANT WAS DETECTED!"))


if "__main__" == __name__:
	queations = Questions()
	answers = Answers()
	reactions = Reactions()

	interviewer(queations, answers, reactions)
	who_are_you(answers, reactions)
	answers.output_answers()

