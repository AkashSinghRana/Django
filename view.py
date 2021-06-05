from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import default_storage


def index(request):
    return render(request, 'index.html')
def about(request):

    text1=(request.POST.get('text','default'))
    text1.strip()
    text2 = (request.POST.get('Upper_case', 'off'))
    text3 = (request.POST.get('Space_Counter', 'off'))
    text4 = (request.POST.get('Word_Counter', 'off'))
    if text2=='on':
        new_text=text1.split('+')
        analyzed_text=''
        for i in new_text:
            analyzed_text=analyzed_text+ i.upper()
        dict = {'purpose': 'Changed To Upper Case', 'analyze_text': analyzed_text}
        return render(request, 'analyze.html',dict)
    elif text3=='on':
        new_text=text1.split(' ')
        c=-1;
        for i in new_text:
            c+=1
        dict = {'purpose': 'Number of Spaces', 'analyze_text': c}
        return render(request,'analyze.html',dict)
    elif text4=='on':
        new_text = text1.split(' ')
        c=0
        for i in new_text:
            c+=1
        dict = {'purpose': 'Number of Words', 'analyze_text': c}
        return render(request, 'analyze.html', dict)
    else:
        return HttpResponse(request, 'Error')




def sign_in(request):
    return render(request, 'sign_in.html')
def register(request):
    text=request.GET.get('name','default')
    text1=request.GET.get('password','default')
    text2=request.GET.get('cpassword','default')
    text3=request.GET.get('male','off')
    text3 = request.GET.get('female', 'off')
    text3 = request.GET.get('others', 'off')
    if text1!=text2:
        return render(request,'sign_in.html')
    else:
        return render(request,'index.html')

