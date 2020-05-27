import datetime
from django.utils import timezone
import json
import os
from django.db.models import Q
from django.conf import settings
from django.conf.urls.static import static
from django.core import serializers as DJangoSerializers
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers as RestSerializers
from rest_framework import status, viewsets
from rest_framework.decorators import (action,   parser_classes)
from rest_framework.parsers import FileUploadParser, JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.renderers import (JSONRenderer, StaticHTMLRenderer, TemplateHTMLRenderer)
from rest_framework.response import Response
from rest_framework.views import APIView
# from requests_toolbelt import MultipartEncoder
import requests

import logging
import employment_api.settings as app_settings
log = logging.getLogger('MYAPP')

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

# from twilio.twiml.messaging_response import MessagingResponse
from django.http import FileResponse
# from .match_response import *
from . import models
import requests
import tempfile
# from urllib.request import urlopen, Request

from django.core import files


class digital(viewsets.ViewSet):
    queryset = models.SessionModel.objects.all()

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def get_response(self, request):
        return Response('Thank you')







#     # renderer_classes = (Renderer.CustomJSONRenderer,)
#     counter = models.SessionModel()
#     req_list = []


#     @action(detail=False, methods=['get'], permission_classes=[AllowAny])
#     def get_response(self, request):
#         try:
#             params = request.GET                
#             return Response(params)
#         except Exception as ex:
#             return Response(f'Error: {str(ex)}')
            
#     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     def post_response(self, request):
#         try:
#             data = request.data
#             return Response(data)
#         except Exception as ex:
#             return Response(f'Error: {str(ex)}')

#     @csrf_exempt
#     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     def sms_reply(self, request):
#         try:               
#             data = request.data     
#             log.info(data['Body'])
#             resp = MessagingResponse()
#             # data_json = json.dumps(data)
#             # msg = data_json['Body'][0]
#             # data = data.dict()
#             log.info(data['Body'])
            
#             # res1 = resp.message()
#             response_msg = 'Welcome {} '.format(data['Body'])
#             res1 = "<Response><Message>" + response_msg +"</Message></Response>"
#             log.info(res1)
#             # return HttpResponse("<Response><Message>Welcome</Message></Response>", content_type='text/xml')
#             return HttpResponse(res1, content_type='text/xml')
#         except Exception as ex:            
#             log.error(str(ex))
#             return HttpResponse("Not Working ", str(ex))



#     @csrf_exempt
#     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     def sms1(self, request):
#         media_url=['https://images.unsplash.com/photo-1545093149-618ce3bcf49d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=668&q=80']
#         response = HttpResponse(mimetype="image/png")
#         # img = Image.open(media_url)
#         # img.save(response,'png')
#         return response


#     @csrf_exempt
#     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     def sms(self, request):
#         r = MessagingResponse()
#         r.message('Hello from your Django app!')
#         return HttpResponse(r, content_type='text/xml')
    



#     @csrf_exempt
#     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     def hello(self):
#         return "Hello World!"

#     @csrf_exempt
#     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     def reply_whatsapp(self, request):
#         GOOD_BOY_URL = "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
#         response = MessagingResponse()
#         data = request.data
#         print(data)
#         log.info(data['Body'])
#         if data['Body'] != 'image':
#             msg = response.message("Your message is-- {}. Kindly send 'image' message for getting an image".format(data['Body']))
#         else:
#             msg = response.message("Dog image!!!")
#             msg.media(GOOD_BOY_URL)
#         return HttpResponse(response)


#     # if __name__ == "__main__":
#     #     app.run(debug=True)


#     @csrf_exempt
#     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     def verify_record(self, request):
#         match_record = MatchRecord()
#         response = MessagingResponse()
#         matched = False
#         data = request.data
#         print(data)
#         print(type(data['Body']))
#         log.info(data['Body'])
#         req_data = data['Body'].lower()

#         if len(req_data) > 10:
#             req_list = req_data.split()
#             matched = match_record.match_dl(req_list)
        
#         if matched:
#             msg = response.message('dl matched')
#         else:
#             msg = response.message('dl not matched')
#         return HttpResponse(response)


