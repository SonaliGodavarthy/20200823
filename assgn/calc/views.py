from django.shortcuts import render
from django.http import HttpResponse
import operator
# Create your views here.

def home(requests):
    return render(requests,'calc/home.html')

def solve(requests):
    num1=int(requests.GET['number1'])
    num2=int(requests.GET['number2'])
    add=num1+num2
    sub=num1-num2
    mul=num1*num2
    div=num1/num2
    return render(requests,'calc/solve.html',{'result1':add,'result2':sub,'result3':mul,'result4':div})
