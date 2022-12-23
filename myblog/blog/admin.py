from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    save_as = True

    class Meta:
        model = Post
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
