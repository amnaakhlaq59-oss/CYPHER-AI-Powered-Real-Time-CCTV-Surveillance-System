from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm 

def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST) 
        if form.is_valid():
            user = form.save()
            
            # --- FIX: Specify the backend explicitly ---
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            
            return redirect('dashboard') 
    else:
        form = CustomUserCreationForm()
        
    return render(request, "signup.html", {"form": form})

# --- ADDED MISSING VIEW ---
def registration_successful(request):
    return render(request, "registration_successful.html")