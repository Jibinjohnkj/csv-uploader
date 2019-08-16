import csv
from io import TextIOWrapper

from django.shortcuts import render
from django.views import View

from .forms import UploadFileForm
from .utils.uploader import process_products



class IndexView(View):
    def get(self, request):
        form = UploadFileForm()
        context = {'form': form}
        return render(request, 'reports/index.html', context)

    def post(self, request):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            doc = request.FILES['file']
            headers = []
            # handle huge files without freezing the whole app for hours
            for chunk in doc.chunks():
                document = chunk.decode("utf-8").splitlines()
                if not headers:
                    # Store headers for future chunks
                    headers = document.pop(0).split(',')
                process_products(document, headers)
            context = {'message': 'Products imported successfully'}
        else:
            context = {'form': form}
        return render(request, 'reports/index.html', context)

