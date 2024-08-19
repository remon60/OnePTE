from django.contrib import admin
from .models import Question, Audio, Paragraph, Option, Submission
from .admin_mixins import RelatedFieldMixin

class BaseAdmin(RelatedFieldMixin, admin.ModelAdmin):
    def get_id(self, obj):
        return self.get_id_display(obj)
    
    def get_title(self, obj):
        return self.get_title_display(obj)
    
    def get_type(self, obj):
        return self.get_type_display(obj)
    
    def get_id_display(self, obj):
        return obj.id.id_field

    def get_title_display(self, obj):
        return obj.title.title_field
    
    def get_type_display(self, obj):
        return obj.type.type_field
    

@admin.register(Question)
class QuestionAdmin(BaseAdmin):
    list_display = ('id', 'get_title', 'get_type')
    search_fields = ('get_type',)

@admin.register(Audio)
class AudioAdmin(BaseAdmin):
    list_display = ('id', 'get_id', 'get_title', 'get_type', 'speaker', 'audio_file')
    search_fields = ('get_type',)

@admin.register(Paragraph)
class ParagraphAdmin(BaseAdmin):
    list_display = ('id', 'get_id', 'get_title', 'get_type', 'content')
    search_fields = ('get_type',)

@admin.register(Option)
class OptionAdmin(BaseAdmin):
    list_display = ('id', 'get_id', 'get_title', 'get_type', 'content', 'is_correct')
    search_fields = ('get_type',)

@admin.register(Submission)
class SubmissionAdmin(BaseAdmin):
    list_display = ('id', 'get_id', 'get_title', 'get_type', 'user_id', 'answer_text', 'ordered_paragraphs', 'selected_options', 'score')
    search_fields = ('get_type',)

