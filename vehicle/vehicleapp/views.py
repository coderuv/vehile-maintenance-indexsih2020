from django.shortcuts import render
from .models import vehicles
from django.http.response import HttpResponse, JsonResponse

# Create your views here.
def home(req):
    q=req.GET.get('q','')    
    con=""
    if q =='' or q=='default':
        con=vehicles.objects.order_by('mileage')
    else:
        l="-"+q
        print(q)
        con= vehicles.objects.order_by(q)
    return render(req,'index.html',{'con':con})


def compare(req):
    q=req.GET.get('q','')    
    t=q.split('k')
 
    conn=[]
    comparestr="<h3><u>"
    o=0
    for i in t :
        o=o+1
        con=vehicles.objects.get(id=i)
        conn.append(con)
        if t.__len__()>o:
            comparestr=comparestr+con.vehicle_name+ " <b>VS</b> "
        else:
            comparestr=comparestr+con.vehicle_name

    comparestr=comparestr+"</u></h3>"

    return render(req,'compare.html',{'con':conn,'comparestr':comparestr})
        
        
        
        
def getmodal(req):
    id=req.GET.get('id','')
    con=vehicles.objects.get(id=id)
    vehicle_name=con.vehicle_name
    modaldescription= con.description
    mileage= str(con.mileage)
    price=str(con.price)
    oil_change=str(con.oil_change)
    airfilter_change=str(con.airfilter_change)
    spark_plug_change=str(con.spark_plug_change)
    tire_change= str(con.tire_change)
    battery_change =str(con.battery_change)
    hh='''
    <h5>Mileage    -    '''+mileage+''' kmpl</h5>
    <h5>Price    -    '''+price+''' &#8377;</h5>
    <h5>oil change    -     After'''+oil_change+''' kms</h5>
    <h5>Airfilter change    -     After'''+airfilter_change+''' kms</h5>
    <h5>spark plug change    -     After '''+spark_plug_change+''' kms</h5>
    <h5>tire change    -    After ''' +tire_change+'''kms</h5>
    <h5>battery_change    -     After'''+battery_change+''' yrs</h5>
        <h5>Rating    -     '''+str(con.rating)+'''</h5>

    '''
    return JsonResponse({'title':vehicle_name,'body':hh,'modaldescription':modaldescription})

    