#     @csrf_exempt
#     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     def verify_dl_detail(self, request):
#         try:
#             match_record = MatchRecord()
#             response = MessagingResponse()
#             matched = False
#             data = request.data
#             print(data)
#             print(type(data['Body']))
#             log.info(data['Body'])
#             req_data = data['Body'].lower()
#             if req_data == 'hvstarts':
#                 self.counter.count = 1
#                 msg = response.message('''Welcome to Hello Verify \nUpload and Verify Documents in matter of seconds \nWho do you want to verify \n1. Myself \n2. Someone Else''')
#             elif (req_data == 'myself' or req_data == '1') and self.counter.count == 1:
#                 self.counter.count = 2
#                 msg = response.message('''Please select one of the below services. \n1. Driver \n2. Nanny \n3. security Guard \n4. Any One''')
            
#             elif (req_data == 'someone else' or req_data == '2') and self.counter.count == 1:
#                 self.counter.count = 2
#                 msg = response.message('''Please select one of the below services. \n1. Driver \n2. Nanny \n3. security Guard \n4. Any One''')

#             elif (req_data == 'driver' or req_data == '1') and self.counter.count == 2:
#                 self.counter.count = 3
#                 msg = response.message('''Please share your Driving License details (consent dlnumber dob) in format "Y MH0120090091406 12-06-1987" ''')
#             elif len(req_data) > 10 and self.counter.count == 3:
#                 print('inside dl')
#                 req_list = req_data.split()
#                 matched = match_record.match_dl(req_list)
#                 if matched:
#                     msg = response.message('DL record matched')
#                 else:
#                     msg = response.message('DL record not matched')
#             else:
#                 msg = response.message('Wrong input!!')
#             return HttpResponse(response)
#         except Exception as ex:            
#             log.error(str(ex))
#             return HttpResponse("Not Working ", str(ex))
#     # @csrf_exempt
#     # @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     # def verify_record_image(self, request):
#     #     print(request.data)
#     #     file = request.data['file']
#     #     image = models.UploadImageTest.objects.create(image=file)
#     #     return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


#     # @csrf_exempt
#     # @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     # def handle_incoming_message(self, request):
#     #     response = MessagingResponse()
#     #     print(request.data)
#     #     # message_sid = request.POST.get('MessageSid', '')
#     #     # from_number = request.POST.get('From', '')
#     #     # num_media = int(request.POST.get('NumMedia', 0))

#     #     # media_files = [(request.POST.get("MediaUrl{}".format(i), ''),
#     #     #                 request.POST.get("MediaContentType{}".format(i), ''))
#     #     #             for i in range(0, num_media)]
#     #     print(request.POST.get("MediaUrl0"))

#     #     # response = reply_with_twiml_message(message_sid, from_number, num_media, media_files)
#     #     msg = response.message('successfully send image')
#     #     return HttpResponse(response, content_type='application/xml')


#     @csrf_exempt
#     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     def handle_image_message(self, request):
#         try:
#             response = MessagingResponse()
#             print(request.data)
#             image_url = request.POST.get("MediaUrl0")

#             print('image_url- ', image_url)
#             request = requests.get(image_url, stream=True)
#             print('request-->', request)

#             file_name = image_url.split('/')[-1]
#             file_name = file_name + '.jpg'

#             lf = tempfile.NamedTemporaryFile()
#             print('lf-->', lf)

#             for block in request.iter_content(1024 * 8):

#                 if not block:
#                     break

#                 # Write image block to temporary file
#                 lf.write(block)

#             # Create the model you want to save the image to
#             image = models.ModelWithImage()

#             # Save the temporary image to the model#
#             # This saves the model so be sure that is it valid
#             image.image.save(file_name, files.File(lf))
#             msg = response.message('sucessfully uploaded')
#             return HttpResponse(response, content_type='application/xml')
#         except Exception as ex:            
#             log.error(str(ex))
#             msg = response.message('Wrong input!!')
#             return HttpResponse(response, content_type='application/xml')



