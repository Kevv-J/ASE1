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
from django.shortcuts import get_object_or_404
from . import decoraters


def base(request):
    return render(request, 'voters/base.html')


@decoraters.voter_home
def home(request):
    elections = Election.objects.all()
    context = {'elections': elections, 'username': request.user}
    return render(request, 'voters/home.html', context = context)


@decoraters.voter_login_required
def profile(request):
    return render(request, 'voters/profile.html', {'username': request.user.username})


@decoraters.user_not_logged_in
def register(request):

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
                    reg_form2.region = voter.voter_region
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
                    print(message)
                    to_email = reg_form1.email
                    email = EmailMessage(
                        mail_subject, message, to=[to_email]
                    )
                    email.send()

                    messages.success(request, f'We have sent a mail to the registered mail.'
                                              f' Please click that link to activate your account and then login')
                    logout(request)
                    return redirect('evoting-voter-login')

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

    return render(request, 'voters/register.html', {'reg_form1': registration_form1, 'reg_form2': registration_form2})


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
        messages.success(request, f'Thanks for activating your account. Now you can login to your account.')

    else:
        messages.error(request, f'Activation link is invalid!')

    return render(request, 'voters/home.html')


# ======================================================================================================================
@decoraters.user_not_logged_in
def voter_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            user_objs = User.objects.filter(username=username)
            if hasattr(user_objs.first(), 'voters_profile'):
                
                if user.is_active:
                    login(request, user)
                    return redirect('evoting-home')
                else:
                    return HttpResponse('account not active')
    
            else:
                messages.error(request, f'Invalid Login details')

        else:
            messages.error(request, f'Invalid Login details')

        return redirect(reverse('evoting-voter-login'))
            
    else:
        return render(request, 'voters/login.html', {'USER': 'voter'})


@decoraters.user_not_logged_in
def orgainser_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if not hasattr(username, 'voters_profile'):

                login(request, user)
                return redirect('organiser_app:mainpage')

            else:
                messages.error(request, f'Invalid Login details')

        else:
            messages.error(request, f'Invalid Login details')

        return redirect(reverse('evoting-organiser-login'))

    else:
        return render(request, 'voters/login.html', {'USER': 'organiser'})


@decoraters.user_login_required
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

def election(request,pk):
    print(Voters_Profile.objects.values_list('user'))
    user = Voters_Profile.objects.get(user = request.user)
    region = user.region


    candidates = Candidate_election.objects.filter(election = pk)
    candidates = {candidate.candidate for candidate in candidates}
    candidates = {candidate for candidate in candidates if candidate.candidate_region in region}
    print(candidates)

    candidates_new = []
    region_options = {
        '0': 'AndhraPradesh',
        '1': 'Bihar',
        '2': 'karnataka',
        '3': 'Tamilnadu',
        '4': 'Kerela',
        '5': 'UttarPradesh',
        '6': 'WestBengal',
        '7': 'MadhyaPradesh',
        '8': 'Haryana',
        '9': 'Assam'
    }

    region = region_options[region]
    for candidate in candidates:
        candidates_new.append([candidate.candidate_name, candidate.candidate_id])
    result_region = {'region': region, 'candidates_new': candidates_new,'user':user}
    return render(request, "trail/index6.html", result_region)

def candidate_details(request,pk):
    template_name='trail/candidate_detail.html'
    candidate=get_object_or_404(Candidate,candidate_id=pk)
    region_options = {
        '0': 'AndhraPradesh',
        '1': 'Bihar',
        '2': 'karnataka',
        '3': 'Tamilnadu',
        '4': 'Kerela',
        '5': 'UttarPradesh',
        '6': 'WestBengal',
        '7': 'MadhyaPradesh',
        '8': 'Haryana',
        '9': 'Assam'
    }
    print(str(candidate.candidate_dob))
    candidate.candidate_region = region_options[candidate.candidate_region]
    dob = str(candidate.candidate_dob)
    return render(request,template_name,{'object':candidate,'dob':dob})