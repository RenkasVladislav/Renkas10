from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import CommentForm
from django.views.decorators.http import require_POST
def post_list(request):
    posts = Post.published.all()
    return render(request,
        'blog/post/list.html',
        {'posts': posts})
def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    return render(request, 'blog/post/detail.html', {'post': post, 'comments': comments,
'form': form})

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    return render(request, 'blog/post/comment.html', {'post': post, 'form': form,
'comment': comment})

               