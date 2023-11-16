from django.shortcuts import render, get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Choice, Question

# Create your views here.
# index() 함수 작성
def index(request):
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5] # 5개의 최근 Question 객체를 가져옴
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context) # polls/index.html에 context 변수를 적용하여 HTML 텍스트를 만듬

# detail() 함수 작성
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question':question})

# redirect해줄 vote() 함수 작성
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        # 설문 투표 폼을 다시 보여준다
        return render(request, 'polls/detail.html', {
            'question':question,
            'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # POST 데이터를 정상적으로 처리하였으면
        # 항상 HttpResponseRedirect를 반환하여 리다이렉션 처리함
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    
# results() 함수 작성
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question':question})