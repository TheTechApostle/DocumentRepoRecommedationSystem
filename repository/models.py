from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class PasswordResetCode(models.Model):
    email = models.CharField("email", max_length=100)
    otpCode = models.CharField("otp", max_length=50)
    date_created = models.DateTimeField("date_created", auto_now_add=False)


    def __str__(self):
        return f'{self.email} {self.otpCode}'
    

class FolderRepo(models.Model):
    foldername = models.CharField("folder name", max_length=150)
    date_created  = models.DateTimeField("date_created", auto_now_add=False)

    def __str__(self):
        return f'{self.foldername}'
    

class DocRepo(models.Model):
    documentname = models.CharField("folder name", max_length=150)
    date_created  = models.DateTimeField("date_created", auto_now_add=False)

    def __str__(self):
        return f'{self.documentname}'

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class UserDetails(models.Model):
    # myuser = models.CharField("username", max_length=100)
    myuser = models.ForeignKey(User, on_delete=models.CASCADE)
    name =  models.CharField("name",  max_length=100)
    title =  models.CharField("title", max_length=100)
    location =  models.CharField("location", max_length=100)
    status =  models.CharField("status", max_length=200)
    profile = models.ImageField(upload_to='medias')


    def __str__(self):
        return self.name


class FolderNameProject(models.Model):
    foldername = models.CharField('Folder Name', max_length=100)
    parentname = models.CharField('Parent Name', max_length=100)
    folderurl = models.CharField('folder Url', max_length=100)
    date_created  = models.DateTimeField("date_created", auto_now_add=False)




    def __str__(self):
        return self.foldername
    

class uploadFile(models.Model):
    status = (
        ('Approved', 'Approved'),
        ('Not Approved', 'Not Approved')
    )
    filename = models.CharField('File Name', max_length=100)
    nameUploaded = models.ForeignKey(User, on_delete=models.CASCADE)
    foldername = models.CharField('Folder Name', max_length=100)
    parentname = models.CharField('Parent Name', max_length=100)
    folderurl = models.CharField('folder Url', max_length=100)
    #lecturer = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'groups__name': 'Lecturer'})
    lecturer =  models.CharField("lecturer", max_length=100)
    date_created  = models.DateTimeField("date_created", auto_now_add=False)
    docs = models.ImageField(upload_to='repository/static/profile/')
    status = models.CharField(choices=status, max_length=100)



    def __str__(self):
        return self.filename

class MessageBox(models.Model):
    documentName = models.CharField('Document Name', max_length=100)
    messageTitle = models.CharField('Message Title', max_length=100)
    messageText = RichTextField(blank=True, null=True)
    SaveToDraft = models.CharField('Save to Draft', max_length=100)
    mydate  = models.DateTimeField("date_created")
    
    def __str__(self):
        return f'{self.messageTitle}'



class Todos(models.Model):
    documentName = models.CharField('Document Name', max_length=100)
    tasklist = models.CharField("Task List", max_length=200)
    assignee = models.CharField("Task Assignee", max_length=100)
    taskdetails = models.CharField("Task Details", max_length=100)
    dueon = models.DateTimeField()


    def __str__(self):
        return f'{self.tasklist}'


class ChatIncoming(models.Model):
    myuser = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("name", max_length=100)
    mymessage = models.CharField("Message", max_length=200)
    mydate  = models.DateTimeField("date_created")
    profile = models.ImageField(upload_to='profile/')



    def __str__(self):
        return f'{self.mymessage}'
    
class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # file = models.FileField(upload_to='messages/files/', null=True, blank=True)


    def __str__(self):
        return f'From {self.sender.username} to {self.receiver.username}: {self.content[:20]}'
    


class Meeting_Schedule(models.Model):
    title = models.CharField(max_length=255)
    posted = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    finish_time = models.TimeField()
    agenda = models.TextField()
    attendees = models.JSONField(default=list)  # To store multiple attendees
    date_created  = models.DateTimeField("date_created")
    def __str__(self):
        return self.title
    

# class Events(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     description = models.TextField(blank=True)
#     date = models.DateField()

#     def __str__(self):
#         return f"{self.title} on {self.description}"

class Event_schedule(models.Model):
    title = models.CharField(max_length=200)
    event_date = models.DateField()
    event_time = models.TimeField()
    stored_hours = models.CharField(max_length=20)
    attendees = models.CharField('Attendee', max_length=100, blank=True)
    generated_links = models.URLField(blank=True)
    category = models.CharField(max_length=100)
    event_day = models.CharField(max_length=20, blank=True)
    date_created  = models.DateTimeField("date_created", auto_now_add=False)

    def __str__(self):
        return self.title


class ProjectIdea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    keywords = models.TextField()  # Example: "Machine Learning, Web Development, AI"

    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="media/")
    summary = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


    
class formatDocument(models.Model):
    fontSize = models.CharField("Font Size", max_length=50)
    fontColor = models.CharField("Font Color", max_length=50)
    fontFamily = models.CharField("Font Family", max_length=50)
    letterSpacing = models.CharField("Letter Spacing", max_length=50)
    lineSpacing = models.CharField("Line Spacing", max_length=50)
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.fontFamily