from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Test(models.Model):
	userID = models.ForeignKey(User,on_delete=models.CASCADE)
	ageCategory = testID = models.CharField(max_length=20)
	testID = models.CharField(max_length=3)
	dateTested = models.DateTimeField(default=timezone.now)
	result = models.CharField(max_length=3)

	def __str__(self):
		return self.result
# Create your models here.

class chek(models.Model):
    date = models.DateTimeField(auto_now_add=False, blank=True, null=True)