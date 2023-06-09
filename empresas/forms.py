from django import forms

from empresas.models import Company, Jobs, Specializations, Technologies


class CadastroEmpresa(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'email': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'headquarters': forms.TextInput(attrs={'class': 'form-control mb-3'}),
            'company_size': forms.Select(attrs={'class': 'form-control mb-3'}),
            'marketing_niche': forms.Select(attrs={'class': 'form-control mb-3'}),
            'logo': forms.FileInput(attrs={'class': 'form-control mb-3l'}),
        }

    technologies = forms.ModelMultipleChoiceField(
        queryset= Technologies.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    specializations = forms.ModelMultipleChoiceField(
        queryset= Specializations.objects.all(),
        widget = forms.CheckboxSelectMultiple
    )

    def clean_logo(self):
        data =  self.cleaned_data.get('logo')
        filesize= data.size
    
        if filesize > 100_000_000:
            raise forms.ValidationError("You cannot upload file more than 10Mb")
        else:
            return data

class CadastroVaga(forms.ModelForm):
    
    class Meta:
        model = Jobs
        fields = '__all__'

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control mb-3'}),
                'experience': forms.Select(attrs={'class': 'form-control mb-3'}),
                'url': forms.URLInput(attrs={'class': 'form-control mb-3'}),
                'final_date': forms.DateInput(attrs={'class': 'form-control mb-3'}),
                'position_type': forms.NumberInput(attrs={'class': 'form-control mb-3'}),
                'statues': forms.Select(attrs={'class': 'form-control mb-3l'}),
            }