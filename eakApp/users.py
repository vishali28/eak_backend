import traceback
import json
from django.db import connection 
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from eakApp.common import dbfunctions, dbconnect
from utils.logger import Logger
import utils.logmodules
from crequest.middleware import CrequestMiddleware
from eakApp.common.logger import *


logg = Logger(utils.logmodules.USERS)
logger = logg.logger()
error_logg = Logger(utils.logmodules.USERS_ERROR)
error_logg = error_logg.logger()

class Ins_UpdateUserDetails(APIView):
    def __init__(self):
        logger.info("Insert User details API starts")

    def post(self,request):
        try:
            CrequestMiddleware.set_request(request)
            logger.info("Insert User details")
            log_request(request)

            params={
                'userdetailsid': request.data['userid'],
                'usercode': request.data['userno'],
                'usertype': request.data['user_type'],
                'firstname': request.data['first_name'],
                'lastname': request.data['last_name'],
                'genderid': request.data['gender_id'],
                'age': request.data['user_age'],
                'user_dob': request.data['dateofbirth'],
                'userqualification':request.data['qualification'],
                'useraddress': request.data['address'],
                'usercontact': request.data['contactnumber'],
                'userlocation': request.data['location'],
                'userdistrict':request.data['district'],
                'userstateid': request.data['stateid'],
                'userservicejson': json.dumps(request.data['selectedServicesjson']),
                'otherinformation': request.data['other_info'],
                'createdby': request.data['created_by']
            }
            ins_res = dbconnect.query_executer.post(dbfunctions.insert_updateuser_details,params)
            logger.info("inserted user details sucessfully-{}".format(ins_res))
            log_request(ins_res)
            return HttpResponse(json.dumps(ins_res))
        except Exception as err:
            error_logg.error("user details are not inserted-{}".format(err))
            return HttpResponse(err)