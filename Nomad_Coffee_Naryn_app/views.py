from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UpdateUserForm, UpdateProfileForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView
import datetime



from .models import *
from .forms import *
from django.db.models import Q


def index(request):
    base_menu = BaseMenu.objects.all()

    return render(request, 'Nomad_Coffee_Naryn_app/index.html', {"base_menu": base_menu})


def menu(request, category_slug=None):
    category = None
    menu_cat = Menu_Category.objects.all()
    menu = Menu.objects.all()
    if category_slug:
        category = get_object_or_404(Menu_Category, slug=category_slug)
        menu = menu.filter(category=category)

    return render(request, 'Nomad_Coffee_Naryn_app/menu.html',
                  {'category': category, 'menu_cat': menu_cat, 'menu': menu})

def menu_detail(request, id, slug):
    menu_detail = get_object_or_404(Menu, id=id, slug=slug)
    return render(request, 'Nomad_Coffee_Naryn_app/menu_detail.html', {"menu_detail":menu_detail})

def about(request):
    return render(request, 'Nomad_Coffee_Naryn_app/about.html')

def special_menu(request):
    return render(request, 'Nomad_Coffee_Naryn_app/special_menu.html')

def contact(request):
    if request.method == "POST":
        form = ContactsForm(request.POST)
        if form.is_valid():
            data = form.save()
            return redirect('index')
    else:
        form = ContactsForm()
    return render(request, 'Nomad_Coffee_Naryn_app/contact.html', {"form": form})


class LoginView(TemplateView):
    template_name = "Nomad_Coffee_Naryn_app/login.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        if request.method == 'POST':
            username = request.POST['name']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Вы успешно вошли в систему')
                return redirect("/")
            else:
                context['error'] = "Логин или пароль неправильные"
        return render(request, self.template_name, context)


class LogOutView(TemplateView):
    template_name = "Nomad_Coffee_Naryn_app/index.html"

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Вы успешно вышли из системы')
        return render(request, self.template_name)




class RegisterView(TemplateView):
    template_name = "Nomad_Coffee_Naryn_app/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password)
                messages.success(request, 'Вы успешно зарегистрировались')
                return redirect(reverse("login"))

        return render(request, self.template_name)




class ProfilePage(TemplateView):
    template_name = "Nomad_Coffee_Naryn_app/profile.html"


def userpage(request):
	user_form = UserForm(instance=request.user)
	profile_form = ProfileForm(instance=request.user.profile)
	return render(request=request, template_name="Nomad_Coffee_Naryn_app/user.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })



@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'Nomad_Coffee_Naryn_app/profile.html', {'user_form': user_form, 'profile_form': profile_form})


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'Nomad_Coffee_Naryn_app/change_password.html'
    success_message = "Пароль успешно обновлено!"
    success_url = reverse_lazy('index')



class MenuDetailView(DetailView):
    model = Menu
    query_pk_and_slug = True