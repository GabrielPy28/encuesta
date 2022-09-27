from rest_framework import serializers
from quiz.models import Quiz, QuizTaker, Questions, Answer, UsersAnswer

class QuizListSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    class Meta:
        model = Quiz
        fields = ['id', 'nombre', 'description', 'slug', 'questions_count']
        read_only_fields = ['questions_count']
    
    def get_questions_count(self, obj):
        return obj.questions_set.all().count()

class UsersAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsersAnswer
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'label']

class QuestionsSerializer(serializers.ModelSerializer):
    answer_set = AnswerSerializer(many=True)

    class Meta:
        model = Questions
        fields = '__all__'

class MyQuizListSerializer(serializers.ModelSerializer):
    questions_count = serializers.SerializerMethodField()
    completed = serializers.SerializerMethodField()
    progress = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()

    class Meta:
        model = Quiz
        fields = ['id', 'name', 'description', 'slug', 'questions_count', 'completed', 'progress', 'score']
        read_only_fields = ['questions_count', 'completed', 'progress']
    
    def get_completed(self, obj):
        try:
            quiztaker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
            return quiztaker.completed
        except QuizTaker.DoesNotExist:
            return None
    
    def get_progress(self, obj):
        try:
            quiztaker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
            if quiztaker.completed == False:
                questions_answered = UsersAnswer.objects.filter(quiz_taker=quiztaker, answer__isnull=False).count()
                total_questions =  obj.question_set.all().count()
                return int(questions_answered / total_questions)
            return None
        except QuizTaker.DoesNotExist:
            return None

    def get_questions_count(self, obj):
        return obj.questions_set.all().count()

    def get_score(self, obj):
        try:
            quiztaker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
            if quiztaker.completed == True:
                return quiztaker.score
            return None
        except QuizTaker.DoesNotExist:
            return None

class QuizTakerSerializer(serializers.ModelSerializer):
    usersanswer_set = UsersAnswerSerializer(many=True)

    class Meta:
        model = QuizTaker
        fields = '__all__'

class QuizDetailSerializer(serializers.ModelSerializer):
    quiztakers_set = serializers.SerializerMethodField()
    questions_set = QuestionsSerializer(many=True)

    class Meta:
        model = Quiz
        fields = '__all__'

    def get_quiztakers_set(self, obj):
        try:
            quiz_taker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
            serializer = QuizTakerSerializer(quiz_taker)
            return serializer.data
        except QuizTaker.DoesNotExist:
            return None

class QuizResultSerializer(serializers.ModelSerializer):
    quiztaker_set = serializers.SerializerMethodField()
    questions_set = QuestionsSerializer(many=True)

    class Meta:
        model = Quiz
        fields = '__all__'

    def get_quiztaker_set(self, obj):
        try:
            quiztaker = QuizTaker.objects.get(user=self.context['request'].user, quiz=obj)
            serializer = QuizTakerSerializer(quiztaker)
            return serializer.data
        except QuizTaker.DoesNotExist:
            return None