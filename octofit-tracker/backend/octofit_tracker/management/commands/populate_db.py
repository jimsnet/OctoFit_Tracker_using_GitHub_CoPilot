from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from djongo import models
from pymongo import MongoClient

# Sample data for superheroes, teams, activities, leaderboard, and workouts
data = {
    "users": [
        {"name": "Superman", "email": "superman@dc.com", "team": "DC"},
        {"name": "Batman", "email": "batman@dc.com", "team": "DC"},
        {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "DC"},
        {"name": "Iron Man", "email": "ironman@marvel.com", "team": "Marvel"},
        {"name": "Captain America", "email": "cap@marvel.com", "team": "Marvel"},
        {"name": "Black Widow", "email": "widow@marvel.com", "team": "Marvel"},
    ],
    "teams": [
        {"name": "Marvel", "description": "Marvel Superheroes"},
        {"name": "DC", "description": "DC Superheroes"},
    ],
    "activities": [
        {"user": "superman@dc.com", "activity": "Flying", "duration": 60},
        {"user": "ironman@marvel.com", "activity": "Suit Training", "duration": 45},
        {"user": "batman@dc.com", "activity": "Martial Arts", "duration": 30},
    ],
    "leaderboard": [
        {"user": "superman@dc.com", "score": 1000},
        {"user": "ironman@marvel.com", "score": 950},
        {"user": "batman@dc.com", "score": 900},
    ],
    "workouts": [
        {"name": "Strength Training", "description": "General superhero strength workout"},
        {"name": "Agility Drills", "description": "Improve agility and reflexes"},
    ]
}

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']

        # Drop collections if they exist
        for collection in ["users", "teams", "activities", "leaderboard", "workouts"]:
            db[collection].delete_many({})

        # Insert test data
        db.users.insert_many(data["users"])
        db.teams.insert_many(data["teams"])
        db.activities.insert_many(data["activities"])
        db.leaderboard.insert_many(data["leaderboard"])
        db.workouts.insert_many(data["workouts"])

        # Ensure unique index on email for users
        db.users.create_index("email", unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
