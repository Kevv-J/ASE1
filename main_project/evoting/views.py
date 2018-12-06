from django.shortcuts import render, redirect
from .forms import *
from .models import *
from organiser_app.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage, send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# Create your views here.

def home(request):
    elections = Election.objects.all()
    context = {'elections':elections}
    return render(request, 'home.html', context=context)


def profile(request):
    return render(request, 'profile.html', {'username': request.user.username})

def register(request):

    registered = False

    if request.method == "POST":
        registration_form1 = Registration_form1(request.POST)
        registration_form2 = Registration_form2(request.POST)

        if registration_form1.is_valid() and registration_form2.is_valid():
            voter_id = request.POST['voterId']
            voter_id_list = Voter.objects.values_list('voter_id', flat=True)

            print(voter_id, voter_id_list)

            if voter_id in voter_id_list:


                reg_form1 = registration_form1.save()
                reg_form1.is_active = False
                reg_form1.set_password(reg_form1.password)
                reg_form1.save()

                reg_form2 = registration_form2.save(commit=False)

                reg_form2.user = reg_form1
                reg_form2.user.is_active = False
                reg_form2.activation = 'False'


                reg_form2.save()


                current_site = get_current_site(request)
                mail_subject = 'Verify your email.'
                message = render_to_string('acc_active_email.html', {
                    'user': reg_form2.user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(reg_form2.user.pk)).decode(),
                    'token': account_activation_token.make_token(reg_form2.user),
                })
                print(message)
                to_email =reg_form1.email
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()


                registered = True


                print('form saved successfully!!')
            else:
                messages.error(request, f'Invalid details given!!')

        else:
            print(registration_form1.errors, registration_form2.errors)
    else:
        registration_form1 = Registration_form1()
        registration_form2 = Registration_form2()

    if not registered:
        return render(request, 'register.html', {'reg_form1': registration_form1, 'reg_form2': registration_form2})

    else:
        logout(request)
        return redirect('evoting-login')

def user_acc_activation(request):
    return render(request, 'acc_activate.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


# ======================================================================================================================

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('evoting-home'))

            else:
                return HttpResponse('account not active')

        else:
            messages.error(request, f'Invalid login details!')
            return redirect(reverse('evoting-login'))
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('evoting-home')


def send_email(request):
    send_mail('Password Reset', 'Click the below link to reset your password.', 'sriram.nandala@gmail.com',
              ['neelakantasriram.n17@iiits.in'])

    return HttpResponse('Email Sent!!')


def print_username(request):
    activation_status = User.objects.filter(username='strange321')
    print(activation_status)
    username = User.objects.values_list('username', flat=True)
    return HttpResponse(activation_status)
