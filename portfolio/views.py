from django.shortcuts import render
from django.http import JsonResponse
from .models import ContactMessage  # Import the ContactMessage model

def submit_contact_form(request):
    if request.method == 'POST':
        form_data = request.POST
        name = form_data.get('name')
        email = form_data.get('email')
        subject = form_data.get('subject')
        message = form_data.get('message')

        # Create a new ContactMessage instance and save it to the database
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )

        # Return a JSON response indicating success
        return JsonResponse({'success': True})
    else:
        # Return a JSON response indicating failure if the request method is not POST
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
