from django.shortcuts import render

# Create your views here.

def info(request):
    teacher = "킹갓갓동주"
    student = ['방대승', '김재현', '임우섭', '조동빈', '박진홍', '이수진']
    context = {
        'Teacher': teacher,
        'Student': student,
    }
    return render(request, 'info.html', context)

def student(request,name):
    age = 28
    context = {
        'name': name,
        'ages': age,
    }
    return render(request, 'student.html', context)