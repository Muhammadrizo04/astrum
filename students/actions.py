from django.http import HttpResponse
from zipfile import ZipFile
import io

def DownloadPptxFile(modeladmin, request, queryset):
    responses = []
    
    for obj in queryset:
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.presentationml.presentation')
        response['Content-Disposition'] = f'attachment; filename="{obj.pptx_file.name}"'

        with open(obj.pptx_file.path, 'rb') as pptx_content:
            response.write(pptx_content.read())
        
        responses.append(response)
    
    if len(responses) == 1:
        # If only one file is selected, return the response directly
        return responses[0]
    else:
        # If multiple files are selected, create a zip file and return it


        zip_buffer = io.BytesIO()
        with ZipFile(zip_buffer, 'w') as zipf:
            for obj, response in zip(queryset, responses):
                filename = obj.pptx_file.name
                zipf.writestr(filename, response.content)
        
        response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename="pptx_files.zip"'
        return response

DownloadPptxFile.short_description = "Download PPTX Files "
