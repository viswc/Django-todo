from django.db import models
import uuid

class TodoModel(models.Model):
	dateCreated = models.DateTimeField(auto_now_add = True)
	dateModified = models.DateTimeField(auto_now = True)
	primaryKey = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

	title = models.CharField(max_length = 512, default="TodoTitlePlaceholder")
	description = models.CharField(max_length = 1024, null=True, blank = True)

# Create your models here.
