from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import Users
from django.http import JsonResponse
from django.urls import reverse
from user.views import index
from .models import Blog


# Create your views here.

def blog(request,id,bid=None):
	user = Users.objects.filter(id=id).first()
	blogs = Blog.objects.filter(doc_id=id,uploaded=False)
	return render(request,'blog.html',{"user":user,"blogs":blogs,"blogClick":None})

def savedraft(request):
	if request.method == 'POST':
		id = request.POST.get('id')
		title = request.POST.get('title')
		text = request.POST.get('text')
		img = request.FILES.get('img')
		summary = request.POST.get('summary')
		category = request.POST.get('category')
		print(id)
		
		user  = Users.objects.filter(id=id).first()
		author = user.first_name + " " + user.last_name
		print(author)
		Blog.objects.create(doc_id=id,title=title,text=text,author=author,img=img,summary=summary,category=category,uploaded=False)
		# # messages.success(request,"draft saved successfully")
		return JsonResponse({"message":"draft saved successfully"})
	return render(request,'blog.html')


def loadDraft(request, id, blogId):
    user = Users.objects.filter(id=id).first()  # Ensure user is a single object
    blog = Blog.objects.filter(id=blogId).first()  # Load clicked blog
    blogs = Blog.objects.filter(doc_id=id,uploaded=False)  # No need for `.values()`
    
    return render(request, 'blog.html', {
        "user": user,
        "blogs": blogs,
        "blogClick": blog
    })

def publish(request):
	if request.method == 'POST':
		print("publishingg............")
		id = request.POST.get('id')
		blogId = request.POST.get('blogId')
		img = request.FILES.get('image')
		print(img)

		if blogId:
			blog = Blog.objects.filter(id=blogId).first()
			blog.img = img
			blog.uploaded = True
			
			blog.save()
			return JsonResponse({"message":"blog published successfully"})

		else:
			title = request.POST.get('title')
			text = request.POST.get('text')
			summary = request.POST.get('summary')
			category = request.POST.get('category')
			user  = Users.objects.filter(id=id).first()
			author = user.first_name + " " + user.last_name
			Blog.objects.create(doc_id=id,title=title,text=text,author=author,img=img,summary=summary,category=category,uploaded=True)

			return JsonResponse({"message":"blog published successfully"})
	print("not post request")
	return render(request,'blog.html')

def delete(request):
	if request.method == 'POST':
		blogId = request.POST.get('blogId')
		blog = Blog.objects.filter(id=blogId).first()
		blog.delete()
		return JsonResponse({"message":"blog deleted successfully"})
	return render(request,'blog.html')


	
		
	
