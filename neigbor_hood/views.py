from django.shortcuts import render,redirect,get_object_or_404,render_to_response
from django.contrib.auth.decorators import login_required
from .forms import NewProfileForm,NewNeigbor_hood_Form,New_Business_Form,NewPostForm,NewCommentForm
from .models import UserProfile,Neighbor_hood,Business,Post,Comments
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='accounts/login')
def home(request):
	neighbor_hood=Neighbor_hood.objects.filter()
	return render(request,'home.html',locals())

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

@login_required(login_url='/accounts/login')
def new_neigbor_hood(request):
	current_user = request.user
	if request.method == 'POST':
		form =NewNeigbor_hood_Form(request.POST,request.FILES)
		if form.is_valid():
			location = form.save(commit=False)
			location.user = current_user
			location.save()
			request.user.profile.neighbor_hood=location
			request.user.profile.save()
			return redirect('home')
	else:
			form = NewNeigbor_hood_Form()
	return render(request, 'new_location.html',{"form":form })

@login_required(login_url='/accounts/login')
def new_business(request):
	current_user = request.user
	if request.method == 'POST':
		form =New_Business_Form(request.POST,request.FILES)
		if form.is_valid():
			location = form.save(commit=False)
			location.user = current_user
			location.save()
			return redirect('home')
	else:
			form = New_Business_Form()
	return render(request, 'new_business.html',{"form":form })

	
def search_results(request):
	if "name" in request.GET and request.GET["name"]:
		search_term = request.GET.get("name")
		print(search_term)
		searched_business = request.user.profile.neighbor_hood.hoodbus.filter(name__icontains=search_term)
		message = f"{search_term}"
		return render(request,'search.html',{"message":message,"businesses":searched_business})
	else:
		message='You havent searched for any term'
		return render(request, 'search.html',locals())	
def hood_business(request):
	return render(request,'hood_business.html')

@login_required(login_url='/accounts/login')
def follow_hood(request,hood_id):
	UserProfile.objects.update(neighbor_hood=hood_id)
	return redirect('home')


@login_required(login_url='/accounts/login')
def hoods(request,hooder_id):
	neighbor_hood=Neighbor_hood.objects.filter(id=hooder_id) 

	return render(request,'hood_follow.html',locals())

@login_required(login_url='/accounts/login')
def neigbor_hood(request):
	neighbor_hood=Neighbor_hood.objects.all()
	return render(request,'hood_follow.html',locals())

@login_required(login_url='/accounts/login')
def hooder(request,post_id=None):
	for hood in Neighbor_hood.objects.all():
		neigbor=hood.hood.all()
		comments=Comments.objects.all()
		posts=hood.hoodpost.all()
		form = NewCommentForm()
		if post_id:
			post = get_object_or_404(Post, pk=post_id)
			if request.method == 'POST':
				commentform = NewCommentForm(request.POST)
				if commentform.is_valid():
					article = commentform.save(commit=False)
					article.user = request.user
					article.post = post
					article.save()
					return redirect('hood')
		else:
			form = NewCommentForm()

	
		return render(request,'hood.html',locals())	

@login_required(login_url='/accounts/login')
def new_post(request):
	current_user = request.user
	if request.method == 'POST':
		form = NewPostForm(request.POST,request.FILES)
		if form.is_valid():
			article = form.save(commit=False)
			article.user = current_user
			article.save()
			request.user.profile.hoodpost=article
			request.user.profile.save()
			return redirect('home')
	else:
			form = NewPostForm()
	return render(request, 'new_post.html',{"form":form })
	