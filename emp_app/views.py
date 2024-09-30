from django.shortcuts import render, redirect,HttpResponse
from .models import Employee, Role, Department
from django.http import HttpResponse
from datetime import datetime

def index(request):
    """Render the home page."""
    return render(request, 'index.html')

def all_emp(request):
    """View to display all employees."""
    emps = Employee.objects.all()
    context = {
        'emps': emps  # Correctly passing all employee objects to the template
    }
    return render(request, 'view_all_emp.html', context)

def add_emp(request):
    """View to add a new employee."""
    if request.method == 'POST':
        # Retrieve form data safely using .get()
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        salary = request.POST.get('salary', 0)  # Default to 0 if not provided
        bonus = request.POST.get('bonus', 0)    # Default to 0 if not provided
        phone = request.POST.get('phone')
        dept_id = request.POST.get('dept')
        role_id = request.POST.get('role')

        # Validation and logic go here

        # Create and save the employee
        # ...
        
        return HttpResponse('Employee added successfully')

    elif request.method == 'GET':
        return render(request, 'add_emp.html')

    else:
        return HttpResponse('Invalid request method', status=405)




def remove_emp(request):
    """View to remove an employee."""
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')

        try:
            emp = Employee.objects.get(id=emp_id)
            emp.delete()
            return redirect('all_emp')
        except Employee.DoesNotExist:
            return HttpResponse('Employee not found', status=404)

    return render(request, 'remove_emp.html')

def filter_emp(request):
    """View to filter employees based on criteria."""
    if request.method == 'POST':
        name = request.POST.get('name')
        dept_id = request.POST.get('dept')
        role_id = request.POST.get('role')
        emps = Employee.objects.all()

        if name:
            emps = emps.filter(firstname__icontains=name) | emps.filter(lastname__icontains=name)
        if dept_id:
            emps = emps.filter(dept__id=dept_id)
        if role_id:
            emps = emps.filter(role__id=role_id)
        
        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    return render(request, 'filter_emp.html')