#     @csrf_exempt
#     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     def verify_dl_image(self, request):
#         try:
#             print(request.data)
#             response = MessagingResponse()

#             # ---------------------- ocr api hit ----------------------------------------#
#             url = 'http://52.66.35.239:8002/v1/ReadTextFromImage'
#             image_url = request.POST.get("MediaUrl0")
#             print('image_url', image_url)
#             payload = MultipartEncoder(fields={'file': ('file.zip', open(image_url, 'rb'), 'text/plain'), 'consent': consent, 'shareCode': shareCode})
#             headers = { 'content-type': "multipart/form-data" }
#             print(payload)

#             response1 = requests.post(url, payload=payload, headers=headers)
#             print(response1)
#             # msg = response.message(response1)
#             return HttpResponse(response1, content_type='application/xml')
#         # --------------------------------------------------------------------------#
#         except Exception as ex:            
#             log.error(str(ex))
#             msg = response.message('Wrong input!!')
#             return HttpResponse(response, content_type='application/xml')

# # Y MH0120090091406 12-06-1987
# # http://7714d7a7.ngrok.io/api/verify_dl_detail/
# # http://7714d7a7.ngrok.io/api/handle_image_message/
# # https://stackoverflow.com/questions/16174022/download-a-remote-image-and-save-it-to-a-django-model
# # http://63f2ebaf.ngrok.io/api/handle_image_message/
# # lf--> <tempfile._TemporaryFileWrapper object at 0x0000020DD5C974C8>


#     @csrf_exempt
#     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     def verify_dl_details(self, request):
#         try:
#             match_record = MatchRecord()
#             response = MessagingResponse()
#             matched = False
#             data = request.data
#             print(data)
#             print(type(data['Body']))
#             log.info(data['Body'])
#             req_data = data['Body'].lower()
#             if req_data == 'hvstarts':
#                 self.req_list.clear()
#                 self.counter.count = 1
#                 msg = response.message('''Welcome to Hello Verify \nUpload and Verify Documents in matter of seconds \nWho do you want to verify \n1. Myself \n2. Someone Else''')
#             elif (req_data == 'myself' or req_data == '1') and self.counter.count == 1:
#                 self.counter.count = 2
#                 msg = response.message('''Please select one of the below services. \n1. Driver \n2. Nanny \n3. security Guard \n4. Any One''')
#             elif (req_data == 'someone else' or req_data == '2') and self.counter.count == 1:
#                 self.counter.count = 2
#                 msg = response.message('''Please select one of the below services. \n1. Driver \n2. Nanny \n3. security Guard \n4. Any One''')
#             elif (req_data == 'driver' or req_data == '1') and self.counter.count == 2:
#                 self.counter.count = 3
#                 msg = response.message('''Please share your DL No.''')
#             elif self.counter.count == 3:
#                 self.counter.count = 4
#                 self.req_list.append(req_data)
#                 print('req_list1 ->', self.req_list)
#                 msg = response.message('''Please share your DOB in the format (DD-MM-YYYY)''')    
#             elif self.counter.count == 4:
#                 self.counter.count = 5
#                 self.req_list.append(req_data)
#                 print('req_list2 ->', self.req_list)                
#                 msg = response.message('''Please share your Consent \n1. Yes \n2. No''')
#             elif (req_data == '1' or req_data == 'yes') and self.counter.count == 5:
#                 req_data = 'Y'
#                 self.req_list.append(req_data)
#                 print('matching detail')
#                 print('req_list3 ->', self.req_list)
#                 matched = match_record.match_dl(self.req_list)
#                 self.req_list = []
#                 if matched == True:
#                     msg = response.message('DL record matched')
#                 else:
#                     msg = response.message('DL record not matched')
#             else:
#                 msg = response.message('Wrong input!! OR No Consent')
#             return HttpResponse(response)
#         except Exception as ex:            
#             log.error(str(ex))
#             return HttpResponse("Not Working ", str(ex))


