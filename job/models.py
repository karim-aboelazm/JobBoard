from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
JOB_TYPE = (
    ('part time','part time'),
    ('full time','full time'),
)

ENGLISH_LEVELS = (
    ('beginner','beginner'),
    ('intermediate','intermediate'),
    ('advanced','advanced'),
    ('expert','expert'),
)

EXPERIANCE_LEVELS = (
    ('beginner','beginner'),
    ('intermediate','intermediate'),
    ('advanced','advanced'),
    ('expert','expert'),
)

class Admin(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='admins/')
    mobile = models.CharField(max_length=20)
    def __str__(self):
        return self.user.username
    
class Company(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(upload_to='companies_images/')
    location = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    
      # creating slug automaticaly
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Company, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
class JobOwner(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    company_ex = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    phone = models.CharField(max_length=15)
    def __str__(self):
        return self.full_name
    
class Candidates(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job = models.ForeignKey('Jobs',on_delete=models.CASCADE,null=True,blank=True)
    full_name = models.CharField(max_length=200)
    about = models.TextField(max_length=800)
    address = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='candidate_images/')
    cv = models.FileField(upload_to='candidate_resumes/',null=True, blank=True)
    phone = models.CharField(max_length=15,blank=True, null=True)
    bio = models.CharField(max_length=50)
    profession = models.CharField(max_length=30)
    experience = models.CharField(max_length=50,choices=EXPERIANCE_LEVELS,default='beginner')
    english_level = models.CharField(max_length=50,choices=ENGLISH_LEVELS,default='beginner')
    hour_rate = models.IntegerField(default=0)
    projects_num = models.IntegerField(default=0)
    
    join_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.full_name

class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(null=True, blank=True)
     # creating slug automaticaly
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.title
    
class Jobs(models.Model):
    category    = models.ForeignKey(Category, on_delete=models.CASCADE)  
    title       = models.CharField(max_length=100)
    slug        = models.SlugField(null=True, blank=True)
    description = models.TextField(max_length=1000)
    prequests   = models.TextField(max_length=1000)
    benefits    = models.TextField(max_length=1000)
    job_type    = models.CharField(max_length=50,choices=JOB_TYPE,default='part_time')  
    created_by  = models.ForeignKey(User,on_delete=models.CASCADE)
    salary      = models.PositiveIntegerField(default = 0)
    vacancy     = models.IntegerField(default=0)
    logo        = models.ImageField(upload_to='job_logo/',null=True,blank=True)
    supervisor  = models.ForeignKey(Company,on_delete=models.CASCADE)
    created_at  = models.DateTimeField(auto_now_add=True)
    view_count  = models.PositiveIntegerField(default = 0)
    location    = models.CharField(max_length=200)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Jobs, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title
   
class skills(models.Model):
    candidate = models.ForeignKey(Candidates,on_delete=models.CASCADE)
    skill = models.CharField(max_length=50,blank=True,null=True)
    percent = models.IntegerField(default=0)
    def __str__(self):
        return  self.skill 

class Candidate_Applying(models.Model):
    job = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    cv = models.FileField(upload_to='candidates_resumes/')
    about = models.TextField(max_length=800)
    def __str__(self):
        return f'candidate : [ {self.name} ] ' + ' _ Applied to _ ' +f' Job: [ {self.job} ]' 
    

