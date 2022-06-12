from django import forms
from datetime import datetime
from .models import *


class CharacteristicForm(forms.Form):
    # gender

    CHOICES_GENDER = (
        ('male', 'Мужчина'),
        ('female', 'Женщина')
    )
    gender = forms.ChoiceField(choices=CHOICES_GENDER,
                               initial=CHOICES_GENDER[0],
                               widget=forms.RadioSelect(
                                   attrs={'class': 'inline'}
                               ))

    # checkboxes

    flag_own_realty = forms.BooleanField(label='Имеет недвижимость', required=False, initial=False,
                                         widget=forms.CheckboxInput(
                                             attrs={'class': 'form-check-input', 'type': 'checkbox'}))

    flag_own_car = forms.BooleanField(label='Имеет автомобиль', required=False, initial=False,
                                      widget=forms.CheckboxInput(
                                          attrs={'class': 'form-check-input', 'type': 'checkbox'}))

    flag_personal_phone = forms.BooleanField(label='Указал(а) личный телефон', required=False, initial=False,
                                             widget=forms.CheckboxInput(
                                                 attrs={'class': 'form-check-input', 'type': 'checkbox'}))

    flag_work_phone = forms.BooleanField(label='Указал(а) рабочий телефон', required=False, initial=False,
                                         widget=forms.CheckboxInput(
                                             attrs={'class': 'form-check-input', 'type': 'checkbox'}))

    flag_email = forms.BooleanField(label='Указал(а) электронную почту', required=False, initial=False,
                                    widget=forms.CheckboxInput(
                                        attrs={'class': 'form-check-input', 'type': 'checkbox'}))

    flag_employed = forms.BooleanField(label='Трудоустроен', required=False, initial=False,
                                       widget=forms.CheckboxInput(
                                           attrs={'class': 'form-check-input', 'type': 'checkbox'}))

    flag_is_pensioner = forms.BooleanField(label='Пенсионер', required=False, initial=False,
                                           widget=forms.CheckboxInput(
                                               attrs={'class': 'form-check-input', 'type': 'checkbox'}))

    flag_is_resident = forms.BooleanField(label='Резидент РФ', required=False, initial=False,
                                          widget=forms.CheckboxInput(
                                              attrs={'class': 'form-check-input', 'type': 'checkbox'}))

    # input fields

    lifetime = 100
    current_year = datetime.now().year
    CHOICES_BIRTH_YEAR = [(str(i), str(i)) for i in range(current_year - lifetime, current_year + 1)]
    birth_year = forms.ChoiceField(label='Год рождения', choices=CHOICES_BIRTH_YEAR,
                                   initial=CHOICES_BIRTH_YEAR[-1],
                                   widget=forms.Select(attrs={'class': 'form-select'}))

    CITIES = Cities.objects.all()
    city = forms.ModelChoiceField(label='Город', initial=CITIES.get(name="Москва"),
                                  queryset=CITIES,
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

    # CHOICES_INCOME_TYPE = (
    #     ('0', 'Зарплата'),
    #     ('1', 'Дивиденты'),
    #     ('2', 'Взятки')
    # )
    # income_type = forms.ChoiceField(label='Категория дохода', choices=CHOICES_INCOME_TYPE,
    #                                 widget=forms.Select(attrs={'class': 'form-select'}))

    salary_min = 0
    salary_max = 999999999
    salary = forms.IntegerField(label='Зарплата',
                                min_value=salary_min, max_value=salary_max,
                                widget=forms.NumberInput(
                                    attrs={'type': 'number', 'class': 'form-control',
                                           'value': salary_min, 'min': salary_min,
                                           'max': salary_max}))

    income_total_min = 0
    income_total_max = 99999999
    income_total = forms.IntegerField(label='Годовой доход',
                                      min_value=income_total_min, max_value=income_total_max,
                                      widget=forms.NumberInput(
                                          attrs={'type': 'number', 'class': 'form-control',
                                                 'value': income_total_min, 'min': income_total_min,
                                                 'max': income_total_max}))

    CHOICES_FAMILY_STATUS = (
        ('0', 'Холост / Не замужем'),
        ('1', 'В браке'),
        ('2', 'Разведен(а)')
    )
    family_status = forms.ChoiceField(label='Семейный статус', choices=CHOICES_FAMILY_STATUS,
                                      widget=forms.Select(attrs={'class': 'form-select'}))

    cnt_dependent_min = 0
    cnt_dependent_max = 10
    cnt_dependent = forms.IntegerField(label='Количество иждивенцев',
                                       min_value=cnt_dependent_min, max_value=cnt_dependent_max,
                                       widget=forms.NumberInput(
                                           attrs={'type': 'number', 'class': 'form-control',
                                                  'value': cnt_dependent_min, 'min': cnt_dependent_min,
                                                  'max': cnt_dependent_max}))

    cnt_children_min = 0
    cnt_children_max = 10
    cnt_children = forms.IntegerField(label='Количество детей',
                                      min_value=cnt_children_min, max_value=cnt_children_max,
                                      widget=forms.NumberInput(
                                          attrs={'type': 'number', 'class': 'form-control',
                                                 'value': cnt_children_min, 'min': cnt_children_min,
                                                 'max': cnt_children_max}))

    family_income_min = 0
    family_income_max = 999999999
    family_income = forms.IntegerField(label='Семейный доход',
                                       min_value=family_income_min, max_value=family_income_max,
                                       widget=forms.NumberInput(
                                           attrs={'type': 'number', 'class': 'form-control',
                                                  'value': family_income_min, 'min': family_income_min,
                                                  'max': family_income_max}))
