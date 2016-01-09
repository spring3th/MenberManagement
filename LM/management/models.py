from django.db import models
from django.contrib.auth.models import User


class Courses(models.Model):
    course_name = models.CharField(max_length=50,verbose_name=u"课程名")
    course_subject = models.TextField(verbose_name=u"课程纲要")
    teacher = models.TextField(verbose_name=u"老师")
    organize = models.CharField(max_length=50,verbose_name=u"培训机构")
    course_date = models.DateField(verbose_name=u"培训日期")
    course_address = models.CharField(max_length=50,verbose_name=u"授课场地")
    beizhu = models.TextField(verbose_name=u"备注")
    def __str__(self):
        return self.course_name
    class Meta:
        verbose_name = "课程"
        verbose_name_plural ="课程"


class Sign(models.Model):
    sign_mood = models.CharField(max_length=50,verbose_name=u"一句话")
    sign_date = models.DateField(verbose_name=u"签到时间")
    def __str__(self):
        return self.sign_mood
    class Meta:
        verbose_name = "签到"
        verbose_name_plural ="签到"


class Menbers(models.Model):
    user = models.OneToOneField(User)
	nickname = models.CharField(max_length = 16,verbose_name=u"昵称")
	permission = models.IntegerField()
    menber_name = models.CharField(max_length=30,verbose_name=u"姓名")
    menber_address = models.CharField(max_length=60,verbose_name=u"地址")
    menber_city = models.CharField(max_length=50,verbose_name=u"城市")
    menber_tel = models.CharField(max_length=50,verbose_name=u"电话")
    menber_store = models.CharField(max_length=50,verbose_name=u"店名")
    menber_brand = models.CharField(max_length=50,verbose_name=u"品牌")
    course = models.ManyToManyField(Courses)
    sign = models.ManyToManyField(Sign)
    menber_typ = models.CharField(max_length = 60,verbose_name="级别")

    def __str__(self):
        return u'%s %s' % (self.menber_name,self.menber_city)
    class Meta:
        verbose_name = "学员"
        verbose_name_plural ="学员"
