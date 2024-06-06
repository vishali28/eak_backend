"""
URL configuration for eakApi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from eakApp.patients import *
from eakApp.common.common import *
from django.views.static import serve
from django.conf.urls import static
from django.urls import re_path as url
from eakApp.users import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('eakapi/getallstatesdetails/', GetAllStateDetails.as_view()),
    path('eakapi/getallpatientdetails/',GetPatietsDetails.as_view()),
    path('eakapi/addpatientdetails/',InsertUpdatePatientDetails.as_view()),
    path('eakapi/deletepatientdetailsbyid/',DeletePatientDetailsById.as_view()),
    path('eakapi/uploadfile/', UploadFile.as_view()),
    path('eakapi/getallmedicinetypes/', GetAllMedicinetypes.as_view()),
    # path('eakapi/getmedicineexcel/', InsertMedicinefromExcel.as_view()),
    path('eakapi/getpatientdatabyid/', GetPatientDetailsByid.as_view()),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    path('eakapi/getmedicationdetails/', GetMedicationDetails.as_view()),
    path('eakapi/inspatientmedicaldetails/', InsertPatientMedicationDetails.as_view()),
    path('eakapi/updatepatentcasesheet/',UpdateCasesheetbyPatientid.as_view()),
    path('eakapi/insertupdateuserdetails/', Ins_UpdateUserDetails.as_view()),
   
    
]
