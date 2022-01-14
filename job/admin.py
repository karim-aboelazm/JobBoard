from django.contrib import admin

from .models import *

for model in [Admin,Company,Candidates,Jobs,Category,JobOwner,skills,Candidate_Applying]:
    admin.site.register(model)

