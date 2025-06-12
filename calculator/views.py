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
        
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = f"Error: Division by zero"
            if result > 100:
                result *= 2
            elif result < 0:
                result += 50
        else:
            result = None
        return render(request, 'calculator/result.html', {'result': result})
    else:
        form = CalculatorForm()
        return render(request, 'calculator/math_form.html', {'form': form})