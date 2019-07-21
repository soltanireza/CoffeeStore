from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from orders.models import Order, OrderItem


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'نام کاربری تکرار می باشد')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'ایمیل تکرار می باشد')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,
                                                    email=email, password=password)
                    # auth.login(request, user)
                    messages.success(request, 'ثبت نام با موفقیت انجام شد')
                    user.save()
                    return redirect('accounts:login')
        else:
            messages.error(request, "عدم تطابق گذرواژه")
    else:
        return render(request, 'accounts/register.html', {})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password= password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "وارد شدید...")
            return redirect('shop:index')

        else:
            messages.error(request, "Invalid  Credentioals...")
            return redirect('accounts:login')
    else:
        return render(request, 'accounts/login.html')


# def dashboard(request):
#     user_orders = Order.objects.order_by('-created').filter(email=request.user.id)
#     order_items = OrderItem.objects.all()
#
#     context={
#         'user_orders': user_orders,
#         'order_items': order_items
#     }
#     return render(request, 'accounts/dashboard.html', context)


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, "خارج شدید")
    return redirect('shop:index')


