from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='views'),
    path('fashion_section/',views.fashion_section,name='fashion_section'),
    path('go_home/',views.go_home,name='go_home'),
    path('search/',views.search,name='search'),
    path('electronics_section/',views.electronics_section,name='electronics_section'),
    path('accessory_section/',views.accessory_section,name='accessory_section'),
    path('view_mens_products/<int:f_id>/',views.view_products,name='view_mens_products'),
    path('view_womens_products/<int:w_id>/',views.view_products,name='view_womens_products'),
    path('view_kids_products/<int:k_id>/',views.view_products,name='view_kids_products'),
    path('view_mobile_products/<int:m_id>/',views.view_products,name='view_mobile_products'),
    path('view_ipad_products/<int:i_id>/',views.view_products,name='view_ipad_products'),
    path('view_laptop_products/<int:l_id>/',views.view_products,name='view_laptop_products'),
    path('view_power_bank_products/<int:p_id>/',views.view_products,name='view_powerbank_products'),
    path('view_watch_products/<int:wh_id>/',views.view_products,name='view_watch_products'),
    path('view_sunglass_products/<int:s_id>/',views.view_products,name='view_powerbank_products'),
    path('view_earphone_products/<int:e_id>/',views.view_products,name='view_powerbank_products'),
    path('view_earring_products/<int:er_id>/',views.view_products,name='view_powerbank_products'),
    path('go_to_mens/',views.go_to_mens),
    path('go_to_womens/',views.go_to_womens),
    path('go_to_kids/',views.go_to_kids),
    path('go_to_mobile/',views.go_to_mobile),
    path('go_to_laptop/',views.go_to_laptop),
    path('go_to_ipad/',views.go_to_ipad),
    path('go_to_power_bank/',views.go_to_power_bank),
    path('go_to_watch/',views.go_to_watch),
    path('go_to_earring/',views.go_to_earring),
    path('go_to_earphone/',views.go_to_earphone),
    path('go_to_sunglass/',views.go_to_sunglass),
    path('show/',views.show),
    path('show/<int:s_id>/',views.show),
    path('see_all/<int:id>/',views.see_all),
    path('cart/<int:p_id>',views.cart),
    path('inc_quantity/<int:id>/',views.inc_quantity),
    path('dec_quantity/<int:id>/',views.dec_quantity),
    path('remove_cart_item/<int:id>/',views.remove_cart_item),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)