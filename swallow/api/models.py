from django.db import models

class Form(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="昵称", max_length=255, default="")
    phone = models.CharField(verbose_name="手机号", max_length=255, default="")
    email = models.CharField(verbose_name="邮箱", max_length=255, default="")
    company = models.CharField(verbose_name="公司名", max_length=255, default="")
    need = models.TextField(verbose_name="业务需求", max_length=1000, default="")

    class Meta:
        db_table = "form"

    def _str_(self):
        return self.form
