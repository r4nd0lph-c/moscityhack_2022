from django import forms


class CheckForm(forms.Form):
    own_realty = forms.BooleanField(label='Недвижимость', required=False, initial=False,
                                    widget=forms.CheckboxInput(
                                        attrs={'class': 'form-check-input', 'type': 'checkbox'}))

    own_personal_phnum = forms.BooleanField(label='Личный телефон', required=False, initial=False,
                                            widget=forms.CheckboxInput(
                                                attrs={'class': 'form-check-input', 'type': 'checkbox'}))

    own_work_phnum = forms.BooleanField(label='Рабочий телефон', required=False, initial=False,
                                        widget=forms.CheckboxInput(
                                            attrs={'class': 'form-check-input', 'type': 'checkbox'}))

    own_email = forms.BooleanField(label='Электронная почта', required=False, initial=False,
                                   widget=forms.CheckboxInput(
                                       attrs={'class': 'form-check-input', 'type': 'checkbox'}))

    own_car = forms.BooleanField(label='Машина', required=False, initial=False,
                                 widget=forms.CheckboxInput(
                                     attrs={'class': 'form-check-input', 'type': 'checkbox'}))

    CHOICES_GENDER = [
        ('male', 'Мужчина'),
        ('female', 'Женщина')
    ]
    gender = forms.CharField(label='Пол',
                             widget=forms.RadioSelect(
                                 choices=CHOICES_GENDER,
                                 attrs={'class': '', 'type': 'radio'}))

    CHOICES_FAMILY_STATUS = (
        ('0', 'Холост / Не замужем'),
        ('1', 'В браке'),
        ('2', 'Разведен(а)')
    )
    family_status = forms.ChoiceField(label='Семейный статус', choices=CHOICES_FAMILY_STATUS,
                                      widget=forms.Select(attrs={'class': 'form-select'}))

    CHOICES_INCOME_TYPE = (
        ('0', 'Зарплата'),
        ('1', 'Дивиденты'),
        ('2', 'Взятки')
    )
    income_type = forms.ChoiceField(label='Категория дохода', choices=CHOICES_INCOME_TYPE,
                                    widget=forms.Select(attrs={'class': 'form-select'}))

    CHOICES_EDUCATION_TYPE = (
        ('0', 'Дошкольное'),
        ('1', 'Начальное'),
        ('2', 'Основное общее'),
        ('3', 'Основное специальноее'),
        ('4', 'Высшее')
    )
    education_type = forms.ChoiceField(label='Уровень образования', choices=CHOICES_EDUCATION_TYPE,
                                       initial=CHOICES_EDUCATION_TYPE[2],
                                       widget=forms.Select(attrs={'class': 'form-select'}))

    cnt_children_min = 0
    cnt_children_max = 10
    cnt_children = forms.IntegerField(label='Количество детей',
                                      min_value=cnt_children_min, max_value=cnt_children_max,
                                      widget=forms.NumberInput(
                                          attrs={'type': 'number', 'class': 'form-control',
                                                 'oninput': 'this.previousElementSibling.value = this.value',
                                                 'value': cnt_children_min, 'min': cnt_children_min,
                                                 'max': cnt_children_max}))
    income_total_min = 0
    income_total_max = 99999999
    income_total = forms.IntegerField(label='Годовой доход',
                                      min_value=income_total_min, max_value=income_total_max,
                                      widget=forms.NumberInput(
                                          attrs={'type': 'number', 'class': 'form-control',
                                                 'oninput': 'this.previousElementSibling.value = this.value',
                                                 'value': income_total_min, 'min': income_total_min,
                                                 'max': income_total_max}))


class CharacteristicForm(forms.Form):
    pass
