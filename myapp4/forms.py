# Поля форм
# Перечислим некоторые из наиболее популярных классов Field в Django:
# ● CharField — используется для создания текстовых полей, таких как имя, фамилия, электронная почта и т.д.
# ● EmailField — используется для создания поля электронной почты.
# ● IntegerField — используется для создания поля для ввода целых чисел.
# ● FloatField — используется для создания поля для ввода чисел с плавающей точкой.
# ● BooleanField — используется для создания поля флажка.
# ● DateField — используется для создания поля даты.
# ● DateTimeField — используется для создания поля даты и времени.
# ● FileField — используется для создания поля для загрузки файла.
# ● ImageField — используется для создания поля для загрузки изображения.
# ● ChoiceField — используется для создания выпадающего списка с выбором одного из нескольких вариантов.

from django import forms
import datetime


class UserForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=0, max_value=120)

    def clean_name(self):
        """Плохой пример. Подмена параметра min_length."""

        name = self.cleaned_data['name']
        if len(name) < 3:
            raise forms.ValidationError('Имя должно содержать не менее 3 символов')
        return name

    def clean_email(self):
        email: str = self.cleaned_data['email']

        if not (email.endswith('vk.team') or
                email.endswith('corp.mail.ru')):
            raise forms.ValidationError('Используйте корпоративную почту')
        return email


class ManyFieldsForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField(min_value=18)
    height = forms.FloatField()
    is_active = forms.BooleanField(required=False)
    birthdate = forms.DateField(initial=datetime.date.today)
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')])


'''Виджеты форм
В Django для работы с формами используются виджеты, которые определяют внешний вид и поведение полей формы на странице.
В Django предусмотрены встроенные виджеты, такие как TextInput, Select, CheckboxInput и др., которые можно использовать
для создания различных типов полей формы. Вот некоторые из наиболее популярных классов виджетов в Django:
● TextInput — используется для создания текстового поля ввода.
● EmailInput — используется для создания поля ввода электронной почты.
● PasswordInput — используется для создания поля ввода пароля.
● NumberInput — используется для создания поля ввода чисел.
● CheckboxInput — используется для создания флажка.
● DateInput — используется для создания поля ввода даты.
● DateTimeInput — используется для создания поля ввода даты и времени.
● FileInput — используется для создания поля загрузки файла.
● Select — используется для создания выпадающего списка с выбором одного из нескольких вариантов.
● RadioSelect — используется для создания списка радиокнопок.
● Textarea — используется для создания многострочного текстового поля ввода'''


# Доработанная форма с виджетами
class ManyFieldsFormWidget(forms.Form):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(
                               attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'user@mail.ru'}))
    age = forms.IntegerField(min_value=18, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    height = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(required=False,
                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    birthdate = forms.DateField(initial=datetime.date.today,
                                widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')],
                               widget=forms.RadioSelect(attrs={'class': 'form-check-input'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))


class ImageForm(forms.Form):
    image = forms.ImageField()
