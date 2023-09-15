from typing import List

from helper_functions import get_set_summary, get_set_full_data, get_all_sets
from objects.Piece import Piece


class BuildSet:
    def __init__(self, name):
        self.name = name
        self.id = get_set_summary(self.name)["id"]
        self.load_collection()

    def load_collection(self):
        collection = self.get_set_collection_by_id()
        self.collection = {}
        for piece in collection:
            self.collection[
                Piece(id=piece["part"]["designID"], color=str(piece["part"]["material"]))
            ] = piece["quantity"]

    def get_set_collection_by_id(self):
        set_data = get_set_full_data(self.id)
        set_collection: List = set_data["pieces"]
        return set_collection


    @staticmethod
    def get_all_buildSets():
        return [BuildSet(build_set["name"]) for build_set in get_all_sets()["Sets"]]