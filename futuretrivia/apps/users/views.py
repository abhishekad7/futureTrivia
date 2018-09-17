from django.shortcuts import render
from django.http import *
from django.urls import reverse
from .user_validation import *
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import UserDetails
from apps.trivia.models import Trivia
import pytz, datetime


# Create your views here.


def userLogin(request):

	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('userprofile', kwargs={'username':request.user.username}))

	if request.method == "POST":
		context = {"success": True}
		errors = []
		username = request.POST.get("username").strip().lower()
		password = request.POST.get("password")

		u = get_user(username)

		if not u:
			errors.append("No Account Found")
		elif not u.is_active:
			errors.append("Acount is deactivated. Contact us to activate it.")
		else:
			#print(u)
			u=authenticate(username=u.username, password=password)
			if not u:
				errors.append("Wrong Password")


		if errors:
			context["success"]=False
			context["errors"]=errors
			return JsonResponse(context)

		login(request, u)

		return JsonResponse(context)

	return render(request, 'users/login.html', {})

def userLogout(request):
	logout(request)
	return HttpResponseRedirect(reverse('userlogin'))


def userSignup(request):

	#print(request.user.is_authenticated)
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse('userprofile', kwargs={'username':request.user.username}))

	if request.method == "POST":
		context = {"success": True}
		errors = []
		email = request.POST.get("email").strip().lower()
		username = request.POST.get("username").strip().lower()
		password = request.POST.get("password")

		if not validate_username(username):
			errors.append("Invalid Username")
		elif user_exists(username):
			errors.append("Username already taken")

		if not check_email_dns(email):
			errors.append("Invalid Email")
		elif user_exists(email):
			errors.append("Email already taken")

		if not validate_password(password):
			errors.append("Password must be 8 characters long")

		if errors:
			context["success"]=False
			context["errors"]=errors
			return JsonResponse(context)

		u = User.objects.create(username = username, email = email)
		u.set_password(password)
		u.save()

		ud = UserDetails.objects.create(user = u)

		login(request, u)

		return JsonResponse(context)

	return render(request, 'users/register.html', {})

def dashboard(request):

	return render(request, 'users/dashboard.html', {})


def userProfile(request, username):
	user = User.objects.filter(username=username).first()
	context = {"exist":False, "active": False}
	if user:
		context["exist"]=True
		if user.is_active:
			context["active"]=True
			context["user"]=user



	return render(request, 'users/userProfile.html', context)



def registerContest(request):
	context={"success": False}

	if not request.user.is_authenticated:
		context["error"] = "Sign in to Register"
		return JsonResponse(context)

	code = request.GET.get("code")
	trivia = Trivia.objects.filter(code=code).first()
	
	if not trivia:
		context["error"] = "Contest Not Found"
		return JsonResponse(context)

	now=datetime.datetime.now().replace(tzinfo=pytz.utc)
	portal_endtime = trivia.start_time + datetime.timedelta(seconds=trivia.portal_duration)

	if now > portal_endtime:
		context["error"] = "Registration ended"
		return JsonResponse

	request.user.userdetails.trivias.add(trivia)
	context["success"] = True

	return JsonResponse(context)
	