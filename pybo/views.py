from django.shortcuts import render
from django.http import HttpResponse

def index(requste):
    return HttpResponse("Welcome 안녕하세요 pybo에 오신 것을 환영합니다.")
