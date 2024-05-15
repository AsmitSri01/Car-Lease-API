from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Car,Lease
from django.http import JsonResponse
# Create your views here.
#test
@csrf_exempt
def lease_car(request):
    if request.method == 'POST':
        data = request.POST
        driver_id=data.get('driverId')
        car_id=data.get('carId')
        try:
            car=Car.objects.get(id=car_id,status='available')
            car.status='leased'
            car.save()
            Lease.objects.create(driver_id=driver_id,car=car)
            return JsonResponse({'message':'Car Leased Succesfully','data':{'driverId':driver_id,'carId':car_id}},status=201)
        except Car.DoesNotExist:
            return JsonResponse({'message':'Car not available for lease'},status=404)
        

@csrf_exempt
def drop_car(request):
    if request.method == 'POST':
        data=request.POST
        driver_id=data.get('driverId')
        car_id=data.get('carId')
        try:
            lease=Lease.objects.get(driver_id=driver_id,car_id=car_id)
            lease.car.status='available'
            lease.car.save()
            lease.delete()
            return JsonResponse({'message':'Car Droppped Succesfully','data':{'carId':car_id,'status':'available'}})
        except Lease.DoesNotExist:
            return JsonResponse({'message':'Car not found or leased by driver'},status=404)
        
def filter_cars():
    cars=Car.objects.all().values()
    return JsonResponse({'message':'Cars retrieved successfully','data':list(cars)})



            
            
