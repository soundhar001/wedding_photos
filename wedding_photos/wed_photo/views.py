from django.shortcuts import render
from .models import FormData


# Create your views here.
def form(request): 
    if request.method == 'POST':
        Name = request.POST.get('name')
        Email = request.POST.get('email')
        Phone = request.POST.get('phone')
        File = request.FILES.get('file')

        # Create a new FormData object and save it
        form_data = FormData(name=Name, email=Email, phone=Phone, file=File)
        form_data.save()
        print(Name,Email,Phone)

        return render(request, 'form.html')

    return render(request, 'form.html')