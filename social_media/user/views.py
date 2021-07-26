from django.contrib import messages
from account.models import Post
from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
        caption = request.POST.get('caption')
        image = request.FILES.get('image')
        user = request.user
        user = Post(caption = caption, image=image, user=user)
        user.save()
        messages.success(request, "Post done successfully")
    return render(request, 'user/feed.html')