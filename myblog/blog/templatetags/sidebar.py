from django import template
from blog.models import Post, Tag


register = template.Library()


@register.inclusion_tag('blog/sidebar_tpl.html')
def get_most_popular(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]  # noqa
    return {
        'posts': posts,
    }


@register.inclusion_tag('blog/tags_tpl.html')
def get_tags():
    tags = Tag.objects.all()  # noqa
    return {
        'tags': tags,
    }
