from django.urls import path
from create_jobs.views import JobCreatorHandler
from create_jobs.views import FecthJobListUsingThirdPartyAPI

urlpatterns = [
    path('createjob', JobCreatorHandler.as_view()),
    path('fetchjob', JobCreatorHandler.as_view()),
    path('fetch-job-api', FecthJobListUsingThirdPartyAPI.as_view()),
]
