import json
import os
from django.shortcuts import get_object_or_404, render
from rest_framework import serializers as RestSerializers
from rest_framework import status, viewsets
from rest_framework.decorators import (action,   parser_classes)
from rest_framework.permissions import AllowAny
from rest_framework.renderers import (JSONRenderer, StaticHTMLRenderer, TemplateHTMLRenderer)
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
import employment_api.settings as app_settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.http import FileResponse
import requests
import tempfile
from django.core import files
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from . import captcha
from . import models
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
from .captcha import GetCaptcha


class aadhaar(viewsets.ViewSet):
    queryset = models.SessionModel.objects.all()
    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def aadhaar_verification(self, request):
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        uid_no = request.data['uid']
        getcaptcha = GetCaptcha()
        driver = webdriver.Chrome(executable_path="empapi\chromedriver\chromedriver.exe", options=chrome_options)
        driver.get("https://resident.uidai.gov.in/verify")
        getcaptcha.download_captcha(driver)
        captcha_text = getcaptcha.get_captcha_text()
        driver.implicitly_wait(5)
        uid = driver.find_element_by_xpath('//*[@id="uidno"]')
        captcha = driver.find_element_by_xpath('//*[@id="security_code"]')
        uid.send_keys(uid_no)
        captcha.send_keys(captcha_text)
        driver.find_element_by_xpath('//*[@id="submitButton"]').click()
        elements = driver.find_element_by_xpath('//*[@id="maincontent"]/div/div[1]/div[3]')
        txt = elements.text
        return Response(txt)
        