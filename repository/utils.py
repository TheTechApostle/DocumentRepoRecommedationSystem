from  .models import *
from django.contrib.auth.models import Group
def get_nav_context():
    
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
    return {'getFile':files_with_dates, 'getFileM':files_with_datesM, 'mycounted':mycounted}