from django.shortcuts import render, redirect
from django.views import View
from .models import UserModel
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class UserView(View):
    model = UserModel

    def get(self, request):
        data_users = self.model.objects.all()

        return render(request, 'user/index.html', {'data_users': data_users})


class CreateUser(View):
    @staticmethod
    def get(request):
        return render(request, 'user/create.html')

    @staticmethod
    def post(request):
        data = UserForm(request.POST)

        if data.is_valid():
            UserModel.objects.create_user(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                                          email=request.POST['email'], password=request.POST['password'],
                                          username=request.POST['username'], phone=request.POST['phone'],
                                          address=request.POST['address'])
            messages.success(request, 'Create successfully !!!')
        else:
            messages.error(request, 'Create failed !!!')

        return redirect('create')

def edit_user(request, id):
    data_user = UserModel.objects.get(pk=id)
    return render(request, 'user/edit.html', {'user': data_user})

def update_user(request, id):
    data_user = UserModel.objects.get(pk=id)
    # if request.POST['id'] is not None:
    #     data_user = UserModel.objects.get(pk=id)
    # data = UserForm(request.POST)
    # print(id)

    if request.POST['id'] is not None:
        #     UserModel.objects.create_user(first_name=request.POST['first_name'], last_name=request.POST['last_name'],
        #                                   email=request.POST['email'], password=request.POST['password'],
        #                                   username=request.POST['username'], phone=request.POST['phone'],
        #                                   address=request.POST['address'])
        messages.success(request, 'Update successfully !!!')
    else:
        messages.error(request, 'Update failed !!!')

    return redirect('edit')

def delete_user(request, id):
    data_user = UserModel.objects.get(pk=id)
    if data_user is not None:
        data_user.delete()
        messages.success(request, 'Delete successfully !!!')
    else:
        messages.error(request, 'Delete failed !!!')

    return redirect('list')


class Auth(View):
    @staticmethod
    def get(request):
        return render(request, 'user/login.html')

    @staticmethod
    def post(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login success !!!')

            return redirect('list')
        else:
            messages.error(request, 'username or password wrong !!!')

            return redirect('login')


def logout_request(request):
    logout(request)

    return redirect('login')
