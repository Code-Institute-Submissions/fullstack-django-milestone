from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from accounts import views as accounts_views
from products import views as products_views
from cart import views as cart_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accounts_views.home, name='home'),
    path('signup/', accounts_views.register, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/',auth_views.LogoutView.as_view(), name='logout'),
    path('beforelogout/',accounts_views.beforeLogout, name='beforelogout'),
    path('ebook/<int:ebook_id>/', products_views.showEbook, name='ebook'),
    path('add-to-cart/<int:ebook_id>/', cart_views.addToCart, name='add-to-cart'),
    path('delete-item/<int:ebook_id>/', cart_views.deleteItem, name='delete-item'),
    path('delete-item-checkout/<int:ebook_id>/', cart_views.deleteItemCheckout, name='delete-item-checkout'),
    path('checkout/', cart_views.checkout, name='checkout'),
    path('success/', cart_views.successMsg, name='success'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
