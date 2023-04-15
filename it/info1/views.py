from django.shortcuts import render, redirect
from info1.models import User_name, User_birth, User_info, User_work, Practice, Criminal, Medicine
from info1.forms import CreateNameForm, CreateBirthForm, CreateInfoForm, CreateWorkForm, CreatePracticeForm, CreateCriminalForm, CreateMedicineForm

def index_page(request):
    if request.user.is_authenticated:
        user_names = User_name.objects.filter(owner_id=request.user.id)
        return render(request, 'info1/index.html', {'user_names': user_names, 'user': request.user})
    else:
        return redirect('/auth/login/')


def create_name(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = CreateNameForm()
            return render(request, 'info1/create-name.html', {'form': form})
        if request.method == 'POST':
            form = CreateNameForm(request.POST)
            if form.is_valid():
                firstname = form.data.get('firstname')
                secondname = form.data.get('secondname')
                user_name = User_name(firstname=firstname, secondname=secondname, owner_id=request.user.id)
                user_name.save()
                return redirect('/')
            else:
                return render(request, 'info1/create-name.html', {'form': form})
    else:
        return redirect('/auth/login/')


def user_name_details(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        user_births = User_birth.objects.filter(user_name_id=pk).order_by('-created_at')
        user_infos = User_info.objects.filter(user_name_id=pk).order_by
        user_works = User_work.objects.filter(user_name_id=pk).order_by
        practices = Practice.objects.filter(user_name_id=pk).order_by
        criminals = Criminal.objects.filter(user_name_id=pk).order_by
        medicines = Medicine.objects.filter(user_name_id=pk).order_by
        form = CreateBirthForm()
        form1 = CreateInfoForm()
        form2 = CreateWorkForm()
        form3 = CreatePracticeForm()
        form4 = CreateCriminalForm()
        form5 = CreateMedicineForm()
        return render(request, 'info1/user-name-details.html', {'user_name': user_name, 'user_births':user_births, 'user_infos':user_infos, 
            'user_works':user_works, 'practices':practices, 'criminals':criminals, 'medicines':medicines, 'form':form, 'form1':form1, 'form2':form2, 
                                            'form3':form3, 'form4':form4, 'form5':form5})
    else:
        return redirect('/auth/login/')
    
def user_names_user_birth_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateBirthForm(request.POST)
            if form.is_valid():
                date_of_birth = form.data.get('date_of_birth')
                place_of_birth = form.data.get('place_of_birth')
                user_birth = User_birth(date_of_birth=date_of_birth, place_of_birth=place_of_birth, user_name_id=pk)
                user_birth.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def user_info_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateInfoForm(request.POST)
            if form.is_valid():
                specialization = form.data.get('specialization')
                orga_of_education = form.data.get('orga_of_education')
                year_of_graduation = form.data.get('year_of_graduation')
                user_info = User_info(specialization=specialization,orga_of_education=orga_of_education,
                                       year_of_graduation=year_of_graduation, user_name_id=pk)
                user_info.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')


def delete_birth(request, pk):
    if request.user.is_authenticated:
        user_birth = User_birth.objects.get(id=pk)
        user_name = User_name.objects.get(id=user_birth.user_name.id)
        if user_name.owner.id == request.user.id:
            user_birth.delete()
            return redirect('/info1/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')


def delete_user_name(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if user_name.owner.id == request.user.id:
            user_name.delete()
            return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def delete_info(request, pk):
    if request.user.is_authenticated:
        user_info = User_info.objects.get(id=pk)
        user_name = User_name.objects.get(id=user_info.user_name.id)
        if user_name.owner.id == request.user.id:
            user_info.delete()
            return redirect('/info1/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def user_work_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateWorkForm(request.POST)
            if form.is_valid():
                address = form.data.get('address')
                organization = form.data.get('organization')
                user_work = User_work(address=address,organization=organization, user_name_id=pk)
                user_work.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def delete_work(request, pk):
    if request.user.is_authenticated:
        user_work = User_work.objects.get(id=pk)
        user_name = User_name.objects.get(id=user_work.user_name.id)
        if user_name.owner.id == request.user.id:
            user_work.delete()
            return redirect('/info1/' + str(user_name.id) + '/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def practice_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreatePracticeForm(request.POST)
            if form.is_valid():
                experience = form.data.get('experience')
                practice = Practice(experience=experience, user_name_id=pk)
                practice.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def criminal_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateCriminalForm(request.POST)
            if form.is_valid():
                criminal_record = form.data.get('criminal_record')
                criminal = Criminal(criminal_record=criminal_record, user_name_id=pk)
                criminal.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')
    
def medicine_create(request, pk):
    if request.user.is_authenticated:
        user_name = User_name.objects.get(id=pk)
        if request.method == 'POST':
            form = CreateMedicineForm(request.POST)
            if form.is_valid():
                medicine_number = form.data.get('medicine_number')
                medicine_date = form.data.get('medicine_date')
                medicine = Medicine(medicine_number=medicine_number, medicine_date=medicine_date, user_name_id=pk)
                medicine.save()
                return redirect('/info1/' + str(user_name.id) + '/')
            else:
                return redirect('/')
        else:
            return redirect('/')
    else:
        return redirect('/auth/login/')