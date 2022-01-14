from django.urls import path
from .views import *

app_name = 'job'
urlpatterns = [
    path('',                                 HomeView.as_view(),                  name='home'),
    path('add-job/',                         AddNewJob.as_view(),                 name='add_job'),
    path('job-list/',                        AllJobsView.as_view(),               name='job_list'),
    path('job-detail/<int:id>/',             JobDetailView,                       name='job_details'),
    path("admin-login/",                     AdminLoginView.as_view(),            name="admin_login"),
    path("admin-logout/",                    AdminLogoutView.as_view(),           name="admin_logout"),
    path("admin-add-job/",                   AdminJobAddView.as_view(),           name="admin_add_job"),
    path("admin-add-company/",               AdminCompanyAddView.as_view(),       name="admin_add_company"),
    path("admin-add-category/",              AdminCategoryAddView.as_view(),      name="admin_add_category"),
    path("admin-edit-job/<int:pk>",          AdminEditJopView.as_view(),          name="admin_edit_job"),
    path("admin-edit-category/<int:pk>",     AdminEditCategoryView.as_view(),     name="admin_edit_category"),
    path("admin-edit-company/<int:pk>",      AdminEditCompanyView.as_view(),      name="admin_edit_company"),
    path("admin-job-list/",                  AdminJobList.as_view(),              name="admin_all_jobs"),
    path("admin-company-list/",              AdminCompanyList.as_view(),          name="admin_all_company"),
    path("admin-category-list/",             AdminCategoryList.as_view(),         name="admin_all_category"),
    path("admin-job/<int:pk>/",              AdminJobDetailView.as_view(),        name="admin_job_detail"),
    path("admin-company/<int:pk>/",          AdminCompanyDetailView.as_view(),    name="admin_company_detail"),
    path("admin-category/<int:pk>/",         AdminCategoryDetailView.as_view(),   name="admin_category_detail"),
    path('candidate-register/',              CandidateRegisterView.as_view(),     name='candidate_register'),
    path('candidate-login/',                 CandidateLoginView.as_view(),        name='candidate_login'),
    path('candidate-logout/',                CandidateLogoutView.as_view(),       name='candidate_logout'),
    path('candidate-profile/',               CandidateProfileView.as_view(),      name='candidate_profile'),
    path('candidate-edit-profile/<int:pk>/', UpdateProfileView.as_view(),         name='candidate_edit_profile'),
    path('manage-skill/<int:cp_id>/',        ManageSkillView.as_view(),           name='manage_skill'),
    path('category-jobs/<int:cat_id>/',      CategoryView.as_view(),              name='category_jobs'),
    path('company-jobs/<int:com_id>/',       CompanyView.as_view(),               name='company_jobs'),
    path('all-category/',                    AllCategoryView.as_view(),           name='all_category'),
    path('all-company/',                     AllCompanyView.as_view(),            name='all_company'),
    path('contact/',                         ContactView.as_view(),               name='contact'),

]