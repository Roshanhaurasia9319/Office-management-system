from django.shortcuts import render, redirect, HttpResponse
from .models import Employee, Department, Role
from django.http import HttpResponseBadRequest
from .models import Employee, Department, Role
from django.core.exceptions import ValidationError
from django.db.models import Q
# Create your views here.

def authenticate(request):
    if request.method == 'POST':
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        if Password == "welcome1" and Username == "Officer":
            return redirect(index)
        else:
            return HttpResponse("Password is incorrect! TRY AGAIN")
    
    
    return render(request, "authenticate.html")




def index(request, emp_id=0):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    return render(request, "index.html", context)









def view_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps':emps
    }
    
    return render(request, "view_emp.html", context)


def add_emp(request):
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        dept_id = request.POST.get('dept')
        salary = request.POST.get('salary')
        bonus = request.POST.get('bonus')
        role_id = request.POST.get('role')
        phone = request.POST.get('phone')
        hire_date = request.POST.get('hire_date')

        # Basic form validation
        if not all([first_name, last_name, dept_id, role_id, phone, hire_date]):
            return HttpResponseBadRequest("Missing required fields")

        try:
            salary = int(salary) if salary else 0
            bonus = int(bonus) if bonus else 0
        except ValueError:
            return HttpResponseBadRequest("Invalid input for salary or bonus")

        # Create and save the new employee
        try:
            dept = Department.objects.get(id=dept_id)
            role = Role.objects.get(id=role_id)
            new_emp = Employee(first_name=first_name, last_name=last_name, dept=dept, salary=salary, bonus=bonus,
                role=role, phone=phone, hire_date=hire_date)
            new_emp.save()
            return redirect("view_emp")
        except (Department.DoesNotExist, Role.DoesNotExist, ValidationError) as e:
            return HttpResponseBadRequest(f"Error saving employee: {e}")
        
    departments = Department.objects.all()
    roles = Role.objects.all()
        
    return render(request, "add_emp.html",{'departments': departments, 'roles': roles})

def remove_emp(request, emp_id = 0):
    
    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return redirect(view_emp)
        except:
            return HttpResponse("Please select valid id")
    
    emps = Employee.objects.all()
    context ={
        'emps' : emps
    }
    return render(request, "remove_emp.html", context)


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        dept = request.POST.get('dept', '').strip()
        role = request.POST.get('role', '').strip()

        emps = Employee.objects.all()

        if name:
            emps = emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
            print(f"Filtered by name: {name}, Result count: {emps.count()}")  # Debugging

        # if dept:
        #     emps = emps.filter(dept__name=dept)
        #     print(f"Filtered by dept: {dept}, Result count: {emps.count()}")  # Debugging

        # if role:
        #     emps = emps.filter(role__name=role)
        #     print(f"Filtered by role: {role}, Result count: {emps.count()}")  # Debugging

        context = {
            'emps': emps,
            'departments': Department.objects.all(),  # To retain the filter options in the form
            'roles': Role.objects.all(),  # To retain the filter options in the form
        }
        return render(request, "view_emp.html", context)

    elif request.method == "GET":
        departments = Department.objects.all()
        roles = Role.objects.all()
        return render(request, "filter_emp.html", {'departments': departments, 'roles': roles})

    else:
        return HttpResponse("An error occurred")

# Note: Don't forget to import necessary modules like Q, Employee, Department, and Role at the top of your file.
