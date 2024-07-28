from django.shortcuts import render , get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,\
PageNotAnInteger
from django.http import Http404

def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    
    post = get_object_or_404(Post,
                        id=id,
                        status=Post.Status.PUBLISHED,
                        slug=post,
                        publish__year=year,
                        publish__month=month,
                        publish__day=day)
    return render(request,
            'blog/post/detail.html',
            {'post': post})

# Create your views here.

def post_list(request):
    post_list = Post.published.all()
    # Pagination with 3 posts per page
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)

    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request,
            'blog/post/list.html',
            {'posts': posts})