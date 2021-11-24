from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import instructorinfo

def need_help(request):
    if request.method == "GET":
        context = {}
        context['data'] = instructorinfo.objects.all()
        return render (request, 'vote/need_help.html',context)
    if request.method == "POST":
        data = request.POST
        instructorinfo.objects.create(fullname = data['fullname'],number = data['number'], address= data['address'], 
                                        bio = data['bio'], gender = data['gender'])
        return render(request,'finish.html')
def helper(request):
    a = instructorinfo.objects.all()
    context = {'azin':a}
    # context = {}
    # context['azin'] = a
    # print(a)
    return render (request, 'vote/helper.html', context = context)

   




        

