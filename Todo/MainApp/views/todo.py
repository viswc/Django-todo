from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from MainApp.models import TodoModel
import json
from django.conf import settings

def index(request):
	reqTodo = TodoModel.objects.all()
	return render(request, "list.json", {
		"todoAll": reqTodo,
	}, content_type="application/json")

def list(request, todo_key):
	reqTodo = TodoModel.objects.filter(primaryKey = todo_key).first()
	if reqTodo is None:
		return HttpResponseRedirect(reverse("TodoApp:index"))
	else:
		return render(request, "todo.json", {
			"todo": reqTodo,
		}, content_type="application/json")

def update(request, todo_key):
	reqTodo = TodoModel.objects.filter(primaryKey = todo_key).first()
	if reqTodo is None:
		return render(request, "outcome.json", {
			"status": False, "key": todo_key,
		}, content_type="application/json")
	else:
		if request.method == "POST":
			reqTodo.title = request.POST["title"]
			reqTodo.description = request.POST["description"]
			reqTodo.save()
			return render(request, "outcome.json", {
				"status": True, "key": todo_key,
			}, content_type="application/json")
		
def delete(request, todo_key):
	reqTodo = TodoModel.objects.filter(primaryKey = todo_key).first()
	if reqTodo is None:
		return render(request, "outcome.json", {
			"status": False, "key": todo_key,
		}, content_type="application/json")
	else:
		reqTodo.delete()
		return render(request, "outcome.json", {
			"status": True, "key": todo_key,
		}, content_type="application/json")
	
def create(request):
	if request.method == "POST":
		reqTodo = TodoModel()
		reqTodo.title = request.POST["title"]
		reqTodo.description = request.POST["description"]
		reqTodo.save()
		return render(request, "outcome.json", {
			"status": True, "key": reqTodo.primaryKey,
		}, content_type="application/json")
	else:
		return render(request, "outcome.json", {
			"status": False, "key": "None",
		}, content_type="application/json")