from django.core.management.base import BaseCommand
from pymongo import MongoClient
from bson import ObjectId
from datetime import timedelta

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activities, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient('localhost', 27017)
        db = client['octofit_db']

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Insert users
        users = [
            {"_id": ObjectId(), "username": "student1", "email": "student1@example.com", "password": "password1"},
            {"_id": ObjectId(), "username": "student2", "email": "student2@example.com", "password": "password2"},
            {"_id": ObjectId(), "username": "student3", "email": "student3@example.com", "password": "password3"},
        ]
        db.users.insert_many(users)

        # Insert teams
        teams = [
            {"_id": ObjectId(), "name": "Team Alpha", "members": [users[0]["_id"], users[1]["_id"]]},
            {"_id": ObjectId(), "name": "Team Beta", "members": [users[2]["_id"]]},
        ]
        db.teams.insert_many(teams)

        # Insert activities
        activities = [
            {"_id": ObjectId(), "user": users[0]["_id"], "activity_type": "Running", "duration": 30},
            {"_id": ObjectId(), "user": users[1]["_id"], "activity_type": "Cycling", "duration": 45},
            {"_id": ObjectId(), "user": users[2]["_id"], "activity_type": "Swimming", "duration": 60},
        ]
        db.activity.insert_many(activities)

        # Insert leaderboard entries
        leaderboard_entries = [
            {"_id": ObjectId(), "user": users[0]["_id"], "score": 100},
            {"_id": ObjectId(), "user": users[1]["_id"], "score": 90},
            {"_id": ObjectId(), "user": users[2]["_id"], "score": 80},
        ]
        db.leaderboard.insert_many(leaderboard_entries)

        # Insert workouts
        workouts = [
            {"_id": ObjectId(), "name": "Morning Run", "description": "A 5km run to start the day"},
            {"_id": ObjectId(), "name": "Cycling Session", "description": "A 20km cycling session"},
            {"_id": ObjectId(), "name": "Swimming Laps", "description": "30 minutes of swimming laps"},
        ]
        db.workouts.insert_many(workouts)

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data using pymongo.'))
