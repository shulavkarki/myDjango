from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request,'home.html')

def Count(request):
    Fulltext=request.GET['fulltext']
    splited=Fulltext.split()

    worddictionary={}
    for word in splited:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            worddictionary[word]=1
    sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':Fulltext,'count':len(splited),'sortedwords':worddictionary.items()})
