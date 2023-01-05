from django.contrib import admin
from django.utils.safestring import mark_safe
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
    list_display = ('pk', 'title', 'slug', )
    list_display_links = ('pk', 'slug', )
    search_fields = ('title', 'slug', )
    empty_value_display = "-пусто-"


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('pk', 'title', 'slug', )
    list_display_links = ('pk', 'slug', )
    search_fields = ('title', 'slug', )
    empty_value_display = "-пусто-"


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('pk', 'title', 'author', 'created_at', 'category', 'get_photo')
    list_display_links = ('pk', 'title')
    search_fields = ('title', 'author', )
    list_filter = ('author', 'created_at', 'category', 'tags')
    fields = ('title', 'slug', 'author', 'content', 'created_at', 'img', 'get_photo', 'views', 'category', 'tags', )
    #  какие поля не редактируемые
    readonly_fields = ('get_photo', 'created_at', 'views', )
    save_on_top = True

    def get_photo(self, obj):
        if obj.img:
            return mark_safe(f'<img src="{obj.img.url}" width="50">')
        return '-'

    get_photo.short_description = 'Миниатюра'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
