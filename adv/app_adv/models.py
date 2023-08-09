from django.db import models, migrations


# Create your models here.
class Advertisement(models.Model):
    title=models.CharField("header", max_length=128)
    description=models.TextField("description")
    price=models.DecimalField("price", max_digits=12, decimal_places=2)
    auction=models.BooleanField("auction")
    created_at=models.DateTimeField(auto_now_add=True) # auto_now_add- time of creation
    updated_at=models.DateTimeField(auto_now=True) # auto_now - time of updates
    
    class Meta:
        db_table="advertisements"
    
    def __str__(self):
        return f"id={self.id}, title={self.title},  price={self.price}"
    #Advertisement: Advertisement(id=1, title=Заголовок №1, price=100.00)

