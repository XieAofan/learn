from django.db import models
class Question(models.Model):
    q_id = models.AutoField(primary_key=True)
    img = models.CharField(max_length=20,default='')
    single = 's'
    indefinite = 'i'
    mass_media = 'm'
    q_type_c = [
        (single, "单选"),
        (indefinite, "不定项"),
        (mass_media, "多媒体"),
    ]
    q_type  = models.CharField(
        max_length=10,
        choices=q_type_c,
        default=indefinite,
    )
    ac_data = models.JSONField(null=True)
    choice = models.JSONField(null=True)

class Question_Group(models.Model):
    source = models.CharField(max_length=40,default='')
    img = models.CharField(max_length=20,default='')
    question_ids = models.JSONField(null=True)
    ac_data = models.JSONField(null=True)
    qg_id = models.AutoField(primary_key=True)
    single = 's'
    indefinite = 'i'
    mass_media = 'm'
    q_type_c = [
        (single, "单选"),
        (indefinite, "不定项"),
        (mass_media, "多媒体"),
    ]
    q_type  = models.CharField(
        max_length=10,
        choices=q_type_c,
        default=indefinite,
    )
    geo = 'g'
    eso = 'e'
    Subject_c = [
        (geo, "地理"),
        (eso, "地球科学"),
    ]
    subject = models.CharField(
        max_length=10,
        choices=Subject_c,
        default=eso,
    )
# Create your models here.
