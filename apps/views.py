from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from apps.models import Wallet, Category


def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    context = Wallet.user_balance(request.user)
    return render(request, 'app/home/home-page.html', context)



def income(request):
    if not request.user.is_authenticated:
        return redirect('login')

    categories = Category.objects.all()

    if request.method == "POST":
        amount = request.POST.get("amount").strip('$ ')
        category_id = request.POST.get("category_id")
        description = request.POST.get("description")

        try:
            category = Category.objects.get(pk=category_id)
            Wallet.objects.create(
                user=request.user,
                amount=amount,
                description=description,
                category=category,
                status="income"
            )
            messages.success(request, "Income added")
            return redirect('home')
        except Category.DoesNotExist:
            messages.error(request, "Category not found")

    return render(request, 'app/Income/income.html', {'categories': categories, 'status': 'income'})

def expenses(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == "GET":
        categories = Category.objects.filter(type="expenses")
        return render(request, 'app/Expenses/expenses.html', {'categories':categories})

    if request.method == "POST":
        amount = request.POST.get("amount").strip("$ ")
        category_id = request.POST.get("category_id")
        description = request.POST.get("description")
        date = request.POST.get("date")
        category = Category.objects.get(pk=category_id)
        Wallet.objects.create(user=request.user, amount=amount, date=date, description=description, category=category, status="expense")
        messages.success(request, "Expense added successfully")
        return redirect('home')

#
# class RegisterFormView(View):
#     template_name = 'app/Register/register.html'
#
#     def get(self, request):
#         return render(request, self.template_name)
#
#     def post(self, request):
#         data = dict(request.POST.items())
#         del data['csrfmiddlewaretoken']
#         username = data.get('username')
#         data['password'] = make_password(data.get('password'))
#
#         if not User.objects.filter(username=username).exists():
#             User.objects.create(**data)
#         else:
#             messages.error(request, 'Already username exists!')
#
#         return redirect('login')
#
#
# class LoginFormView(View):
#     template_name = 'app/Register/login.html'
#
#     def get(self, request):
#         return render(request, self.template_name)
#
#     def post(self, request):
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = User.objects.filter(username=username).first()
#
#         if user and check_password(password, user.password):
#             login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#             return redirect('home')
#         else:
#             messages.error(request, "Username or Password invalid!")
#             return redirect('login')
#
#
# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect('login')
def register_form_view(request):
    if request.method == "GET":
        return render(request , 'app/Register/register.html')

    if request.method == "POST":
        data = dict(request.POST.items())
        del data['csrfmiddlewaretoken']
        username = data.get('username')
        data['password'] = make_password(data.get('password'))
        user = User.objects.filter(username=username)
        if not user.exists():
            User.objects.create(**data)
        else:
            messages.error(request , 'Already username exists!')
        return redirect('login')


def login_form_view(request):
    if request.method == "GET":
        return render(request , 'app/Register/login.html')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(username=username)
        if user.exists():
            user = user.first()
            if check_password(password , user.password):
                login(request , user,backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')
            else:
                messages.error(request , "Username or Password invalid !")
        else:
            messages.error(request , "Not Found account")
        return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')

