from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


def home_view(request):
 return render(request=request,template_name='index.html')

def about_view(request):
 return render(request=request,template_name='about.html')


def blog_view(request):
 return render(request=request,template_name='blog.html')



def contact_view(request):
    if request.method == 'POST':
        contact_name = request.POST.get('contact_name')
        contact_email = request.POST.get('contact_email')
        contact_subject = request.POST.get('contact_subject')
        contact_message = request.POST.get('contact_message')

        # Ma'lumotlarni tekshirish
        if not contact_name or not contact_email or not contact_subject or not contact_message:
            print(f"contact_name: {contact_name}, contact_email: {contact_email}, contact_subject: {contact_subject}, contact_message: {contact_message}")
            return HttpResponse('All fields are required.', status=400)

        # Konsolga chop etish
        print(contact_name, contact_email, contact_subject, contact_message)
        print("Siz POST request yubordingiz")

        # Ma'lumotlarni saqlash
        contact = Contact(name=contact_name, email=contact_email, subject=contact_subject, message=contact_message)
        contact.save()

        # Ma'lumot muvaffaqiyatli saqlangandan so'ng, tasdiqlash sahifasini ko'rsatish
        return HttpResponse('Xabaringiz jonatildi.')
    
    # Agar so'rov metodi POST bo'lmasa, forma sahifasini ko'rsatish
    return render(request, 'contact.html')