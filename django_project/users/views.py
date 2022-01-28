from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
import logging
import yagmail
from django.conf import settings


logger = logging.getLogger("django")


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')

            #  This will send sign up congratulations email
            
            receiver = request.POST.get('email')
            subject = 'Thank you for registering your profile!'
            contents = '''
            Thank you for taking the time to visit my site and set up a profile, I hope you like it!
            '''
            yag = yagmail.SMTP(user=settings.EMAIL_HOST_USER, password=settings.EMAIL_HOST_PASSWORD)
            yag.send(to=receiver, subject=subject, contents=contents)

            # Redirect success message
            messages.success(request, f'Your account creation has been successful, you can now login!')
            
            logger.info("A new user has successfully registered a new profile.")
            logger.debug(request)
            return redirect('login')
    else:
        form = UserRegisterForm()
        logger.info("A user has visited the sites registration page.")
        logger.debug(request)
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account details have been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        logger.info("A user has visited the sites user_profile page.")
        logger.debug(request)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
        

    return render(request, 'users/profile.html', context )


    