import json
from aekApp.common import dbfunctions;
from django.http import HttpResponse;
from rest_framework.views import APIView
from django.db import connection

cursor = connection.cursor()

class GetALllStateDetails(APIView):
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

