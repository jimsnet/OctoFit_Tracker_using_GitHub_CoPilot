from rest_framework.routers import DefaultRouter
from .views import UserViewSet, TeamViewSet, ActivityViewSet, WorkoutViewSet, LeaderboardEntryViewSet
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserTests(APITestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.assertEqual(user.username, 'testuser')

class TeamTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teamuser', password='pass')
        self.team = Team.objects.create(name='Test Team')
        self.team.members.add(self.user)

    def test_team_creation(self):
        self.assertEqual(self.team.name, 'Test Team')
        self.assertIn(self.user, self.team.members.all())

class ActivityTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='activityuser', password='pass')
        self.activity = Activity.objects.create(user=self.user, activity_type='run', duration=30, calories_burned=200, date='2024-01-01')

    def test_activity_creation(self):
        self.assertEqual(self.activity.activity_type, 'run')
        self.assertEqual(self.activity.duration, 30)

class WorkoutTests(APITestCase):
    def test_workout_creation(self):
        workout = Workout.objects.create(name='Pushups', description='Do pushups', difficulty='Easy')
        self.assertEqual(workout.name, 'Pushups')

class LeaderboardEntryTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='leaderuser', password='pass')
        self.entry = LeaderboardEntry.objects.create(user=self.user, total_points=100)

    def test_leaderboard_entry(self):
        self.assertEqual(self.entry.total_points, 100)
