from django.urls import path
from .views import product_detail
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('<int:product_id>/', views.product_detail, name='product_detail'),

	path('update_item/', views.updateItem, name="update_item"),


]