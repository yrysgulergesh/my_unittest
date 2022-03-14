from http.client import responses
import unittest
from survey import AnonymousSurvery

class TestAnonmySurvey(unittest.TestCase):
    """Тесты для класса AnonymousSurvery"""

    def setUp(self):
        """Создание опроса и набора ответов для всех методов"""
        question = "Какой язык программирования для вас наиболее интересен?"
        self.my_survey = AnonymousSurvery(question)
        self.responses = ['Java', 'Python', 'C#', 'Go', 'JavaScript']

    def test_store_single_response(self):
        """Проверяет, что один ответ сохранен правильно."""
        self.my_survey.store_response(self.responses[1])
        self.assertIn(self.responses[1], self.my_survey.responses)



    # def test_store_single_response(self):
    #     """Проверяется, что один ответ сохранен в списке."""
    #     question = "Какой язык программирования для вас наиболее интересен?"
    #     my_survey = AnonymousSurvery(question)
    #     my_survey.store_response('Python')

    #     self.assertIn('Python', my_survey.responses)



    # def test_fife_responses(self):
    #     """Проверяет, что пять ответов были сохранены"""

    #     question = "Какой язык программирования для вас наиболее интересен?"
    #     my_survey = AnonymousSurvery(question)
    #     responses = ['Java', 'Python', 'C#', 'Go', 'JavaScript']
    #     for response in responses:
    #         my_survey.store_response(response)

    #     for response in responses:
    #         self.assertIn(response, my_survey.responses)


unittest.main()


# if __name__ == '__name__':
#     unittest.main()
