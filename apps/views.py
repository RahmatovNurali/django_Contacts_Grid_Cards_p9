from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView, UpdateView
from django.views.generic.edit import BaseUpdateView, ModelFormMixin

from apps.forms import CustomerForm
# from apps.forms import CustomerForm
from apps.models import Customer


# Create your views here.
class CustomerView(ListView):
    template_name = 'apps/index.html'
    queryset = Customer.objects.all()
    context_object_name = 'customers'


class CustomerAddView(CreateView):
    template_name = 'apps/add.html'
    form_class = CustomerForm
    success_url = reverse_lazy('index_page')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'apps/index.html'
    success_url = reverse_lazy('index_page')


class CustomerUpdateView( UpdateView):
    model = Customer
    fields = '__all__'
    template_name = 'apps/detail.html'
    success_url = reverse_lazy('index_page')


    # https://forum.djangoproject.com/t/reverse-for-with-no-arguments-not-found/14318

    # def form_valid(self, form):
    #     return super().form_valid(form)
    #
    # def form_invalid(self, form):
    #     return super().form_valid(form)

# def add_page(request):
#     context = {
#         'form': CustomerForm()
#     }
#
#     if request.method == 'POST':
#         form = CustomerForm(request.POST)
#         if form.is_valid():
#             form.save()
#         context['form'] = form
#     return render(request, 'apps/add.html', context)