#     @csrf_exempt
#     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     def handle_images(self, request):
#         try:
#             response = MessagingResponse()
#             print(request.data)
#             image_url = request.POST.get("MediaUrl0")
#             print('image_url- ', image_url)
#             request = requests.get(image_url, stream=True)
#             print('request-->', request)
#             file_name = image_url.split('/')[-1]
#             file_name = file_name + '.jpg'
#             lf = tempfile.NamedTemporaryFile()
#             print('lf-->', lf)
#             for block in request.iter_content(1024 * 8):
#                 if not block:
#                     break
#                 # Write image block to temporary file
#                 lf.write(block)
#             # Create the model you want to save the image to
#             image = models.ModelWithImage()
#             # Save the temporary image to the model#
#             # This saves the model so be sure that is it valid
#             image.image.save(file_name, files.File(lf))
            
#             # ------------------------ hit ocr api ------------------ #
#             url = 'http://52.66.35.239:8002/v1/ReadTextFromImage'
#             # image_url = 'D:\APIs\whatsappapi\myhvproj\media\images\\' + file_name
#             image_url = app_settings.MEDIA_ROOT + '\\images\\' + file_name
#             # image_url = '/D:/APIs/whatsappapi/myhvproj/media/images\/' + file_name
#             print('image_url', image_url)
#             payload = MultipartEncoder(fields={'file': ('file', open(image_url, 'rb')) })
#             multipart_form_data = {
#                 'image': (file_name, open(image_url, 'rb'))
#             }
#             headers = { 'content-type': "multipart/form-data; boundary=--------------------------442473888289216136190209" }
#             print('payload', payload)
#             print(file_name)
#             response = requests.post(url, files=multipart_form_data)
#             print(response)
#             # msg = response.message(str(response1))
#             #-----------------------------------------------------------
#             # payload = {}
#             # files = [
#             # ('file', open('/C:/Users/SV999500/Desktop/dl.jpg','rb'))
#             # ]
#             # headers = {
#             # 'Content-Type': 'multipart/form-data; boundary=--------------------------520169851510992314668310'
#             # }

#             # response = requests.request("POST", url, headers=headers, data = payload, files = files)


#             return HttpResponse(response, content_type='application/xml')
#         except Exception as ex:            
#             log.error(str(ex))
#             msg = response.message('Wrong input!!')
#             return HttpResponse(response, content_type='application/xml')


#     @csrf_exempt
#     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     def handle_dl_images(self, request):
#         try:
#             match_record = MatchRecord()
#             req_list = []
#             req_list.clear()
#             response = MessagingResponse()
#             print('request data - ', request.data)
#             image_url = request.POST.get("MediaUrl0")
#             print('image_url- ', image_url)
#             request = requests.get(image_url, stream=True)
#             file_name = image_url.split('/')[-1]
#             file_name = file_name + '.jpg'
#             lf = tempfile.NamedTemporaryFile()
#             print('lf-->', lf)
#             for block in request.iter_content(1024 * 8):
#                 if not block:
#                     break
#                 lf.write(block)
#             image = models.ModelWithImage()
#             image.image.save(file_name, files.File(lf))
            
#             # ------------------------ hit ocr api ------------------ #
#             url = 'http://52.66.35.239:8002/v1/ReadTextFromImage'
#             url2 = 'http://13.233.33.194:2000/services/api/v1/util/ocr/get_dl_details/'
#             # url3 = 'http://53a9070c.ngrok.io/api/handle_dl_images/'
#             image_url = app_settings.MEDIA_ROOT + '\\images\\' + file_name
#             # print('image_url', image_url)
#             # payload = MultipartEncoder(fields={'file': ('file', open(image_url, 'rb')) })
#             multipart_form_data = {
#                 'image': (file_name, open(image_url, 'rb'))
#             }
#             response1 = requests.post(url, files=multipart_form_data)
#             str_res = response1.text
#             print(str_res)
#             payload = {'DL': str_res}
#             res = requests.post(url2, data=payload)
            
