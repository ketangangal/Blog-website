from django.contrib import admin
from .models import *
from .models import textEditor
from django.db import models
from tinymce.widgets import TinyMCE

  
class textEditorAdmin(admin.ModelAdmin):
   list_display = ["title"]
   formfield_overrides = {
   models.TextField: {'widget': TinyMCE()}
   }


admin.site.register(textEditor, textEditorAdmin)
admin.site.register(BlogPost)
admin.site.register(Comment)
admin.site.register(Profile)