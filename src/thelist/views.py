from django.views.generic.base import TemplateView

# Create your views here.


class ViewOrderList(TemplateView):
    template_name = "thelist/order-list.html"
