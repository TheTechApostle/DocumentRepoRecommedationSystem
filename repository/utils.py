from  .models import *
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.contrib.auth.models import User
from django.db.models import Q, Max
from django.utils.timezone import now

def get_nav_context(request=None):
    user = request.user

    # Group by conversation (unique pair of users)
    conversations = Message.objects.filter(
        Q(sender=user) | Q(receiver=user)
    ).values('sender', 'receiver').annotate(
        latest=Max('timestamp')
    ).order_by('-latest')[:10]

    partner_ids = set()
    for convo in conversations:
        partner_id = convo['receiver'] if convo['sender'] == user.id else convo['sender']
        partner_ids.add(partner_id)
        if len(partner_ids) == 4:
            break

    # Fetch latest message per partner
    recent_chats = []
    for pid in partner_ids:
        message = Message.objects.filter(
            Q(sender=user, receiver_id=pid) | Q(sender_id=pid, receiver=user)
        ).order_by('-timestamp').first()
        if message:
            recent_chats.append(message)

    allFilesCount = uploadFile.objects.all().count()
    theFile = uploadFile.objects.order_by('-date_created')[:3]
    allUsers = User.objects.all().count()
    projectFolder = FolderRepo.objects.count()
    lecturer_group = Group.objects.filter(name="Lecturer").first()
    lecturers = lecturer_group.user_set.all() if lecturer_group else [] 
    allDocuments = uploadFile.objects.all()
    allCount = uploadFile.objects.all().count()
   
    files = uploadFile.objects.order_by('-date_created')[:1]
    filesx = uploadFile.objects.order_by('-date_created')[:1].count()
    filesM = Meeting_Schedule.objects.order_by('-date_created')[:1]
    filesMx = Meeting_Schedule.objects.order_by('-date_created')[:1].count()
    mycounted = filesx+ filesMx
    files_with_datesM = []
    for fileM in filesM:
        # theId = FolderNameProject.objects.get(foldername=file.foldername)
        # myid = theId.id
        first_letterM = str(fileM.posted)
        firstLM = first_letterM[0]
        # Extract month and day from the date_created field
        month = fileM.date_created.strftime("%b")  # Full month name (e.g., "August")
        day = fileM.date_created.strftime("%d") 
        time = fileM.date_created.strftime("%I:%M %p")   # Day with leading zero (e.g., "30")

        # Append to the list as a dictionary
        files_with_datesM.append({
            'fileM': fileM,
            'firstlM':firstLM.upper(),
            # 'myid': myid,
            'month': month,
            'day': day,
            'time' : time
        })
    # Create a list to store the month and day for each file
    files_with_dates = []
    theId = []
    file = []
    for file in files:
        theId = FolderNameProject.objects.get(foldername=file.foldername)
        myid = theId.id
        first_letter = str(file.nameUploaded)
        firstL = first_letter[0]
        # Extract month and day from the date_created field
        month = file.date_created.strftime("%b")  # Full month name (e.g., "August")
        day = file.date_created.strftime("%d") 
        time = file.date_created.strftime("%I:%M %p")   # Day with leading zero (e.g., "30")

        # Append to the list as a dictionary
        files_with_dates.append({
            'file': file,
            'firstl':firstL.upper(),
            'myid': myid,
            'month': month,
            'day': day,
            'time' : time
        })
    context =  {'recent_chats': sorted(recent_chats, key=lambda x: x.timestamp, reverse=True), 'theFolder':projectFolder,'thefile':theFile,'allFiles':allFilesCount,'allUsers':allUsers,'getFile':files_with_dates, 'lecturers':lecturers, 'allFile':allDocuments, 'getFileM':files_with_datesM, 'mycounted':mycounted}
    return context