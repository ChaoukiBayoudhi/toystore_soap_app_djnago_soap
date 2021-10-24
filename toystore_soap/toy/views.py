from django.shortcuts import render
from spyne.decorator import rpc
from spyne.model.binary import File,ByteArray
from spyne.model.complex import ComplexModel
from spyne.service import ServiceBase
from spyne.model.primitive import Integer,String,UnsignedInteger,Decimal,Image,Date
from spyne import Array

from toy.models import Toy


class Toys(ComplexModel):
    id=Integer('id')
    name=String('name')
    price=Decimal
    quantity=UnsignedInteger
    photo=File #or ByteArray
    bought_date=Date
    description=String('description')
class AddEditToy(ComplexModel):
    id=Integer('id')
    name=String('name')
    price=Decimal
    quantity=UnsignedInteger
    photo=File #or ByteArray
    bought_date=Date
    description=String('description')

class SoapService(ServiceBase) :
    @rpc(_returns=Array(Toys))
    def ListToy(ctx):
        return Toy.objects.values('id','name','price','description') 
           
    @rpc(AddEditToy,_returns=Toys)
    def AddToy(ctx,toy):
        data=Toy.as_dict(); #convert to toys dictionary
        data_toy=keys_add_none(data,'id',)