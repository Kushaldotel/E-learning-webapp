from django.contrib import admin

# Register your models here.
from .models import Course, Review, Enrollment, Attachment, Feedback

admin.site.register(Course)
admin.site.register(Review)
admin.site.register(Enrollment)
admin.site.register(Attachment)
admin.site.register(Feedback)