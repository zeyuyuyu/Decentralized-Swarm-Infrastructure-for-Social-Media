import hashlib
import time
from typing import Dict

class ReputationManager:
    def __init__(self):
        self.reputation_scores: Dict[str, float] = {}
        self.reputation_history: Dict[str, list] = {}

    def update_reputation(self, user_id: str, score_change: float):
        if user_id not in self.reputation_scores:
            self.reputation_scores[user_id] = 0.0
        self.reputation_scores[user_id] += score_change
        self.reputation_history.setdefault(user_id, []).append((time.time(), score_change))

    def get_reputation_score(self, user_id: str) -> float:
        return self.reputation_scores.get(user_id, 0.0)

    def get_reputation_history(self, user_id: str) -> list:
        return self.reputation_history.get(user_id, [])

class Post:
    def __init__(self, content: str, author_id: str):
        self.content = content
        self.author_id = author_id
        self.timestamp = time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self) -> str:
        return hashlib.sha256((self.content + str(self.timestamp) + self.author_id).encode()).hexdigest()

class SocialMediaApp:
    def __init__(self):
        self.reputation_manager = ReputationManager()
        self.posts: list[Post] = []

    def create_post(self, content: str, author_id: str):
        post = Post(content, author_id)
        self.posts.append(post)
        self.reputation_manager.update_reputation(author_id, 1.0)
        return post

    def get_posts(self) -> list[Post]:
        return self.posts

    def get_user_reputation(self, user_id: str) -> float:
        return self.reputation_manager.get_reputation_score(user_id)

    def get_user_reputation_history(self, user_id: str) -> list:
        return self.reputation_manager.get_reputation_history(user_id)
