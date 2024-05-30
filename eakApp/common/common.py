import json
from eakApp.common import dbfunctions;
from django.http import HttpResponse;
from rest_framework.views import APIView
from django.db import connection
import pathlib
from django.core.files.storage import FileSystemStorage
from eakApi import settings
import os
from datetime import datetime,timezone


cursor = connection.cursor()

class GetAllStateDetails(APIView):
    def post(self,request):
        try:
            params={
                'countryid':request.data['country_id']
            }
            print(params,'params')
            cursor.callproc(dbfunctions.getallstatedetailsbycountryid, params)
            stateres= cursor.fetchall()
            return HttpResponse(json.dumps(stateres[0][0]))

        except Exception as err:
            return HttpResponse(err)
        

class UploadFile(APIView):
    def post(self,request):

        file = request.FILES['uploads']
        print(file,'file')
        file_extension = pathlib.Path(file.name).suffix
        print(file_extension,'file_extension')
        now = datetime.now(timezone.utc).strftime("%d-%m-%Y--%H-%M-%S-%f")
        file_name = str(file.name).split('.')[0]  + now + file_extension
        print(file_name,'filename')
        file_path = settings.MEDIA_ROOT + settings.DIR_SLASHES + settings.DIR_SLASHES + file_name
        fs = FileSystemStorage()
        fs.save(file_path, file)
        # fs.url(filename)
        return HttpResponse(json.dumps(file_name))




