from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Post

# Create your views here.
def home(request):
    if request.method == 'POST':
        caption = request.POST.get('caption')
        image = request.FILES.get('image')
        user = request.user
        user = Post(caption = caption, image=image, user=user)
        user.save()
        messages.success(request, "Post done successfully")

    allPost = Post.objects.all()
    data = {
        'posts': allPost
    }
    return render(request, 'user/feed.html', data)


def delete_view(request, pk):
    post = Post.objects.get(id = pk)
    post.delete()
    messages.info(request, "Post deleted")
    return redirect("home_page")