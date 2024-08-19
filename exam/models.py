from django.db import models

class Question(models.Model):
    QUESTION_TYPES = [
        ('SST', 'Summarize Spoken Text'),
        ('RO', 'Re-Order Paragraph'),
        ('RMMCQ', 'Reading Multiple Choice (Multiple)'),
    ]

    type = models.CharField(max_length=5, choices=QUESTION_TYPES)
    title = models.CharField(max_length=255)

class Audio(models.Model):
    question = models.ForeignKey(Question, related_name='audios', on_delete=models.CASCADE, unique=True)
    speaker = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audios/')

class Paragraph(models.Model):
    question = models.ForeignKey(Question, related_name='paragraphs', on_delete=models.CASCADE)
    content = models.TextField()

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    correct_order=models.IntegerField(default=0)

class Submission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    answer_text = models.TextField(null=True, blank=True)
    ordered_paragraphs = models.TextField(null=True, blank=True)
    selected_options = models.TextField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)





    