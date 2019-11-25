from survey import AnonymousSurvey

# create a survey
program_language_survey = AnonymousSurvey("What language do you work? ")

# store the response
program_language_survey.show_question()
print("Enter 'q' at any time to quit.")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    program_language_survey.store_response(response)

# Show the survey results
print("Thank you to everyone who take part in the survey!")
program_language_survey.show_results()
