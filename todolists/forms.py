from django.core.exceptions import ValidationError
from django.forms import forms
from todolists.models import ToDoList


class ToDoListBaseForm(forms.ModelForm):

    class Meta:
        model = ToDoList
        fields = '__all__'


class ToDoListCreateForm(ToDoListBaseForm):
    class Meta(ToDoListBaseForm.Meta):
        fields = ['checkbox', 'content', 'worker',
                  'deadline', 'content_detail']

    # 유효성 검사
    def clean_content(self):
        data = self.cleaned_data['content']
        if 'content' is None:
            raise ValidationError('올바르지 않은 값입니다.')

        return data
