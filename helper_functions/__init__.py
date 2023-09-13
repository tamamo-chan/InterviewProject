from typing import List, Optional

import helper_functions
from helper_functions.api_data_retrieval import get_user_summary, get_user_full_data, get_all_sets, get_set_summary, \
    get_set_full_data, get_all_users


def get_user_collection_by_username(username):
    user_summary = get_user_summary(username)
    return get_user_collection_by_id(user_summary["id"])


def get_user_collection_by_id(user_id):
    user_data = get_user_full_data(user_id)
    user_collection: List = user_data["collection"]
    return user_collection


def get_buildable_sets(username):
    if username not in [user["username"] for user in get_all_users()["Users"]]:
        return []
    user_collection = get_user_collection_by_username(username)
    sets = get_all_sets()
    build_able_sets = []
    for specific_set in sets["Sets"]:
        set_name = specific_set["name"]
        set_summary = get_set_summary(set_name)
        set_full_data = get_set_full_data(set_summary["id"])

        user_has_all_pieces = True

        for piece in set_full_data["pieces"]:
            user_has_piece = check_if_piece_quantity_in_user_collection(piece, user_collection)
            if not user_has_piece:
                user_has_all_pieces = False
                break

        if user_has_all_pieces:
            build_able_sets.append(set_name)
    return build_able_sets


def check_if_piece_quantity_in_user_collection(piece, user_collection):
    designID = piece["part"]["designID"]
    color_code = str(piece["part"]["material"])
    quantity = piece["quantity"]
    variant = extract_variant_from_user_collection(user_collection, designID, color_code)
    if variant:
        if variant["count"] >= quantity:
            return True
    return False


def calculate_missing_pieces(user_collection, designID, color_code, quantity) -> int:
    variant = extract_variant_from_user_collection(user_collection, designID, color_code)
    if variant:
        return quantity - variant["count"]
    return quantity


def extract_variant_from_user_collection(user_collection, designID, color_code) -> Optional[dict]:
    user_piece = next((piece_type for piece_type in user_collection if piece_type["pieceId"] == designID), None)
    if user_piece:
        return next((variant for variant in user_piece["variants"] if variant["color"] == color_code), None)
    return None


def compile_missing_pieces_list(set_name, user_collection):
    set_summary = get_set_summary(set_name)
    set_full_data = get_set_full_data(set_summary["id"])
    missing_pieces = {}
    for piece in set_full_data["pieces"]:
        designID = piece["part"]["designID"]
        color_code = str(piece["part"]["material"])
        quantity = piece["quantity"]
        user_has_piece = check_if_piece_quantity_in_user_collection(piece, user_collection)
        if not user_has_piece:
            amount = calculate_missing_pieces(user_collection, designID, color_code, quantity=quantity)
            missing_pieces[(designID, color_code)] = amount
    return missing_pieces


def users_worth_collaborating_with(set_name, user_collection):
    all_users = get_all_users()["Users"]
    users_worth_collabing_with = []
    for user in all_users:
        missing_pieces = helper_functions.compile_missing_pieces_list(set_name=set_name,
                                                                      user_collection=user_collection)
        potential_collab_mate_collection = helper_functions.get_user_collection_by_id(user_id=user["id"])

        not_missing_pieces = []

        for (designID, color_code), amount_missing in missing_pieces.items():
            variant = extract_variant_from_user_collection(potential_collab_mate_collection, designID, color_code)
            if variant:
                if amount_missing - variant["count"] <= 0:
                    not_missing_pieces.append((designID, color_code))

        if len(missing_pieces.keys()) == len(not_missing_pieces):
            users_worth_collabing_with.append(user["username"])
    return users_worth_collabing_with
