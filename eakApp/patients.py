import json
from django.db import connection 
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from eakApp.common import dbfunctions
import boto3


cursor = connection.cursor()

class GetPatietsDetails(APIView):
   
   def get(self,request):
    try:
      
    #   CrequestMiddleware.set_request(request)
      cursor.callproc(dbfunctions.get_all_patient_details)
      allpatientdetails=cursor.fetchall()
      return HttpResponse(json.dumps(allpatientdetails[0][0]))
        
    except Exception as err:
      return HttpResponse(err)

    

class InsertUpdatePatientDetails(APIView):
  def post(self,request):
    try:
        
      
        params ={
            'patientdetails_id': request.data['patientid'],
            'patientnumber' : request.data['patient_num'],
            'firstvisitdate' : request.data['first_visitdate'],
            'firstname' : request.data['p_first_name'],
            'lastname' : request.data['p_last_name'],
            'gender' : request.data['p_gender'],
            'age' : request.data['p_age'],
            'dob' : request.data['p_dob'],
            'tob' : request.data['p_tob'],
            'birthplace' : request.data['p_birthplace'],
            'nearest_birthplace' : request.data['pn_birthplace'],
            'address' : request.data['p_address'],
            'mobileno' : request.data['p_mobileno'],
            'district' : request.data['p_district'],
            'p_state_id' : request.data['p_stateid'],
            'createdby': request.data['created_by'],
            'createddate': request.data['created_date'],
            'branchid': request.data['branch_id'],
            'attachmentname':request.data['attachment']
        }
        cursor.callproc(dbfunctions.ins_update_patient_details,params)
        patientres= cursor.fetchall()
        return HttpResponse(json.dumps(patientres[0][0]))
    except Exception as err:
      return HttpResponse(err)
  
class DeletePatientDetailsById(APIView):
    def post(self,request):
        try:
            params={
                'patientdetailsid':request.data['patientid'],
            }
            cursor.callproc(dbfunctions.deletepatirnt_detailsbyid,params)
            delres = cursor.fetchall()
            return HttpResponse(json.dumps(delres[0][0]))
        except Exception as err:
           return HttpResponse(err)

        
class GetPatientDetailsByid(APIView):
  def post(self, request):
    try:
       
      params = {
        'patientid': request.data['patient_id'],
        'action_typeid': request.data['actionid']
      }
      cursor.callproc(dbfunctions.get_patient_detailsbyid, params)
      pa_details = cursor.fetchall()

      return HttpResponse(json.dumps(pa_details[0][0]))
    except Exception as err:
       return HttpResponse(err)
        
            
      
class GetMedicationDetails(APIView):
   def get(self,request):
      try:
         
        cursor.callproc(dbfunctions.getmedicationdetails)
        medication_details =cursor.fetchall()
        return HttpResponse(json.dumps(medication_details[0][0]))

      except Exception as err:
         return HttpResponse(err)
      

class InsertPatientMedicationDetails(APIView):
   def post(self,request):
      try:
          params={
            'patientid':request.data['patient_id'] ,
	          'doctorid': request.data['doctor_id'] ,
	          'medicielistid':request.data['medicine_listid'] ,
	          'med_dosage' :request.data['dosage'],
	          'med_consume_time': request.data['consumetime'] ,
	          'special_instructions':request.data['spe_instruct'] ,
	          'next_medicine':request.data['next_med'],
	          'aliment' :request.data['p_aliment'],
	          'created_by' : request.data['createdby']
          }
          cursor.callproc(dbfunctions.insert_patient_medicationdetails,params)
          res= cursor.fetchall()
          return HttpResponse(json.dumps(res[0][0]))
      
      except Exception as err:
         return HttpResponse(err)
