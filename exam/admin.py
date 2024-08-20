from django.contrib import admin
from .models import Question, Audio, Paragraph, Option, Submission


class QuestionRelatedMixin:
    def question_id(self, obj):
        return obj.question.id
    
    def question_title(self, obj):
        return obj.question.title
    
    def question_type(self, obj):
        return obj.question.type



@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'type')
    search_fields = ('type',)



@admin.register(Audio)
class AudioAdmin(QuestionRelatedMixin, admin.ModelAdmin):
    list_display = ('id', 'question_id', 'question_title', 'question_type', 'speaker', 'audio_file')
    search_fields = ('question_type',)



@admin.register(Paragraph)
class ParagraphAdmin(QuestionRelatedMixin, admin.ModelAdmin):
    list_display = ('id', 'question_id', 'question_title', 'question_type', 'content')
    search_fields = ('question_type',)



@admin.register(Option)
class OptionAdmin(QuestionRelatedMixin, admin.ModelAdmin):
    list_display = ('id', 'question_id', 'question_title', 'question_type', 'content', 'is_correct', 'correct_order')
    search_fields = ('question_type',)



@admin.register(Submission)
class SubmissionAdmin(QuestionRelatedMixin, admin.ModelAdmin):
    list_display = ('id', 'question_id', 'question_title', 'question_type', 'user_id', 'answer_text', 'ordered_paragraphs', 'selected_options', 'score')
    search_fields = ('question_type',)
