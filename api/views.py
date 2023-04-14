from django.shortcuts import render
from api.models import *
from django.http import HttpResponse
import json

def get_question_groups(QG:Question_Group):
    qg = []
    for i in QG.question_ids:
        qg.append(Question.objects.get(q_id=i))
    return qg

def get_question(request):
    question_id = int(request.POST['id'])
    QG = Question_Group.objects.get(qg_id=question_id)
    questions = get_question_groups(QG)
    s_data ={'state':True,
           'type':'question',
           'data':{},
           }
    s_data['data']['Subject'] = QG.subject
    s_data['data']['ac_data'] = QG.ac_data
    s_data['data']['ac_data'] = QG.ac_data
    s_data['data']['question'] = []
    for q in questions:
        mq = {
            'type':q.q_type,
        }
        s_data['data']['question'].append(mq.copy())
    return HttpResponse(json.dumps(s_data),content_type='application/json')

def add_question(request):
    source = request.POST['source']
    questions = json.loads(request.POST['questions'])['question']
    print(questions)
    QG = Question_Group()
    QG.source = source
    QG.ac_data = None
    QG.subject = request.POST['subject']
    q_ids = []
    for q in questions:
        print(q)
        Q = Question()
        Q.ac_data=None
        Q.q_type = q['type']
        Q.choice = q['choice']
        Q.save()
        q_id = Q.q_id
        q_ids.append(q_id)
    QG.question_ids = q_ids
    QG.save()
    s_data ={'state':True,
           'type':'new_question',
           'data':q_ids,
           }
    return HttpResponse(json.dumps(s_data),content_type='application/json')
# Create your views here.
