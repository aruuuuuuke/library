from django import forms
from . import models, parser_litres

class ParserForm(forms.Form):
    BOOK_CHOICES = (
        ('litnet', 'litnet'),
        ('mybook', 'mybook'),
    )
    book_type = forms.ChoiceField(choices=BOOK_CHOICES)
    class Meta:
        fields = [
            'book_type',
        ]

    def parser_data(self):
        if self.data['book_type'] == 'litnet':
            file_litnet = parser_litres.parsing()
            for i in file_litnet:
                models.Linet.objects.create(**i)