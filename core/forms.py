import json

from django import forms

from core.models import DataSet


class DataSetForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        try:
            return json.loads(self.cleaned_data['file'].read().decode())
        except (ValueError, TypeError):
            raise forms.ValidationError('Invalid JSON file')

    def save(self):
        data = self.cleaned_data['file']
        if not isinstance(data, list):
            data = [data]
        # we can't bulk_create here because of
        # post_save signal won't work
        for data_set in data:
            DataSet.objects.create(input=json.dumps(data_set))
