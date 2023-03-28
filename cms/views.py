from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.views.generic import *
# from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

@method_decorator(login_required(login_url='/admin/login/'), name='dispatch')
class PostCreateView(CreateView):
    template_name = "insert.html"
    model = Post
    fields = ['title']
    exclude = ('author',)
    success_url = "/"
    def form_valid(self,request, form):
         form.user = request.user
         form.save()
         return super().form_valid(form)
    
class PostView(ListView):
     template_name = "index.html"
     context_object_name = 'post'

     slug = None
     def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PostView, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
     
     # if slug is not None:
     def get_queryset(self):
     #    id = self.kwargs['category_id']
        return Post.objects.all()

def search(r,id):
    data = {
        'category' : Category.objects.all(),
        'post' : Post.objects.filter(category=id)
    }

    return render(r,'index.html',data)

     


