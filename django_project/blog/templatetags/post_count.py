from blog.models import Post
from django import template
register = template.Library()


@register.simple_tag(name='post_count')
def post_count():
    post_count = Post.objects.all().count()
    
    return post_count