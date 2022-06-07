from re import L
from django.shortcuts import render, get_object_or_404
from .models import ToDoList
from accounts.views import login_view, logout_view, signup_view
from .forms import ToDoListCreateForm


# 내 할 일 목록
def myToDoList(request):
    if request.user.is_authenticated :
    # Post.writer가 현재 로그인인 것만 조회
        # todo_list = get_object_or_404(ToDoList, created_by=request.user)
        todo_list = ToDoList.objects.filter(created_by=request.user, worker=request.user)
        # render 함수의 3번째 인자가 context(딕셔너리)이기 때문에 코딩할 때도 웬만하면 규칙을 지켜서 진행
        context = {
            'todo_list' : todo_list,
        }
        return render(request, 'index.html', context)

# 할 일 추가
def createWhatToDo(request) :
    # form을 불러와서 사용
    if request.method == 'GET' :
        form = ToDoListCreateForm()

        return render(request, )
    pass