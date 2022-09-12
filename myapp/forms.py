from django.forms import ModelForm
from myapp.models import ToDo

class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = ['title', 'status','priority']