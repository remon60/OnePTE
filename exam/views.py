from rest_framework import generics
from .models import Question, Submission
from .serializers import QuestionSerializer, SubmissionSerializer
import random


class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        question_type = self.request.query_params.get('type')
        if question_type:
            return Question.objects.filter(type=question_type)
        return Question.objects.all()


class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SubmissionCreateView(generics.CreateAPIView):
    serializer_class = SubmissionSerializer

    def perform_create(self, serializer):
        submission = serializer.save()
        
        if submission.question.type == 'SST':
            scores = {
                "Content": random.randint(0, 2),
                "Form": random.randint(0, 2),
                "Grammar": random.randint(0, 2),
                "Vocabulary": random.randint(0, 2),
                "Spelling": random.randint(0, 2),
            }
            submission.score = sum(scores.values())
        elif submission.question.type == 'RO':
            correct_order = ['1', '2', '3', '4']
            user_order = submission.ordered_paragraphs.split(',')

            correct_pairs = [(correct_order[i], correct_order[i + 1]) for i in range(len(correct_order) - 1)]
            user_pairs = [(user_order[i], user_order[i + 1]) for i in range(len(user_order) - 1)]
            
            scores = {
                "CorrectPairs": sum([1 for pair in user_pairs if pair in correct_pairs])
            }
            submission.score = scores["CorrectPairs"]
        elif submission.question.type == 'RMMCQ':
            correct_options = ['A', 'C'] 
            user_options = submission.selected_options.split(',')

            scores = 0
            for option in user_options:
                if option in correct_options:
                    scores += 1
                else:
                    scores -= 1
            
            submission.score = max(0, scores)

        submission.save()



class PracticeHistoryView(generics.ListAPIView):
    serializer_class = SubmissionSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        question_type = self.request.query_params.get('type')
        queryset = Submission.objects.filter(user_id=user_id)
        if question_type:
            queryset = queryset.filter(question__type=question_type)
        return queryset
















