from django.shortcuts import render
from django.http import JsonResponse
from .models import ContactMessage  # Import your ContactMessage model

# Existing view function
def index(request):
    return render(request, 'home.html')

# New view function for handling form submission
def submit_contact_form(request):
    if request.method == 'POST':
        # Handle form submission logic here
        # For demonstration, let's assume the form data is sent as JSON and we're returning a JSON response
        form_data = request.POST
        name = form_data.get('name')
        email = form_data.get('email')
        subject = form_data.get('subject')
        message = form_data.get('message')

        # Create a new ContactMessage object and save it to the database
        ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)

        # Return a JSON response indicating success
        return JsonResponse({'success': True})
    else:
        # Return a JSON response indicating failure if the request method is not POST
        return JsonResponse({'success': False, 'error': 'Invalid request method'})
