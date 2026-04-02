from django.contrib.auth import authenticate, login, decorators
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views import View
from .forms import PostForm



class IndexClass(View):
    def get(self,request):
        return HttpResponse('Hello')

class LoginClass(View):
    def get(self,request):
        return render(request, 'login.html')

    def post(self,request):
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        my_user = authenticate(username=user_name, password=pass_word)
        if my_user is None:
            return HttpResponse('Khong co user')

        login(request, my_user)
        return render(request, 'success.html')

class UserView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return HttpResponse('Đây là view user')

@decorators.login_required(login_url='/login/')
def viewProduct(request):
    return HttpResponse('View product')


class AddPost(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        f = PostForm()
        return render(request, "addPost.html", {'fm': f})

    def post(self, request):
        f = PostForm(request.POST)
        if not f.is_valid():
            return HttpResponse('Nhập sai rồi')
        print(request.user.get_all_permissions())
        if request.user.has_perm('Login.add_post'):
            f.save()
        else:
            return HttpResponse('Mày không có quyền')
        return HttpResponse(f)