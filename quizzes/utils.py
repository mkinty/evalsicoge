import random

# Generate pdf utils
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import HttpResponse
import weasyprint

from datetime import datetime


def generate_pdf(request, *args):
    template_path = args[0]
    pdf_name = args[1]
    context = args[2]
    response = HttpResponse(content_type='application/pdf')
    # if download
    response['Content-Disposition'] = f'filename={pdf_name}_{datetime.now()}.pdf'
    response['Content-Tranfer-Encoding'] = 'binary'
    html_string = render_to_string(template_path, context)
    html = weasyprint.HTML(string=html_string, base_url=request.build_absolute_uri())
    css = [weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
    html.write_pdf(response, stylesheets=css)
    return response