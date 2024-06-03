import json
from django.db import connection 
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.views import APIView
from eakApp.common import dbfunctions, dbconnect



cursor = connection.cursor()

class GetPatietsDetails(APIView):
   
   def get(self,request):
    try:
      
    #   CrequestMiddleware.set_request(request)
      params ={}

      # cursor.callproc(dbfunctions.get_all_patient_details)
      allpatientdetails=dbconnect.query_executer.get(dbfunctions.get_all_patient_details,params)
      return HttpResponse(json.dumps(allpatientdetails))
        
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
         
        params={}
        # cursor.callproc(dbfunctions.getmedicationdetails)
        medication_details = dbconnect.query_executer.get(dbfunctions.getmedicationdetails,params)
        return HttpResponse(json.dumps(medication_details))

      except Exception as err:
         return HttpResponse(err)
      

class InsertPatientMedicationDetails(APIView):
   def post(self,request):
      med_listjson = request.data['medicationlistjson']
      try:
          params={
            'patientid':request.data['patient_id'] ,
	          'doctorid': request.data['doctor_id'] ,
	          'specialinstructions':request.data['spe_instruct'],
	          'nextmedicine':request.data['next_med'],
	          'p_ailment' :request.data['patient_ailment'],
            'medicalrepots': request.data['patient_medicalreports'],
            'medicinelist_json':json.dumps(request.data['medicationlistjson']),
	          'createdby' : request.data['createdby'],
            'consultationdate': request.data['consult_date']
          }

          cursor.callproc(dbfunctions.insert_patient_medicationdetails,params)
          res= cursor.fetchall()
          return HttpResponse(json.dumps(res[0][0]))
      
      except Exception as err:
         return HttpResponse(err)
