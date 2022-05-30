from django.shortcuts import render
from .models import ToDoList

# 할 일 목록
def todo_list_view(request):
    # Post.writer가 현재 로그인인 것만 조회
    todo_list = ToDoList.objects.filter(todolist_writer=request.user, worker=request.user)
    # render 함수의 3번째 인자가 context(딕셔너리)이기 때문에 코딩할 때도 웬만하면 규칙을 지켜서 진행
    context = {
        'todo_list' : todo_list,
    }
    return render(request, 'posts/post_list.html', context)