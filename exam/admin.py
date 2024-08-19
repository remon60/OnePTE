from django.contrib import admin
from .models import *  


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type') 
    search_fields = ('type',)


@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_id', 'question_title', 'question_type', 'speaker', 'audio_file') 
    search_fields = ('get_type',)

    def question_id(self, obj):
        return obj.question.id
    def question_title(self, obj):
        return obj.question.title
    def question_type(self, obj):
        return obj.question.type


@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_id', 'get_title', 'get_type', 'content') 
    search_fields = ('get_type',)

    def get_id(self, obj):
        return obj.question.id
    def get_title(self, obj):
        return obj.question.title
    def get_type(self, obj):
        return obj.question.type


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_id', 'get_title', 'get_type', 'content', 'is_correct', 'correct_order') 
    search_fields = ('get_type',)

    def get_id(self, obj):
        return obj.question.id
    def get_title(self, obj):
        return obj.question.title
    def get_type(self, obj):
        return obj.question.type
    

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_id', 'get_title', 'get_type', 'user_id', 'answer_text', 'ordered_paragraphs', 'selected_options', 'score') 
    search_fields = ('get_type',)

    def get_id(self, obj):
        return obj.question.id
    def get_title(self, obj):
        return obj.question.title
    def get_type(self, obj):
        return obj.question.type
    










