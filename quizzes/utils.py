import random

# To generate PDF white weasyprint
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import HttpResponse
import weasyprint

# To generate PDF white xhtml2pdf
# from django.conf import settings
# from django.contrib.staticfiles import finders


# datetime
from datetime import datetime


# def link_callback(uri, rel):
#     """
#     Convert HTML URIs to absolute system paths so xhtml2pdf can access those
#     resources
#     """
#     result = finders.find(uri)
#     if result:
#         if not isinstance(result, (list, tuple)):
#             result = [result]
#         result = list(os.path.realpath(path) for path in result)
#         path = result[0]
#     else:
#         sUrl = settings.STATIC_URL  # Typically /static/
#         sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
#         mUrl = settings.MEDIA_URL  # Typically /media/
#         mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/
#
#         if uri.startswith(mUrl):
#             path = os.path.join(mRoot, uri.replace(mUrl, ""))
#         elif uri.startswith(sUrl):
#             path = os.path.join(sRoot, uri.replace(sUrl, ""))
#         else:
#             return uri
#
#     # make sure that file exists
#     if not os.path.isfile(path):
#         raise Exception(
#             'media URI must start with %s or %s' % (sUrl, mUrl)
#         )
#     return path


# *-----------------------------------------------------------------------------------------*
# if weasyprint:
# *-----------------------------------------------------------------------------------------*
def generate_pdf(request, *args):
    template_path = args[0]
    pdf_name = args[1]
    context = args[2]
    response = HttpResponse(content_type='application/pdf')
    # if download:
    # response['Content-Disposition'] = f'attachment; filename={pdf_name}_{datetime.now()}.pdf'
    # if display:
    response['Content-Disposition'] = f'filename={pdf_name}_{datetime.now()}.pdf'
    response['Content-Tranfer-Encoding'] = 'binary'
    html_string = render_to_string(template_path, context)
    html = weasyprint.HTML(string=html_string, base_url=request.build_absolute_uri())
    css = [weasyprint.CSS(settings.STATIC_ROOT / 'css/pdf.css')]
    html.write_pdf(response, stylesheets=css)
    return response
# *-----------------------------------------------------------------------------------------*
# end if weasyprint
# *-----------------------------------------------------------------------------------------*
