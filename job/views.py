from django.shortcuts import render,redirect
from django.urls import reverse_lazy,reverse
from django.contrib.auth import authenticate , login ,logout
from django.views.generic import TemplateView,View,CreateView,FormView,DetailView,ListView,UpdateView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from .models import *
from .forms import *



class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/admin-login/")
        return super().dispatch(request, *args, **kwargs)

class AdminLoginView(FormView):
    template_name = "Admins/admin_login.html"
    form_class = AdminLoginForm
    success_url = reverse_lazy('jobs:admin_home')
    
    def form_valid(self, form):
        user_name = form.cleaned_data.get('username')
        pass_word = form.cleaned_data['password']
        usr = authenticate(username=user_name,password=pass_word)
        if usr is not None and Admin.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request,self.template_name,{'form':self.form_class})
        return super().form_valid(form)

class AdminHomeView(TemplateView):
    template_name = "Admins/job_list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["all_orders"] = Order.objects.filter(order_status = "Order Received").order_by('-id') 
        return context

class AdminLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('jobs:home')
    
class AdminJobAddView(CreateView):
    template_name = "Admins/add_new_job.html"
    form_class = AddJobForm
    success_url = reverse_lazy("jobs:admin_home")
    def form_valid(self,form):
        form.save()           
        return super().form_valid(form)

class AdminCompanyAddView(CreateView):
    template_name = "Admins/add_new_company.html"
    form_class = AddCompanyForm
    success_url = reverse_lazy("jobs:admin_all_company")
    def form_valid(self,form):
        form.save()           
        return super().form_valid(form)

class AdminCategoryAddView(CreateView):
    template_name = "Admins/add_new_category.html"
    form_class = AddCategoryForm
    success_url = reverse_lazy("jobs:admin_all_category")
    def form_valid(self,form):
        form.save()           
        return super().form_valid(form)

class AdminJobDetailView(DetailView):
    template_name = "Admins/admin_job_detail.html"
    model = Jobs
    context_object_name = "job_object"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AdminCompanyDetailView(DetailView):
    template_name = "Admins/admin_company_detail.html"
    model = Company
    context_object_name = "com_object"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AdminCategoryDetailView(DetailView):
    template_name = "Admins/admin_category_detail.html"
    model = Category
    context_object_name = "cat_object"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class AdminEditJopView(UpdateView):
    model = Jobs
    form_class = AddJobForm
    template_name = 'Admins/edit_job.html'
    def get_success_url(self, *args, **kwargs):
        success_url = reverse_lazy('jobs:admin_all_jobs')
        return success_url

class AdminJobList(ListView):
    template_name = 'Admins/job_list.html'
    queryset = Jobs.objects.all().order_by('-id')
    context_object_name = "all_jobs"

class AdminCompanyList(ListView):
    template_name = 'Admins/company_list.html'
    queryset = Company.objects.all().order_by('-id')
    context_object_name = "all_companies"

class AdminEditCompanyView(UpdateView):
    model = Company
    form_class = AddCompanyForm
    template_name = 'Admins/edit_company.html'
    def get_success_url(self, *args, **kwargs):
        success_url = reverse_lazy('jobs:admin_all_company')
        return success_url

class AdminCategoryList(ListView):
    template_name = 'Admins/category_list.html'
    queryset = Category.objects.all().order_by('-id')
    context_object_name = "all_category"

class AdminEditCategoryView(UpdateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'Admins/edit_category.html'
    def get_success_url(self, *args, **kwargs):
        success_url = reverse_lazy('jobs:admin_all_company')
        return success_url

class CandidateRegisterView(CreateView):
    template_name = 'candidate/signup.html'
    form_class = CandidateRegisterForm
    success_url = reverse_lazy('jobs:home')
    
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = User.objects.create_user(username,email,password)
        form.instance.user = user
        login(self.request , user)
        return super().form_valid(form)

class CandidateLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('jobs:home')

# candidate logout
class CandidateLoginView(FormView):
    template_name = 'candidate/login.html'
    form_class = CandidateLoginForm
    success_url = reverse_lazy('jobs:home')
    
    def form_valid(self,form):
        user_name = form.cleaned_data.get('username')
        pass_word = form.cleaned_data['password']
        usr = authenticate(username=user_name,password=pass_word)
        if usr is not None and Candidates.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request,self.template_name,{'form':self.form_class})
        return super().form_valid(form)
    
    def get_success_url(self):
        if 'next' in self.request.GET:
            next_url = self.request.GET.get('next')
            return next_url
        else:
            return self.success_url

