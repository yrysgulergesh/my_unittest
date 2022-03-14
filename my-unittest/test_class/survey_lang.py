from survey import AnonymousSurvery

question = "Какой язык программирования для вас наиболее интересен?"

my_survey = AnonymousSurvery(question)

my_survey.show_question()
print("Нажмите 'q' для выхода с опроса. \n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\n Спасибо за ответ")
my_survey.show_results()