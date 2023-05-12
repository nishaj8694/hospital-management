from django.shortcuts import render,redirect,HttpResponse
from .models import DoctorProfile
from django.db.models import Prefetch
from admn.models import Product,varient
from home.models import Appointment,treatment,TreatMedicine
from .forms import doc_form
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required(login_url='home:signin')
def doc_dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_docter:
            Pr_no=Product.objects.count()
            My_no=Appointment.objects.filter(docter__user_id=request.user.id , status='finish').count()
            P_no=Appointment.objects.filter( status='finish').count()
            AP_no=Appointment.objects.filter(docter__user_id=request.user.id ).count()
            
            docter=DoctorProfile.objects.get(user_id=request.user.id)
            # print(docter.image,docter.badge_id)
            if docter is None:
                print('iam in docter')
                docter=DoctorProfile(user_id=request.user.id)
                docter.save()
                docter=DoctorProfile.objects.filter(user_id=request.user.id)
                context={'docter':docter,'Pr_no':Pr_no,'My_no':My_no,'P_no':P_no,'AP_no':AP_no}
                return render(request,'doc_home.html',context)
            
            if docter.image !=None and docter.badge_id !=None:
                print('iam home doc') 
                context={'docter':docter,'Pr_no':Pr_no,'My_no':My_no,'P_no':P_no,'AP_no':AP_no}
                return render(request,'doc_home.html',context)
            
            if docter.image == None or docter.badge_id == None:
                print('iam home doc') 
                context={'docter':docter,'Pr_no':Pr_no,'My_no':My_no,'P_no':P_no,'AP_no':AP_no}
                return render(request,'doc_home.html',context)
            
            context={'docter':docter,'Pr_no':Pr_no,'My_no':My_no,'P_no':P_no,'AP_no':AP_no}
            return render(request,'doc.html',context)
             
        return redirect('signin')      
       
    return redirect('signin')      

@login_required(login_url='home:signin')
def doc_profile(request):
    if request.method=='POST':
        form=doc_form(request.POST , request.FILES)
        # print('halo')
        if form.is_valid():
            # print('halo')
            docter=DoctorProfile.objects.get(user_id=request.user.id)
            if docter:
                docter.specialization=form.instance.specialization
                docter.gender=form.instance.gender
                docter.image=form.instance.image
                docter.department=form.instance.department
                docter.address=form.instance.address
                docter.residence=form.instance.residence
                docter.contact_number='+91'+form.instance.contact_number
                docter.badge_id=form.instance.badge_id
                docter.save()
                return redirect('docter:doc_dashboard')
            else:
                return redirect('docter:doc_dashboard')
        else:
            print('else woe')    
            return redirect('docter:doc_dashboard')    
          

    else:
        docter=DoctorProfile.objects.get(user_id=request.user.id)
        form=doc_form()
        return render(request,'doc_profile.html',{'form':form,'docter':docter})

@login_required(login_url='home:signin')
def doc_edit_profile(request):
    if request.method=='POST':
        form=doc_form(request.POST , request.FILES)
        # print('halo')
        if form.is_valid():
            # print('halo')
            try:
                docter=DoctorProfile.objects.get(user_id=request.user.id)
            except:               
               return render(request,'doc_home.html')
                     
            if docter:
                docter.specialization=form.instance.specialization
                docter.gender=form.instance.gender
                docter.image=form.instance.image
                docter.department=form.instance.department
                docter.address=form.instance.address
                docter.residence=form.instance.residence
                docter.contact=form.instance.contact
                docter.badge_id=form.instance.badge_id
                docter.save()
                return redirect('docter:doc_dashboard')
                
        else:
            return redirect('docter:doc_dashboard')
            

    else:
        profile=DoctorProfile.objects.get(user_id=request.user.id)
        form=doc_form(instance=profile)
        return render(request,'doc_profile.html',{'form':form,'docter':profile})    
    
@login_required(login_url='home:signin')
def doc_Product(request):
      
      product=Product.objects.prefetch_related(Prefetch('item',queryset=varient.objects.all()))
      docter=DoctorProfile.objects.get(user_id=request.user.id)
      print(docter)
      context={'product':product,'docter':docter} 
      return render(request,'doc_Product.html',context)

@login_required(login_url='home:signin')
def doc_appointment(request):

    doct=DoctorProfile.objects.get(user=request.user)
    print(doct.id)
    Patient_list=Appointment.objects.filter(docter_id=doct.id)
    print(Patient_list)
    docter=DoctorProfile.objects.get(user_id=request.user.id)
    context={'Appointment':Patient_list,'docter':docter}
    return render(request,'doc_appointment.html',context)

@csrf_exempt
def update_is_available(request):
    if request.method=='POST':
        id=request.POST.get('item_id')
        is_available=request.POST.get('is_available')
        docter=DoctorProfile.objects.get(id=id)
        print(is_available)
        if is_available =='true':
            print("true")
            docter.is_available = True
            docter.save()
        else:
            print("false")
            docter.is_available = False
            docter.save()    
        return JsonResponse({'is_available': docter.is_available})
    
    else:
        return JsonResponse({'error': 'Invalid request method.'})




