from django.urls import path, re_path
from .views import QuizList, QuizDetailsView, MyQuizListView, SaveUsersAnswer, SubmitQuizView

urlpatterns = [
    path('my-quizzes/', MyQuizListView.as_view()),
    path('quizzes/', QuizList.as_view()),
    path('save-answer/', SaveUsersAnswer.as_view()),
    re_path(r'quizzes/(?P<slug>[\w\-]+)/$', QuizDetailsView.as_view()),
    re_path(r'quizzes/(?P<slug>[\w\-]+)/submit/$', SubmitQuizView.as_view()),
]