from django.shortcuts import render
from .forms import CalculatorForm

# Create your views here.
def calculate_view(request):
    result = None
    
    if request.method == 'POST':
        form = CalculatorForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['input1']
            num2 = form.cleaned_data['input2']
            operator = form.cleaned_data['operator']
        
            if operator == '/' and num2 == 0:
                form.add_error('input2', 'Division by zero is not allowed.')
            else:
                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/':
                    result = num1 / num2

                if result is not None:
                    if result > 100:
                        result *= 2
                    elif result < 0:
                        result += 50

        return render(request, 'calculator/result.html', {'form': form, 'result': result})
    else:
        form = CalculatorForm()
        return render(request, 'calculator/math_form.html', {'form': form})