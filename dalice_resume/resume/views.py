from django.shortcuts import render, redirect
from .models import User, Experience, Skill, Project, Certification, Education, Volunteer, Blog
from .forms import BlogForm

# Create your views here.


def home(request): 
    """The home page for Dalice's resume"""
    return render(request, 'resume/home.html')

def aboutme(request): 
    """The home page for Dalice's testing blog card page"""
    return render(request, 'resume/aboutme.html')





def projects(request): 
    """Show Dalice's projects from projects class"""
    project_list = Project.objects.order_by("project_name")
    context = {'projects' : project_list}
    return render(request, 'resume/projects.html', context)


def experiences(request): 
    """Show Dalice's experiences from experience class"""
    experience_list = Experience.objects.order_by("comp_name")
    context = {'experiences' : experience_list}
    return render(request, 'resume/experiences.html', context)



def skills(request): 
    """Show Dalice's skills from skill class"""
    skill_list = Skill.objects.order_by("skill_name")
    context = {'skills' : skill_list}
    return render(request, 'resume/skills.html', context)



def certifications(request): 
    """Show Dalice's certifications from certification class"""
    certification_list = Certification.objects.order_by("cert_name")
    context = {'certifications' : certification_list}
    return render(request, 'resume/certifications.html', context)



def educations(request): 
    """Show Dalice's education"""
    education_list = Education.objects.order_by("degree")
    context = {'educations' : education_list}
    return render(request, 'resume/educations.html', context)



def volunteers(request): 
    """Show Dalice's volunteer experience"""
    volunteer_list = Volunteer.objects.order_by("organization")
    context = {'volunteers' : volunteer_list}
    return render(request, 'resume/volunteers.html', context)


# Views for comments


def admin_blogs(request): 
    """ A page for blogs to be added by me! """
    blog_list = Blog.objects.order_by('updated_date')
    context = {'blogs' : blog_list}
    return render(request, 'resume/admin_blogs.html', context)



# @login_required
def blogs(request): 
    """ A page for blogs to be added by me! """
    blog_list = Blog.objects.order_by('updated_date')
    context = {'blogs' : blog_list}
    return render(request, 'resume/blogs.html', context)


# @login_required
def blog(request, blog_ID): 
    """Show a single blog entry, and its contents"""
    blog_ = Blog.objects.get(id=blog_ID)
    context = {'blog': blog_}
    print("Context", context)
    return render(request, 'resume/blog.html', context)


 # @login_required
def new_blog(request): 
    """Add a new entry."""
    if request.method != 'POST': 
        # No data submitted, create a blank form.
        form = BlogForm() 

    else: 
    # POST data submitted; process data. 
        form = BlogForm(data = request.POST)
        if form.is_valid(): 
            form.save() 
            return redirect('resume:blogs')
    

    # Display a blank or invlaid form. 
    context = {'form': form}
    return render(request, 'resume/new_blog.html', context)


 # @login_required
def edit_blog(request, blog_ID):
    """Edit an existing entry."""
    blog = Blog.objects.get(id=blog_ID)    

    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = BlogForm(instance=blog)
    else:
        # POST data submitted; process data.
        form = BlogForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume:blog', blog_ID=blog.id)    
    context = {'blog': blog, 'form': form}
    return render(request, 'resume/edit_blog.html', context)
                        

######################## ABOVE TO BE UN-HIGHLIGHTED TO WHEN I AM READY TO INTRODUCT FORMS BACK INTO THE DESIGN.


# @login_required
# def new_entry(request, comment_ID):
#     """Add a new entry for a particular comment."""
#     comment = Comment.objects.get(comment_ID= comment_ID)
    
#     if request.method != 'POST':
#         # No data submitted; create a blank form.
#         form = EntryForm()
#     else:
#         # POST data submitted; process data.
#         form = EntryForm(data=request.POST)
#         if form.is_valid():
#             new_entry = form.save(commit=False)
#             new_entry.comment = comment
#             new_entry.save()
#             return redirect('project_app:comment', comment_ID=comment_ID)
               
#     # Display a blank or invalid form.
#     context = {'comment': comment, 'form': form}
#     return render(request, 'project_app/new_entry.html', context)


