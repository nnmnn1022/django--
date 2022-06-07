from multiprocessing import context
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponse
from accounts.forms import UserSignupForm

def signup_view(request):
    if request.method == 'GET' :
        form = UserSignupForm
        context = {
            'form' : form
        }
        return render(request,'accounts/signup.html', context)

    # Post 요청 시 데이터 확인 후 회원 생성
    else :
        form = UserSignupForm(request.POST, request.FILES)
        try :
            if form.is_valid :
                # 회원가입 처리
                instance = form.save()
                # return redirect('index.html')
                return redirect('accounts:login')

            else :
                # 인덱스
                return redirect('accounts:signup')

        except ValueError :
            message = '잘못된 입력입니다.'
            context = {
                'form' : form,
                # 'message' : message,
            }
            return (request, 'accounts/signup.html', context)


def login_view(request):
    # GET, POST 분리
    if request.method == 'GET' :
        # 로그인 HTML 응답
        context = {
            'message' : '밥게이트 페이지에 오신 것을 환영합니다.',
            'form' : AuthenticationForm()
        }
        return render(request, 'accounts/login.html', context)

    else :
        form = AuthenticationForm(request, request.POST)
        # 데이터 유효성 검사
        if form.is_valid() :
            # 비즈니스 로직 처리 - 로그인 처리
            login(request, form.user_cache) # django에서 제공하는 로그인, 로그아웃 메소드
            return redirect('index')
        else :
            # 비즈니스 로직 처리 - 로그인 실패
            # 응답
            context = {
                'form' : form,
            }
            return render(request, 'accounts/login.html', context)

def logout_view(request) :
    # 데이터 유효성 검사
    if request.user.is_authenticated :
        # 비즈니스 로직 처리 - 로그아웃
        logout(request)
    
    # 응답
    return redirect('accounts:login')
