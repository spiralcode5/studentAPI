from studentapi.viewsets import StudentViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('student',StudentViewset) #student-->it is prefix