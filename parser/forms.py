from django import  forms
from  . import models, parser

class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('rezka', 'rezka'),
        ('ts', 'ts'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)
    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'rezka':
            file_rezka = parser.parsing()
            for i in file_rezka:
                models.Rezka.objects.create(**i)

