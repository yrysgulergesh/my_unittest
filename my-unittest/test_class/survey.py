class AnonymousSurvery():
    """Класс  для анонимих ответтов"""


    def __init__(self, question):
        """Сохраняем вопрос"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Вывод вопроса"""
        print(self.question)

    def store_response(self, new_response):
        """"Сохранение одного ответа"""
        self.responses.append(new_response)

    def show_results(self):
        """Вывод полученных ответов"""
        print("Ответы на опросы: ")
        for response in self.responses:
            print('- ' + response)



            


