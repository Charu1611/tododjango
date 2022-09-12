from django.db import models
from django.contrib.auth.models import User

class ToDo(models.Model):
    status_choices = [
    ('C', 'Completed'),
    ('F', 'Pending'),
]
    priority_choices =[
    ('1','1️'),
    ('2','2️'),
    ('3','3️'),
    ('4','4️'),
    ('5','5️'),
    ('6','6️'),
    ('7','7️'),
    ('8','8️'),
    ('9','9️'),
    ('10','10'),
]
    title = models.CharField(max_length=50)
    status = models.CharField(max_length=2 , choices=status_choices)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # dforeign key mtlb dusri table se user utha rhe h, cascade mtlb user delete hote he uski todo delete
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2 , choices=priority_choices)

    # models ko admin.py me register krna hota h taki panel pr show kre