from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    '''Renders index page.'''
    recent_questions = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_questions_list': recent_questions}

    # without render shortcut
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context, request))

    # with shortcut
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    '''Renders details page.'''
    # without shortcuts
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     return Http404("Question does not exist")

    # return render(request, 'polls/detail.html', {'question': question})

    # with shortcuts
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    '''Renders results page.'''
    response = "You are looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    '''Renders vote page.'''
    return HttpResponse("You are votting on the question %s." % question_id)
