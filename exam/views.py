from rest_framework import generics
from .models import Question, Submission
from .serializers import QuestionSerializer, SubmissionSerializer
import random


class QuestionListView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        question_type = self.request.query_params.get('type')
        if question_type:
            return self.queryset.filter(type=question_type)
        return self.queryset


class QuestionDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SubmissionCreateView(generics.CreateAPIView):
    serializer_class = SubmissionSerializer

    def perform_create(self, serializer):
        submission = serializer.save()
        
        if submission.question.type == 'SST':
            submission.score = {
                "Content": random.randint(0, 2),
                "Form": random.randint(0, 2),
                "Grammar": random.randint(0, 2),
                "Vocabulary": random.randint(0, 2),
                "Spelling": random.randint(0, 2),
            }
            # Calculate total score
            submission.total_score = sum(submission.score.values())
        elif submission.question.type == 'RO':
            correct_order = ['1', '2', '3', '4']  # Replace with the actual correct order
            user_order = submission.ordered_paragraphs.split(',')

            correct_pairs = [(correct_order[i], correct_order[i + 1]) for i in range(len(correct_order) - 1)]
            user_pairs = [(user_order[i], user_order[i + 1]) for i in range(len(user_order) - 1)]
            
            submission.score = {
                "CorrectPairs": sum([1 for pair in user_pairs if pair in correct_pairs])
            }

            # The total score is the number of correctly ordered pairs
            submission.total_score = submission.score["CorrectPairs"]
        elif submission.question.type == 'RMMCQ':
            correct_options = ['A', 'C']  # Replace with the actual correct options
            user_options = submission.selected_options.split(',')

            score = 0
            for option in user_options:
                if option in correct_options:
                    score += 1
                else:
                    score -= 1
            
            # Ensure the minimum score is 0
            submission.total_score = max(0, score)
            submission.score = {"ChoiceScore": submission.total_score}

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















