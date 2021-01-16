from django.shortcuts import render, get_object_or_404
from django.http import Http404, JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .models import AutoEvaluation
from .forms import AutoEvaluationForm

from school.models import Student
# Create your views here.

import requests
import os
def activate_view(request):
    if request.user.is_authenticated:
        id = 1;
        value = request.GET.get('val', None)
        if id:
            time = get_object_or_404(AutoEvaluation, id=id)
            if value == 'true':
                time.activate = True
            else: 
                time.activate = False
            time.save()
    else:
        raise Http404("User is not authenticated")
    return render(request, 'dashboard/autoevaluation_form.html')

@method_decorator(login_required, name='dispatch')
class AutoEvaluationView(UpdateView):
    form_class = AutoEvaluationForm
    template_name = 'evaluation/autoevaluation_form.html'
    success_url = reverse_lazy('student_list')

    def get_object(self):
        time, created = AutoEvaluation.objects.get_or_create(id=1)
        return time

def restart_board(request):
    json_response = {'recount':'False'}
    if request.user.is_authenticated:
        id = request.GET.get('idb', None)
        if id:
            student = get_object_or_404(Student, id_board=id)
            response = os.popen(f"ping -c 4 {student.ip_board}").read()
            if "4 received" in response:
                #print(student.ip_board)
                _ = requests.get("http://"+str(student.ip_board), params={'recount':'true'})
                json_response['recount'] = True
            else:
                print("No hay conexión")
    else:
        raise Http404("User is not authenticated")
    return JsonResponse(json_response)

def activate_view(request):
    if request.user.is_authenticated:
        id = 1;
        value = request.GET.get('val', None)
        if id:
            time = get_object_or_404(AutoEvaluation, id=id)
            if value == 'true':
                time.activate = True
            else: 
                time.activate = False
            time.save()
    else:
        raise Http404("User is not authenticated")
    return render(request, 'dashboard/autoevaluation_form.html')

def plus_score(request):
    json_response = {'sent':'False'}
    if request.user.is_authenticated:
        id = request.GET.get('cs', None)
        if id:
            student = get_object_or_404(Student, id=id)
            response = os.popen(f"ping -c 4 {student.ip_board}").read()
            if "4 received" in response:
                #print(student.ip_board)
                _ = requests.get("http://"+str(student.ip_board), params={'plus':'true'})
                student.score = student.score + 1
                student.accum_score = student.accum_score + 1
                student.save()
                json_response['sent'] = True
            else:
                print("No hay conexión")
    else:
        raise Http404("User is not authenticated")
    return JsonResponse(json_response)

def minus_score(request):
    json_response = {'sent':'False'}
    if request.user.is_authenticated:
        id = request.GET.get('cs', None)
        if id:
            student = get_object_or_404(Student, id=id)
            response = os.popen(f"ping -c 4 {student.ip_board}").read()
            if "4 received" in response:
                _ = requests.get("http://"+str(student.ip_board), params={'minus':'true'})
                student.score = student.score - 1
                student.accum_score = student.accum_score - 1
                student.save()
                json_response['sent'] = True
            else:
                print("No hay conexión")
    else:
        raise Http404("User is not authenticated")
    return JsonResponse(json_response)