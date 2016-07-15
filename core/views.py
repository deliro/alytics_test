from django.core.urlresolvers import reverse_lazy
from django.views import generic

from core.forms import DataSetForm
from core.models import DataSet


class DataSetList(generic.FormView):
    template_name = 'core/dataset_list.html'
    form_class = DataSetForm
    success_url = reverse_lazy('dataset_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        kwargs['object_list'] = DataSet.objects.order_by('-pk')
        kwargs['status'] = DataSet.get_last_status()
        return super().get_context_data(**kwargs)
