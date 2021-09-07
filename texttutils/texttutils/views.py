#i have added this file
from django.http import HttpResponse
from django.shortcuts import render
def  index(request):
    params={'name':'suraj','place':'Earth'}
    return render(request,'index.html',params)

def analyze(request):
    # get the text here
    djtext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')

    if removepunc == "on":
        analyzed = ""
        punctuations = '''!()-[}]{;:'"\/,.<>?@#$%^&*_~+='''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove Punctuation','analyzed_text': analyzed}
        # analyze the text
        djtext=analyzed
        # return render(request, 'analyze.html',params)
    if (fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new lines ', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove Extra Space  ', 'analyzed_text': analyzed}
    if(removepunc !="on" and extraspaceremover !="on" and newlineremover !="on" and fullcaps!="on") :
        return HttpResponse("Please chosse any of these 4 options to do some operaton ")
    

    return render(request,'analyze.html',params)