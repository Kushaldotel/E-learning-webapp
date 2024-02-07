# course/models.py

from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_courses')

    def __str__(self):
        return self.name

class Review(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])

    def __str__(self):
        return f"{self.course.name} - Rating: {self.rating}"

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrolled_courses')

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.name}"

class Attachment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='course_attachments/')

    def __str__(self):
        return f"{self.course.name} - {self.file.name}"

class Feedback(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='feedbacks')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='course_feedbacks')
    content = models.TextField()

    def __str__(self):
        return f"{self.student.username} - {self.course.name} Feedback"
