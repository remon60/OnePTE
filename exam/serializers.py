from rest_framework import serializers
from .models import Question, Audio, Paragraph, Option, Submission


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ['id', 'speaker', 'audio_file']


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'content']


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'content']




class QuestionSerializer(serializers.ModelSerializer):
    audios = AudioSerializer(many=True, read_only=True)
    paragraphs = ParagraphSerializer(many=True, read_only=True)
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'type', 'title', 'audios', 'paragraphs', 'options']



class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'question', 'user_id', 'answer_text', 'ordered_paragraphs', 'selected_options', 'score']






