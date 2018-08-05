from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm
# Create your views here.
@login_required(login_url='accounts/login')
def home(request):
	return render(request,'home.html')

@login_required(login_url='/accounts/login')
def new_profile(request):
	current_user = request.user
	if request.method == 'POST':
		form = NewProfileForm(request.POST,request.FILES, instance=request.user.profile)
		if form.is_valid():
			form.save()
			return redirect('home')

	else:
			form = NewProfileForm()
	return render(request, 'new_profile.html',{"form":form })

