from django.db import models

class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    head1=models.CharField(max_length=200,default="")
    content_head1=models.CharField(max_length=5000,default="")
    head2=models.CharField(max_length=200,default="")
    content_head2=models.CharField(max_length=5000,default="")
    head3=models.CharField(max_length=200,default="")
    content_head3=models.CharField(max_length=5000,default="")
    head4=models.CharField(max_length=200,default="")
    content_head4=models.CharField(max_length=5000,default="")
    author_name=models.CharField(max_length=80,default="")
    publishing_date = models.DateField()
    thumbnail = models.ImageField(default="")

    def __str__(self):
        return self.post_title

class Contact_us(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,default="")
    email = models.CharField(max_length=80,default="")
    phone =models.CharField(max_length=13,default="")
    description =models.CharField(max_length=500,default="")

    def __str__(self):
        return self.name