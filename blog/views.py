from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
import csv
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def csv_test_export(request):
    #Get all Data from Posts
    posts = Post.objects.all()
    
    csv_export_date = datetime.strftime(timezone.now(), '%Y-%m-%d-%H:%M:%s')

    #Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="csv_' + csv_export_date + '.csv"'

    response.write(u'\ufeff'.encode('utf8'))
    write = csv.writer(response)
    write.writerow(['title', 'text', 'created_at', 'published_date'])

    for post in posts:
        write.writerow([post.title, post.text, post.created_at, post.published_date])

    return response