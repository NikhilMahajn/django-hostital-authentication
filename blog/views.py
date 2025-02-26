from django.shortcuts import render,redirect
from django.contrib import messages
from user.models import Users
from django.http import JsonResponse
from django.urls import reverse
from user.views import index
from .models import Blog


# Create your views here.

def blog(request,id,bid=None):
	try:
		user = Users.objects.filter(id=id).first()
		blogs = Blog.objects.filter(doc_id=id,uploaded=False)
	except Exception as e:
		return JsonResponse({"message",e})
	return render(request,'blog.html',{"user":user,"blogs":blogs,"blogClick":None})

def savedraft(request):
	if request.method == 'POST':
		try:
			# id = request.POST.get('id')
			id = request.user.id
			bid = request.POST.get('blogId')
			title = request.POST.get('title')
			text = request.POST.get('text')
			img = request.FILES.get('img')
			summary = request.POST.get('summary')
			category = request.POST.get('category')
			blog = None
			if bid:
				blog = Blog.objects.filter(id=bid).first()

			if blog:
				print("blog present")
				blog.title = title
				blog.summary = summary
				blog.img = img
				blog.category = category
				blog.text = text

				blog.save()

				return JsonResponse({"message": "Draft updated successfully!"})
			else:
				user  = Users.objects.filter(id=id).first()
				author = user.first_name + " " + user.last_name
				Blog.objects.create(doc_id=id,title=title,text=text,author=author,img=img,summary=summary,category=category,uploaded=False)
				return JsonResponse({"message": "Draft saved successfully!"})

		except Exception as e:
			print(e)
			return JsonResponse({'message':e})
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
	try:
		if request.method == 'POST':
			id = request.POST.get('id')
			blogId = request.POST.get('blogId')
			img = request.FILES.get('image')

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
	except Exception as e:
		return JsonResponse({"message":e})
	return render(request,'blog.html')

def delete(request):
	if request.method == 'POST':
		blogId = request.POST.get('blogId')
		blog = Blog.objects.filter(id=blogId).first()
		blog.delete()
		return JsonResponse({"message":"blog deleted successfully"})
	return render(request,'blog.html')


	
		
	
