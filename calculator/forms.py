from django import forms

class CalculatorForm(forms.Form):
    input1 = forms.IntegerField(label='Enter a nunmber1.', required=True)
    input2 = forms.IntegerField(label='Enter a nunmber2.', required=True)

    OPERATOR_LIST = [
        ('+', 'Add (+)'),
        ('-', 'Subtract (−)'),
        ('*', 'Multiply (×)'),
        ('/', 'Divide (÷)'),
    ]
    
    operator = forms.ChoiceField(
        label='Select the operator.',
        choices=OPERATOR_LIST,
        widget=forms.Select
    )