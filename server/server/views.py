from django.shortcuts import render , redirect
from .forms import UserImageForm
from .models import UserImage

def upload_image(request):
    if request.method == 'POST':
        form = UserImageForm(request.POST , request.FILES)
        if form.is_valid():
            user_image = form.save(commit=False)
            user_image.file_path = user_image.image.url
            user_image.save()
            return redirect('Succes')
        
    else:
        form = UserImageForm()
    return render(request , 'upload_image.html' , {'form' : form})