from django.contrib import admin
from .models import  Transaction ,Wallet ,Question, Answer,UserID


admin.site.register(Transaction)
admin.site.register(Wallet)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(UserID) 


