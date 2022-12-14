"""
answers_list = [[#1 scenario], ..., [#n scenario]]
"""

 with pytest.raises(ValueError) as excinfo:
            tasks.start_tasks_db('some/great/path', 'mysql')
        exception_msg = excinfo.value.args[0]
        assert exception_msg == "db_type must be a 'tiny' or 'mongo'"


import pytest


def test_answers(send_answers, create_answers):
	answers = send_answers
	answers_object = create_answers
	for answer in answers:
		


"""

def test_interviewer(create_objects, send_answers, send_degree):
	objects_list = create_objects
	answers_list = send_answers
	degree_list = send_degree
	except_fl = False
	i = 0
	questions_generator = objects_list[0].out_questions()
	for question_key in questions_generator:
		if ()
			with pytest.raises(ValueError) as excinfo:


		if except_fl is False:
			objects_list[1].check_answer(i)
			i += 1
"""
