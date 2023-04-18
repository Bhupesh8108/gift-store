from django.db import models
categories = [
    ('Birthday', 'hbd'),
    ('Anniversary','anv'),
    ('Valentine','vlt'),
    ('Flowers','flw'),
    ('Chocolate','clt'),
    ('Plants','pla'),
    ('Electronic','elt'),
    ('Jewels','jwl')   
]
class item(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to ='product/static/images')
    price = models.IntegerField()
    category = models.CharField(choices=categories,max_length=20)
    
    def __str__(self):
        return self.name