# candidate profile
class CandidateProfileView(LoginRequiredMixin,CreateView):

    template_name = "candidate/profile.html"
    form_class = CandidateSkills
    success_url = '/candidate-profile/'
     
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_user = self.request.user
        profile_own = Candidates.objects.get(user=self.request.user)
        context["profile"] = profile_own
        return context
    
    def form_valid(self, form):
        form.instance.candidate = Candidates.objects.get(user=self.request.user)
        return super().form_valid(form)

class ManageSkillView(View):
    def get(self,request,*args, **kwargs):
        cp_id = self.kwargs['cp_id']
        action = request.GET.get('action')
        cp_obj = skills.objects.get(id = cp_id)
        if action == 'rcr':
            cp_obj.delete()
        else:
            pass
        return redirect('/candidate-profile/')

class UpdateProfileView(UpdateView):
    model = Candidates
    form_class = ProfileUpdateForm
    template_name = 'candidate/edit_profile.html'
    
    def get_object(self, *args, **kwargs):
        candidate = get_object_or_404(Candidates, pk=self.kwargs['pk'])
        return candidate
    
    def get_success_url(self, *args, **kwargs):
        success_url = reverse_lazy('jobs:candidate_profile')
        return success_url
 
class HomeView(TemplateView):
    template_name = "jobs/home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_jobs = Jobs.objects.all().order_by('-id')
        all_category = Category.objects.all().order_by('-id')
        all_company = Company.objects.all().order_by('-id')
        context["all_jobs"] = all_jobs
        context["all_category"] = all_category
        context["all_company"] = all_company
        return context
    
class AllJobsView(TemplateView):
    template_name='jobs/job_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_jobs = Jobs.objects.all().order_by('-id') 
        paginator = Paginator(all_jobs,5)
        page_number = self.request.GET.get('page')
        job_list = paginator.get_page(page_number)
        context["list_jobs"] = job_list 
        context['all_jobs'] = Jobs.objects.all()
        context["all_category"] = Category.objects.all().order_by('-id')
        context["all_company"] = Company.objects.all().order_by('-id')
        return context
    
class AddNewJob(CreateView):
    template_name = "add_new_job.html"
    form_class = AddJobForm
    success_url = reverse_lazy("job:home")
    def form_valid(self,form):
        return super().form_valid(form)
    
def JobDetailView(request,id):
    job = Jobs.objects.get(id=id)
    all_category= Category.objects.all().order_by('-id')
    all_company = Company.objects.all().order_by('-id')
    if request.method=='POST':
        form = ApplyToJobForm(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job
            myform.save()
    else:
        form = ApplyToJobForm()
    
    context = {'job':job,'form':form,'all_category':all_category,'all_company':all_company}
    return render(request, 'jobs/job_detail.html' , context)
 
class AllCategoryView(TemplateView):
    template_name = 'jobs/allcategory.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_category'] = Category.objects.all().order_by('-id')
        context['all_company'] = Company.objects.all().order_by('-id')
        return context
    
class AllCompanyView(TemplateView):
    template_name = 'jobs/allcompany.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_category'] = Category.objects.all().order_by('-id')
        context['all_company'] = Company.objects.all().order_by('-id')
        return context  
     
class CategoryView(TemplateView):
    template_name = "jobs/jobCategory.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_id = kwargs['cat_id']
        context["Category_Jobs"] = Category.objects.get(id=cat_id)
        context["all_category"] = Category.objects.all().order_by('-id')
        context["all_company"] = Company.objects.all().order_by('-id')
        return context
    
class CompanyView(TemplateView):
    template_name = "jobs/jobCompany.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cat_id = kwargs['com_id']
        context["Company_Jobs"] = Company.objects.get(id=cat_id)
        context["all_category"] = Category.objects.all().order_by('-id')
        context["all_company"] = Company.objects.all().order_by('-id')
        return context

class ContactView(FormView):
    template_name="jobs/contact_us.html"
    form_class = ContactForm
    success_url = reverse_lazy('jobs:home')
    
    def form_valid(self,form):
        subject = form.cleaned_data.get('subject')
        email = form.cleaned_data['email']
        msg = form.cleaned_data['msg']
        myemail = settings.EMAIL_HOST_USER
        send_mail(subject,msg,myemail,[email],fail_silently = False)
        return super().form_valid(form)
    


