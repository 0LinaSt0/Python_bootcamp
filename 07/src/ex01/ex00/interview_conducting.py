# FOR INPUT ANSWERS

def estimate(reactions):
	print("\t~.~.~.~.~.~.~.~.~.~.~\n")
	print("I SEE. YOUR ...")
	reactions.degree("respiration", reactions.check_respiration)
	reactions.degree("heart rate", reactions.check_heartRate)
	reactions.degree("blushing level [1; 6]", reactions.check_blushingLevel)
	reactions.degree("pupillary dilation [2; 8]", reactions.check_pupillaryDilation)


def interviewer(questions, answers, reactions):
	questions_generator = questions.out_questions()
	for question_key, i in zip(questions_generator, range(1,11)):
		print(question_key)
		print("\t1) {}".format(questions.questions_dict[question_key]["1"]))
		print("\t2) {}".format(questions.questions_dict[question_key]["2"]))
		print("\t3) {}".format(questions.questions_dict[question_key]["3"]), end='\n\n')
		answers.append_answer(i)
		estimate(reactions)
		print('\n\n')


