from typing import List

from helper_functions import get_user_summary, get_user_full_data
from objects.Piece import Piece


class User:
    def __init__(self, username):
        self.username = username
        self.id = get_user_summary(self.username)["id"]
        self.load_collection()

    def load_collection(self):
        collection = self.get_user_collection_by_id()
        self.collection = {}
        for piece in collection:
            for variant in piece["variants"]:
                self.collection[Piece(id=piece["pieceId"], color=variant["color"])] = variant["count"]

    def get_user_collection_by_id(self):
        user_data = get_user_full_data(self.id)
        user_collection: List = user_data["collection"]
        return user_collection
