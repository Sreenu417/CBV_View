from django.shortcuts import render

# Create your views here.
from django.views.generic import View,TemplateView
from django.http import HttpResponse
from app.forms import *

# FBV for returning string

def fbv_string(request):
    return HttpResponse('This is function based views string')


# CBV for returning  string

class cbv_string(View):
    def get(self,request):
        return HttpResponse('This is class based view string')
    
# FBV for returning HTML page

def fbv_html(request):
    return render(request,'fbv_html.html')


# CBV for returning HTML page

# class cbv_html(View):
#     def get(self,request):
#         return render(request,'cbv_html.html')            ( OR  )

class cbv_direct(TemplateView):               # No need of creating views directly render html page through  URL mapping
    template_name='cbv_direct.html'





# Handling Forms by using View (Function based views for insering the topic)

def FBV_form(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('topic inserted successfully')

    return render(request,'FBV_form.html',d)


# Handling Forms by using View (Class based views for insering the topic)

class CBV_form(View):
    def get(self,request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'CBV_form.html',d)
    
    def post(self,request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('topic inserted successfully')