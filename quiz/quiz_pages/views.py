from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect

from .models import Theme, Question, Choice

# Create your views here.
def index(request):
    template = 'quiz_pages/index.html'
    themes = Theme.objects.all()
    context = {'themes': Theme.objects.all()}
    for theme in themes:
        print(theme.theme_text)

    return render(request, 'quiz_pages/index.html', context=context)

def quiz(request, theme_id):
    theme = Theme.objects.get(pk=theme_id)
    questions = Question.objects.filter(theme=theme)
    context = {'theme': theme, 'questions': questions}
    return render(request, 'quiz_pages/quiz.html', context=context)

def add_quiz(request):
    return render(request, 'quiz_pages/add_quiz.html')


'''
    This function is called when the user submit the form to add a quiz.
    It gets all the data from the form and create objects in the database only 
    if the form is correctly filled.
'''
def check_form(request):
    if request.method == 'POST':
        theme = request.POST['theme_text']

        if (theme == ''):
            return render(request, 'quiz_pages/add_quiz.html', {'error_message': "You didn't fill the form correctly."})
        
        for existing_theme in Theme.objects.all():
            if (existing_theme.theme_text.strip().lower() == theme.strip().lower()):
                return render(request, 'quiz_pages/add_quiz.html', {'error_message': "This theme already exists."})

        theme = Theme(theme_text=theme)

        questions = []
        choices = []
        for i in range(10):
            question = request.POST['question_text_' + str(i)]
            if (question == '' and i == 0): 
                return render(request, 'quiz_pages/add_quiz.html', {'error_message': "You must fill at least 1 question."})
            
            if question != '':
                question = Question(question_text=question, theme=theme)
                questions.append(question)

                for j in range(4):
                    choice = request.POST['choice_text_' + str(i) + '_' + str(j)]
                    if (choice == ''):
                        return render(request, 'quiz_pages/add_quiz.html', {'error_message': "You must fill all the choices."})

                    is_valid_answer = False

                    if request.POST.get('valid_answer_' + str(i)) == str(j):
                        is_valid_answer = True

                    choices.append(Choice(choice_text=choice, question=question, is_valid_answer=is_valid_answer))

        theme.save()

        for question in questions :
            question.save()
        
        for choice in choices:
            choice.save()
        
        return HttpResponseRedirect(reverse('quiz_pages:index'))

    return render(request, 'quiz_pages/add_quiz.html', {'error_message': "You didn't fill the form correctly."})

def results(request, theme_id):
    theme = get_object_or_404(Theme, pk=theme_id)
    answers = {}
    for question in theme.question_set.all():
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice' + str(question.id)])
            answers[question] = selected_choice
                
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'quiz_pages/quiz.html', {
                'questions' : theme.question_set.all(),
                'theme': theme,
                'error_message': "You didn't select a choice.",
            })

    context = {'theme': theme, 'questions' : theme.question_set.all(),  'answers': answers}
    return render(request, 'quiz_pages/results.html', context)