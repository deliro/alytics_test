import json
from collections.abc import Mapping, Sequence

from django import forms

from core.models import DataSet


class DataSetForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        try:
            data = json.loads(self.cleaned_data['file'].read().decode())
            if not isinstance(data, Sequence):
                raise forms.ValidationError('JSON file must contain list in the root')
            if not all(isinstance(chunk, Mapping) for chunk in data):
                raise forms.ValidationError('JSON file must contain list of dicts')
            return data
        except (ValueError, TypeError):
            raise forms.ValidationError('Invalid JSON file')

    def save(self):
        return DataSet.objects.create(input=json.dumps(self.cleaned_data['file']))
