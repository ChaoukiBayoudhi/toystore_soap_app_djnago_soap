from django.db import models
from django.utils import timezone


from toystore_soap.settings import TIME_ZONE

dir_storage="Storages/commun/toys"
# Create your models here.

class Provider(models.Model):
    name=models.CharField(max_length=50)
    tel=models.CharField("Telephone Number",max_length=13)
    email=models.EmailField(unique=True)
    site=models.URLField("Provider Web Site")
    class Meta:
        ordering=['name','email']

    def __str__(self):
        return "%s : the provider"%self.name

    

class Toy(models.Model):
    """blank=False like required
    and null = True like NULL on database
    """
    name=models.CharField(max_length=200,unique=True,blank=False,null=False);
    price=models.DecimalField(max_digits=6, decimal_places=2, blank=False,null=True)
    quantity=models.PositiveIntegerField(null=True)
    photo=models.ImageField(upload_to=dir_storage,blank=True,null=True)
    bought_date=models.DateField(blank=True,null=True,default=timezone.now)
    description=models.TextField(max_length=250,blank=True,null=True)












    #1-* relationship between Toy and Provider
    Provider=models.ForeignKey(Provider,on_delete=models.CASCADE)







    class Meta:
        db_table = 'Toy'
        managed = True
        verbose_name = 'Toy'
        verbose_name_plural = 'Toys'
        ordering=['name']
    def __str__(self):
        return "(%s, %s) : The toy"%(self.name,self.price)

    
class Place(models.Model):
    house_number=models.IntegerField(null=False)
    street=models.TextField(null=False)
    province=models.CharField(max_length=30,null=False)
    city=models.CharField(max_length=30,null=False)
    postal_code=models.IntegerField()

    class Meta:
        db_table = 'Address'
        managed = True
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self):
        return "(%s, %s, %s) : the place"%(self.house_number,self.street,self.city)



class Customer(models.Model):
    name = models.CharField(max_length=30,null=False)
    tel = models.IntegerField(null=False)
    email=models.EmailField("Customer Email", null=False)
    #1-1 relationship between customer and Place
    address=models.OneToOneField(Place,on_delete=models.CASCADE)
    # verbose_name  is the name that will be displayed on admin page
    #*-* relationship between Customer and Toy
    toys=models.ManyToManyField(Toy, verbose_name="Provided toys")
    class Meta:
        ordering=['name','tel']
        db_table = 'customer_tab'
        managed = True
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return "%s : the customer"%self.name

    