def today_appointment(request):
    today=datetime.now().date()
    doct=DoctorProfile.objects.get(user=request.user)
    Patient_list=Appointment.objects.filter(docter_id=doct.id,appointment_date=today)
    docter=DoctorProfile.objects.filter(user_id=request.user.id)
    context={'Appointment':Patient_list,'docter':docter,'today':today}
    return render(request,'doc_appointment.html',context)

@login_required(login_url='home:signin')
def accept(request,id):
    try:
       appoiment=Appointment.objects.get(id=id)
       if appoiment.status != 'finish':
             appoiment.status='accept'
             appoiment.save()
             return redirect('docter:doc_appointment')
       return redirect('docter:doc_appointment')
    except:
       return redirect('docter:doc_appointment')

    
@login_required(login_url='home:signin')
def reject(request,id):
    appoiment=Appointment.objects.get(id=id)
    if appoiment.status != 'finish':
        appoiment.status='reject'
        appoiment.save()
        return redirect('docter:doc_appointment')
    return redirect('docter:doc_appointment')

@login_required(login_url='home:signin')    
def finish(request,id):
    appoiment=Appointment.objects.get(id=id)
    if appoiment.status != 'finish':
        appoiment.status='finish'
        appoiment.save()
        id=appoiment.id
        return redirect('docter:prescribe',id)
    return redirect('docter:doc_appointment')

@login_required(login_url='home:signin')    
def prescribe(request,id):
    id=id
    if request.method=='POST':
        symtems= request.POST['symtems']
        medicines_id = request.POST.getlist('av1') 
        # print(medicines_id)
        # print(qt)
        tret = treatment(appointment_id=id, symtems=symtems)
        tret.save()
        print('its not ',tret.id)
        for i in range(len(medicines_id)):
            med=TreatMedicine(Treatment=tret,medicine_id=int(medicines_id[i]))
            med.save()
            # print(med)
        # medic = varient.objects.filter(id__in=medicines_id)
        # tret.medicine.set(medic)
        # list=TreatMedicine.objects.filter(Treatment_id=tret.id)
        # return render(request,'prescb2.html',{'list':list})
        return redirect('docter:pre2',tret.id)
    else:
        docter=DoctorProfile.objects.get(user_id=request.user.id)
        context={'medicines':varient.objects.all(),'id':id ,'docter':docter}
        return render(request,'prescribe.html',context)
    
@login_required(login_url='home:signin')    
def pre2(request,id):
     list=TreatMedicine.objects.filter(Treatment_id=id)
     docter=DoctorProfile.objects.get(user_id=request.user.id)

     return render(request,'prescb2.html',{'list':list,'docter':docter})


@login_required(login_url='home:signin')    
def myPatient(request):
    docter=DoctorProfile.objects.get(user_id=request.user.id)
    Patients=Appointment.objects.filter(docter__user_id=request.user.id , status='finish')
    context={'Patients':Patients,'docter':docter}
    return render(request,'myPatient.html',context)


@login_required(login_url='home:signin')    
def doc_chat(request):
    Patient_list=Appointment.objects.filter(docter__user_id=request.user.id,status='finish')
    added_doctors=[]
    filtered_list = []
    for patient in Patient_list:
        doctor = patient.patient
        if doctor not in added_doctors:
            filtered_list.append(patient)
            added_doctors.append(doctor)

    print('haoll') 
    # return render(request,'pat_chat.html',{'pat':Patient_list})
    user=str(request.user.id)
    docter=DoctorProfile.objects.get(user_id=request.user.id)
    return render(request,'doc_chat.html',{'pat':filtered_list,'docter':docter})
    # return HttpResponseRedirect(reverse('home:room', args=[user]))
    # return redirect('room',user)

@login_required(login_url='home:signin')    
def msgg(request,id):
        Person=Appointment.objects.get(id=id)
        print(id)
        id=str(id)
        Patient_list=Appointment.objects.filter(docter__user_id=request.user.id,status='finish')
        added_doctors=[]
        filtered_list = []
        for patient in Patient_list:
            doctor = patient.patient
            if doctor not in added_doctors:
                filtered_list.append(patient)
                added_doctors.append(doctor)

        docter=DoctorProfile.objects.get(user_id=request.user.id)
        context={'pat':filtered_list,'id':id,'Person':Person,'username':request.user.username,'docter':docter}        
        return render(request,'msg2.html',context)

@login_required(login_url='home:signin')    
def decr(request,id):
    item=TreatMedicine.objects.get(id=id)
    if  item.quantity >1:
        item.quantity=item.quantity-1
        item.save()
    tem=item.Treatment_id    
    return redirect('docter:pre2',tem)

@login_required(login_url='home:signin')    
def incr(request,id):
    item=TreatMedicine.objects.get(id=id)
    item.quantity=item.quantity+1
    item.save()
    tem=item.Treatment_id    
    return redirect('docter:pre2',tem)
   
