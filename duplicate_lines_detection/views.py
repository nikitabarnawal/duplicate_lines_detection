from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .duplicate_lines_detection import DuplicateLineDetector


# Create your views here.

def home(request):
	return render(request, 'duplicate_lines_detection/upload_form.html', {})

def upload(request):
	error = None
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		if fs.exists(myfile.name):
			fs.delete(myfile.name)
		filename = fs.save(myfile.name, myfile)
		# uploaded_file_url = fs.url(filename)
		duplicate_detector = DuplicateLineDetector(filename)
		duplicates = duplicate_detector.detect_duplicates()
		if duplicates:
			return render(request, 'duplicate_lines_detection/near_duplicate_lines.html',{
				'duplicates' : duplicates
				})

		error = 'No Duplicates Found'

	return render(request, 'duplicate_lines_detection/upload_form.html',{
		'error':error
		})