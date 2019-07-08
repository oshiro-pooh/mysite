from django import forms
from .models import Pref, City

class PostForm(forms.ModelForm):
    prefs = forms.ModelChoiceField(
    label='都道府県名',
    queryset=Pref.objects,
    empty_label='',
    )
    
    class Meta:
        model = Pref
        fields = '__all__'
        
    cities = forms.ModelChoiceField(
    label='市町村名',
    queryset=Pref.objects.none(),
    empty_label='',
    to_field_name="city_id",
    required=False
    )
    
    class Meta:
        model = City
        fields = '__all__'
        
    def clean(self) :
        # 入力されたデータを取得
        prefs = self.cleaned_data.get('prefs')
        cities = self.cleaned_data.get('cities')
        
        # TODO チェックメソッド追加 
        #if (prefs and not cities) :
        #  raise forms.ValidationError("市町村を選んだください")

        
        return self.cleaned_data
