from django.shortcuts import render, redirect
from evoting.forms import *
from evoting.models import *
from organiser_app.models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from evoting.tokens import account_activation_token
from django.core.mail import EmailMessage, send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

# Create your views here.


def base(request):
    return render(request, 'voters/base.html')


def home(request):
    elections = Election.objects.all()
    if str(request.user) != 'AnonymousUser':
        user_type = User.objects.get(username=request.user).first_name
    else:
        user_type = 'null'
    return render(request, 'voters/home.html', {'elections': elections, 'username': request.user, 'user_type': user_type})


def profile(request):
    return render(request, 'voters/profile.html', {'username': request.user.username})


def register(request):

    registered = False
    if request.method == "POST":
        registration_form1 = Registration_form1(request.POST)
        registration_form2 = Registration_form2(request.POST)

        if registration_form1.is_valid() and registration_form2.is_valid():
            voter_id = request.POST['voterId']
            voter_id_list = Voter.objects.values_list('voter_id', flat=True)

            if voter_id in voter_id_list:
                voter = Voter.objects.get(voter_id=voter_id)
                if request.POST['email'] == voter.voter_email and\
                        request.POST['fullname'] == voter.voter_name:

                    reg_form1 = registration_form1.save()
                    reg_form1.is_active = False
                    reg_form1.set_password(reg_form1.password)
                    reg_form1.save()

                    reg_form2 = registration_form2.save(commit=False)

                    reg_form2.user = reg_form1
                    reg_form2.user.is_active = False

                    reg_form2.save()

                    current_site = get_current_site(request)
                    mail_subject = 'Verify your email.'
                    message = render_to_string('voters/acc_active_email.html', {
                        'user': reg_form2.user,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(reg_form2.user.pk)).decode(),
                        'token': account_activation_token.make_token(reg_form2.user),
                    })
                    to_email = reg_form1.email
                    email = EmailMessage(
                        mail_subject, message, to=[to_email]
                    )
                    email.send()

                    registered = True

                    Voters_Profile.objects.get(voterId=voter_id).user.first_name = 'Voter'

                else:
                    messages.error(request, f'(Email Id) or (fullname) or (Date of Birth) does\'nt'
                                            f' matches with the given Voter Id')
            else:
                messages.error(request, f'Voter with the given Voter Id does not exist!!')

        else:
            messages.error(request, (registration_form1.errors, registration_form2.errors))
            print(registration_form1.errors, registration_form2.errors)
    else:
        registration_form1 = Registration_form1()
        registration_form2 = Registration_form2()

    if not registered:
        return render(request, 'voters/register.html',
                      {'reg_form1': registration_form1, 'reg_form2': registration_form2})

    else:
        logout(request)
        return render(request, 'voters/login.html',
                      {'registered_message': 'We have sent a mail to the registeered mail.'
                       ' Please click that link to activate your account and then login', 'USER': 'voter'})


def user_acc_activation(request):
    return render(request, 'voters/acc_activate.html')


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
        message = {'acc_confirmation_message': 'Thanks for activating your account. Now you can login to your account.'}
        return render(request, 'voters/home.html', message)
    else:
        err_message = {'acc_confirmation_message': 'Activation link is invalid!'}
        return render(request, 'voters/home.html', err_message)


# ======================================================================================================================

def voter_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user and User.objects.get(username=username).first_name == '':
            if user.is_active:
                login(request, user)
                a = User.objects.get(username=username)
                print(a.first_name)
                return render(request, 'voters/home.html',
                              {'username': username, 'user_type': User.objects.get(username=username).first_name})

            else:
                return HttpResponse('account not active')

        else:
            messages.error(request, f'Invalid login details!')
            print()
            return redirect(reverse('evoting-voter-login'))
    else:
        return render(request, 'voters/login.html', {'USER': 'voter'})


def orgainser_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user and User.objects.get(username=username).first_name == 'Organiser':
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('organiser_app:mainpage'))

            else:
                return HttpResponse('account not active')

        else:
            messages.error(request, f'Invalid login details!')
            return redirect(reverse('evoting-organiser-login'))
    else:
        return render(request, 'voters/login.html', {'USER': 'organiser'})


def user_logout(request):
    logout(request)
    return redirect('evoting-home')


def send_email(request):
    send_mail('Password Reset', 'Click the below link to reset your password.', 'sriram.nandala@gmail.com',
              ['neelakantasriram.n17@iiits.in'])

    return HttpResponse('Email Sent!!')


def print_username(request):
    voter = Voter.objects.get(voter_id='TS2018102')
    userx = request.user
    print(type(userx))
    # username = User.objects.values_list('username', flat=True)
    return HttpResponse(str(userx))


def test_ajax(request):
    return render(request, 'voters/test.html')