#             res = res.text.lower()
#             print(type(res))
#             res = json.loads(res)
#             res = json.loads(res["result"])
#             dl_no = res["dl_no"]
#             dl_no = dl_no.replace('-', '')
#             dl_no = dl_no.replace(' ', '')
#             req_list.append(dl_no)
#             dob = res["dob"]
#             dob = dob.replace('/', '-')
#             req_list.append(dob)
#             req_list.append('Y')
#             print('req_list - ', req_list)
#             matched = match_record.match_dl(req_list)
#             if matched:
#                 msg = response.message('DL record matched')
#             else:
#                 msg = response.message('DL record not matched')
#             print(response)
#             return HttpResponse(response, content_type='application/xml')
#         except Exception as ex:            
#             log.error(str(ex))
#             msg = response.message('Wrong input!!')
#             print('inside except')
#             return HttpResponse(response, content_type='application/xml')


#     @csrf_exempt
#     @action(detail=False, methods=['post'], permission_classes=[AllowAny])
#     def handle_pan_images(self, request):
#         try:
#             match_record = MatchRecord()
#             req_list = []
#             req_list.clear()
#             response = MessagingResponse()
#             print('request data - ', request.data)
#             image_url = request.POST.get("MediaUrl0")
#             print('image_url- ', image_url)
#             request = requests.get(image_url, stream=True)
#             file_name = image_url.split('/')[-1]
#             file_name = file_name + '.jpg'
#             lf = tempfile.NamedTemporaryFile()
#             print('lf-->', lf)
#             for block in request.iter_content(1024 * 8):
#                 if not block:
#                     break
#                 lf.write(block)
#             image = models.ModelWithImage()
#             image.image.save(file_name, files.File(lf))
            
#             # ------------------------ hit ocr api ------------------ #
#             url = 'http://52.66.35.239:8002/v1/ReadTextFromImage'
#             url2 = 'http://13.233.33.194:2000/services/api/v1/util/ocr/get_pan_details/'
#             # url3 = 'http://53a9070c.ngrok.io/api/handle_dl_images/'
#             image_url = app_settings.MEDIA_ROOT + '\\images\\' + file_name
#             # print('image_url', image_url)
#             # payload = MultipartEncoder(fields={'file': ('file', open(image_url, 'rb')) })
#             multipart_form_data = {
#                 'image': (file_name, open(image_url, 'rb'))
#             }
#             response1 = requests.post(url, files=multipart_form_data)
#             str_res = response1.text
#             # str_res = str_res.replace('\\', '')
#             # str_res = str_res.strip('\"')
#             print(str_res)
#             # str_res = "आयकर विभाग\\nभारत सरकार\\nINCOME TAX DEPARTMENT\\nGOVT. OF INDIA\\nसत्यमेव जयते\\nSAURABH VERMA\\nSWARAJYA SINGH VERMA\\n29/05/1990\\nदिचाय\\nPermanent Account Number\\nASOPV4200H\\nSaurabh Vooma\\nSignature\\n03052013\\n"
            
#             # str_res = "आयकर विभाग\nभारत सरकार\nINCOME TAX DEPARTMENT\nGOVT. OF INDIA\nसत्यमेव जयते\nSAURABH VERMA\nSWARAJYA SINGH VERMA\n29/05/1990\nPermanent Account Number\nASOPV4200H\nSaurobh Veoma\nSignature\n03052013\n"
#             payload = {'PAN': str_res}
#             print(payload)
#             res = requests.post(url2, data=payload)
            
#             res = res.text.lower()
#             print(res)
#             res = json.loads(res)
#             res = json.loads(res["result"])
#             dl_no = res["dl_no"]
#             dl_no = dl_no.replace('-', '')
#             dl_no = dl_no.replace(' ', '')
#             req_list.append(dl_no)
#             dob = res["dob"]
#             dob = dob.replace('/', '-')
#             req_list.append(dob)
#             req_list.append('Y')
#             print('req_list - ', req_list)
#             matched = match_record.match_dl(req_list)
#             if matched:
#                 msg = response.message('DL record matched')
#             else:
#                 msg = response.message('DL record not matched')
#             print(response)
#             return HttpResponse(response, content_type='application/xml')
#         except Exception as ex:            
#             log.error(str(ex))
#             msg = response.message('Wrong input!!')
#             print('inside except')
#             return HttpResponse(response, content_type='application/xml')

