from django.contrib import admin
from todolists.models import ToDoListModel

@admin.register(ToDoListModel)
class todolistModelAdmin(admin.ModelAdmin):
    list_display = ['checkbox',
                    'content',
                    'created_by',
                    'created_at',
                    ]

    list_filter = ('created_at',
                'checkbox',
                )
    search_fields = ('id',
                    'todolist_writer__username',
                    'content'
                    )
    search_help_text = '글 번호, 작성자, 내용으로 검색이 가능합니다.'
    readonly_fields = ('created_at',)