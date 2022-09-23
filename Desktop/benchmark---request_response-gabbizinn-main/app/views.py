from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest

# Create your views here.

#Last 2
def last_2(request, str):
    if len(str) <2:
        return HttpResponse(0)
    count = 0
    end = str[len(str)-2:]
    for i in range (len(str)-2):
        if str[i:i+2]==end:
            count +=1
    return HttpResponse (count)

#End Other
def end_other(request, str,):

    if str.count("a") == str.count("b"):
        return HttpResponse(True)
    elif str.count("A") == str.count("B"):
        return HttpResponse(False)
    # a = a.lower()
    # b = b.lower()

    # lstr = a
    # sstr = b

    # if len(b) > len(a):
    #     lstr = b
    #     sstr = a

    # if sstr == lstr[len(lstr) - len(sstr): len(lstr)]:
    #     return HttpResponse(True)
    # else:
    #     return HttpResponse(False)



def lone_sum(request, a,b,c):
    if c == b and c == a  and a == b:
        return HttpResponse(0)
    elif a == b:
        return HttpResponse(c)
    elif a == c:
        return HttpResponse(b)
    elif b == a:
        return HttpResponse(c)
    elif b == c:
        return HttpResponse(a)
    elif c == a:
        return HttpResponse(b)
    elif c == b:
        return HttpResponse(a)
    else:
        return HttpResponse(a + b + c)