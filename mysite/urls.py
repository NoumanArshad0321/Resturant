# Add an import: from other_app.views import Home
# Add a URL to urlpatterns: path('', Home.as_view(), name='home')
# Including another URLconf
# Import the include() function: from django.urls import include, path
# Add a URL to urlpatterns: path('blog/', include('blog.urls'))

from django.contrib import admin
from django.urls import path
from mysite import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.About, name='about'),
    path('contact/',views.contact, name='contact'),
    path('menu/',views.menu,name='menu'),
    path('',views.homepage),
    path('home/',views.home, name='home'),
    path('userform/',views.userform,name='userform'),
    path('submitform/',views.submitform,name='submitform'),
    path('calculator/',views.calculator,name='calculator'),
    path('evenodd/',views.evenodd,name='evenodd'),
    path('marksheet/',views.marksheet,name='marksheet'),
    path('newsdetail/<slug>', views.newsDetails),
    path('service/',views.service,name='service'),
    ]