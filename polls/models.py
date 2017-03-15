from django.db import models


class Question(models.Model):
    q_id = models.IntegerField(primary_key=True)
    standard = models.TextField(blank=True, null=True)
    all_id = models.IntegerField(blank=True, null=True)
    q_text = models.TextField(blank=True, null=True)
    option1 = models.TextField(blank=True, null=True)
    option2 = models.TextField(blank=True, null=True)
    option3 = models.TextField(blank=True, null=True)
    option4 = models.TextField(blank=True, null=True)
    ans = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'polls'
        db_table = 'Question'
    def __unicode__(self):
        return self.q_text

class Phpquestion(models.Model):
    q_id = models.IntegerField(primary_key=True)
    all_id = models.IntegerField(blank=True, null=True)
    q_text = models.TextField(blank=True, null=True)
    option1 = models.TextField(blank=True, null=True)
    option2 = models.TextField(blank=True, null=True)
    option3 = models.TextField(blank=True, null=True)
    option4 = models.TextField(blank=True, null=True)
    ans = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'polls'
        db_table = 'phpQuestion'
    def __unicode__(self):
        return self.q_text

class Pythonquestion(models.Model):
    q_id = models.IntegerField(primary_key=True)
    all_id = models.IntegerField(blank=True, null=True)
    q_text = models.TextField(blank=True, null=True)
    option1 = models.TextField(blank=True, null=True)
    option2 = models.TextField(blank=True, null=True)
    option3 = models.TextField(blank=True, null=True)
    option4 = models.TextField(blank=True, null=True)
    ans = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'polls'
        db_table = 'Pythonquestion'
    def __unicode__(self):
        return self.q_text

class Userprof(models.Model):
    username = models.TextField(blank=True, null=True)
    subject = models.TextField(blank=True, null=True)
    
    score = models.IntegerField(blank=True, null=True)
    
    class Meta:
        app_label = 'polls'
        db_table = 'Userprof'
    def __unicode__(self):
        return self.username

class ContactDetails(models.Model):
    username = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'polls'
        db_table = 'ContactDetails'
    def __unicode__(self):
        return self.username

class UserQuestions(models.Model):
    username = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    question = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'polls'
        db_table = 'UserQuestions'
    def __unicode__(self):
        return self.username

class Vocabulary(models.Model):
    q_id = models.IntegerField(primary_key=True)
    all_id = models.IntegerField(blank=True, null=True)
    std=models.IntegerField(blank=True, null=True)
    q_text = models.TextField(blank=True, null=True)
    option1 = models.TextField(blank=True, null=True)
    option2 = models.TextField(blank=True, null=True)
    option3 = models.TextField(blank=True, null=True)
    option4 = models.TextField(blank=True, null=True)
    ans = models.TextField(blank=True, null=True)

class comprehension(models.Model):
    q_id = models.IntegerField(primary_key=True)
    all_id = models.IntegerField(blank=True, null=True)
    std=models.IntegerField(blank=True, null=True)
    q_text = models.TextField(blank=True, null=True)
    option1 = models.TextField(blank=True, null=True)
    option2 = models.TextField(blank=True, null=True)
    option3 = models.TextField(blank=True, null=True)
    option4 = models.TextField(blank=True, null=True)
    ans = models.TextField(blank=True, null=True)

class maths(models.Model):
    q_id = models.IntegerField(primary_key=True)
    all_id = models.IntegerField(blank=True, null=True)
    std=models.IntegerField(blank=True, null=True)
    q_text = models.TextField(blank=True, null=True)
    option1 = models.TextField(blank=True, null=True)
    option2 = models.TextField(blank=True, null=True)
    option3 = models.TextField(blank=True, null=True)
    option4 = models.TextField(blank=True, null=True)
    ans = models.TextField(blank=True, null=True)


class Composition(models.Model):
    q_id = models.IntegerField(primary_key=True)
    all_id = models.IntegerField(blank=True, null=True)
    std=models.IntegerField(blank=True, null=True)
    q_text = models.TextField(blank=True, null=True)

class upload(models.Model):
    q_id = models.IntegerField(primary_key=True)
    all_id = models.IntegerField(blank=True, null=True)
    std=models.IntegerField(blank=True, null=True)
    pic = models.FileField()


class Document(models.Model):
     docfile = models.ImageField(upload_to='Documents/%Y/%m/%d')

class Dictation(models.Model):
    word=models.TextField(blank=True,null=True)
     

class studentprof(models.Model):
    username = models.TextField(blank=True, null=True)
    std=models.IntegerField(blank=True,null=True)
    vocabulary=models.IntegerField(blank=True,null=True)
    comprescore=  models.IntegerField(blank=True, null=True)
    wordreadingscore=models.IntegerField(blank=True, null=True)
    Spelling=models.IntegerField(blank=True, null=True)
    creative = models.IntegerField(blank=True, null=True)
    punctuation = models.IntegerField(blank=True, null=True)
    composition = models.IntegerField(blank=True, null=True)
    handwriting=models.FileField(blank=True, null=True)
    handwritingscore=models.IntegerField(blank=True, null=True)
    dr = models.IntegerField(blank=True, null=True)
    ds = models.IntegerField(blank=True, null=True)
    dh = models.IntegerField(blank=True, null=True)
    dwe = models.IntegerField(blank=True, null=True)
    dba = models.IntegerField(blank=True, null=True)
    dha = models.IntegerField(blank=True, null=True)
    da = models.IntegerField(blank=True, null=True)
    ed = models.IntegerField(blank=True, null=True)
    dm = models.IntegerField(blank=True, null=True)
    lm = models.IntegerField(blank=True, null=True)
    dss = models.IntegerField(blank=True, null=True)
    dns = models.IntegerField(blank=True, null=True)
    dll = models.IntegerField(blank=True, null=True)
    dls = models.IntegerField(blank=True, null=True)
    stl = models.IntegerField(blank=True, null=True)
    rg = models.IntegerField(blank=True, null=True)
    status=models.TextField(blank=True,null=True)

class Resources(models.Model):
    area=models.TextField(blank=True,null=True)
    subject_grade=models.IntegerField(blank=True,null=True)
    res_url=models.TextField(blank=True,null=True)






