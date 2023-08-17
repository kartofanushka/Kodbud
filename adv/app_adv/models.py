from django.db import models, migrations
from django.contrib import admin
from django.contrib.auth import get_user_model

User=get_user_model() # auth_user table

# Create your models here.
class Advertisement(models.Model):
    title=models.CharField("header", max_length=128)
    description=models.TextField("description")
    price=models.DecimalField("price", max_digits=12, decimal_places=2)
    auction=models.BooleanField("auction")
    created_at=models.DateTimeField(auto_now_add=True) # auto_now_add- time of creation
    updated_at=models.DateTimeField(auto_now=True) # auto_now - time of updates
    user=models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name="User")
    image= models.ImageField(verbose_name="Image", upload_to="adv/")
    
    class Meta:
        db_table="advertisements"
    
    def __str__(self):
        return f"(id={self.id}, title={self.title},  price={self.price},created_at={self.created_at}, updated_at={self.updated_at},user={self.user},image={self.image},)"
    #Advertisement: (id=1, title=Заголовок №1, price=100.00)

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
    @admin.display(description = 'Teaser')
    def teaser(self):
        teaser=self.description
        if len(teaser)>300:
            teaser=teaser[0:200] + " ..."
        return teaser
    @admin.display(description = 'Image')
    def image_d(self):
        from django.utils import html
       
        image=self.image
        if image=="1":
            image="/static/img/noimage.png"
        else:
            image="/media/"+str(image)
        return html.format_html(
                "<a href='{}'><img src='{}' width=150></a>", image,image
            )

    
    # {{MEDIA_URL/noimage.png}}