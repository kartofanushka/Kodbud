from django.db import models, migrations
from django.contrib import admin

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
        return f"Advertisement:(id={self.id}, title={self.title},  price={self.price})"
    #Advertisement: Advertisement(id=1, title=Заголовок №1, price=100.00)

    # template "Today 12:34:36"
    @admin.display(description=  'Creation date')
    def cteated_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time= self.created_at.time().strftime("%H:%M:%S")
            return "Today ", created_time

        # print ("self: ",self.created_at.date(),"now", timezone.now().date())
        return self.created_at.strftime("%d/%m/%Y, %H:%M:%S")
   
    @admin.display(description = 'Updated date')
    def updated_date(self):
        from django.utils import timezone, html
        if self.updated_at.date() == timezone.now().date():
            updated_time= self.updated_at.time().strftime("%H:%M:%S")
            return html.format_html(
                "<span style='color:grey'>Today {}</span>", updated_time
            )
        return self.updated_at.strftime("%d/%m/%Y, %H:%M:%S")
