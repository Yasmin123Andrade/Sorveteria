from django.urls import path

from . import views


urlpatterns = [

    path('', views.listar_pagamentos, name='lista_pagamentos'),

    path('novo/', views.criar_pagamento, name='criar_pagamento'),

    path('<int:pk>/editar/', views.editar_pagamento, name='editar_pagamento'),

    path('<int:pk>/', views.detalhe_pagamento, name='detalhe_pagamento'),

]