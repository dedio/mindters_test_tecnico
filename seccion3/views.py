# Escriba una vista basada en clases en Django 
# que liste todos los objetos de un modelo Producto.
# La vista debe usar paginación para mostrar 10 productos por página.

from django.views.generic import ListView
from .models import Producto
from django.core.paginator import Paginator

class ListaProductos(ListView):
    model = Producto
    template_name = 'lista_productos.html'
    context_object_name = 'productos'

    def get_queryset(self):
        return Producto.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productos = context['productos']
        paginator = Paginator(productos, 10)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['page_obj'] = page_obj
        return context
