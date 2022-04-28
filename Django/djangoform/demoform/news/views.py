from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View
# Create your views here.

class IndexViews(View):
    def get(self, request):
        return HttpResponse('Xin chào!!!')

class ClassSaveNews(View):
    def get(self, request):
        post_form = PostForm()
        return render(request, 'news/add_news.html', {'f':post_form})

    def post(self,request):
        catch_up = PostForm(request.POST)
        if catch_up.is_valid():
            catch_up.save()
            return HttpResponse('Lưu thành công')
        else:
            return HttpResponse('Lưu không thàn công')

def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html',{'f':b})

def process(request):
    if request.method == 'POST':
        m = SendEmail(request.POST)
        if m.is_valid():
            # tieude = m.cleaned_data['title']
            # cc = m.cleaned_data['cc']
            # noidung = m.cleaned_data['content']
            # email = m.cleaned_data['email']
            # context = {'td':tieude,'c':cc,'b':noidung,'d':email}
            context2 = {'email_data':m}
            return render(request,'news/print_email.html',context2)
    else:
        return HttpResponse('Fail post rồi')