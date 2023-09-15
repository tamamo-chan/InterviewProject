from helper_functions.api_data_retrieval import get_user_summary, get_user_full_data, get_all_sets, get_set_summary, \
    get_set_full_data, get_all_users
from objects.BuildSet import BuildSet
from objects.User import User


def get_buildable_sets(username):
    if username not in [user["username"] for user in get_all_users()["Users"]]:
        return []
    user = User(username=username)
    sets = BuildSet.get_all_buildSets()
    build_able_sets = []
    for specific_set in sets:

        user_has_all_pieces = True

        for piece, quantity in specific_set.collection.items():
            user_has_piece = 0 >= calculate_missing_pieces(user, piece, quantity)
            if not user_has_piece:
                user_has_all_pieces = False
                break

        if user_has_all_pieces:
            build_able_sets.append(specific_set.name)
    return build_able_sets


def calculate_missing_pieces(user, piece, quantity) -> int:
    amount_available = user.collection.get(piece, 0)
    return quantity - amount_available


def compile_missing_pieces_list(set_name, user):
    set = BuildSet(set_name)
    missing_pieces = {}
    for piece, quantity in set.collection.items():
        amount_missing = calculate_missing_pieces(user, piece, quantity)
        missing_pieces[piece] = amount_missing
    return missing_pieces


def users_worth_collaborating_with(set_name, user):
    all_users = get_all_users()["Users"]
    all_users = [User(user_dict["username"]) for user_dict in all_users if user_dict["username"] != user.username]
    users_worth_collabing_with = []
    for potential_collab_mate in all_users:
        missing_pieces = compile_missing_pieces_list(set_name=set_name, user=user)

        not_missing_pieces = []

        for piece, amount_missing in missing_pieces.items():
            potential_collab_missing = potential_collab_mate.collection.get(piece, 0)
            if amount_missing - potential_collab_missing <= 0:
                not_missing_pieces.append(piece)

        if len(missing_pieces.keys()) == len(not_missing_pieces):
            users_worth_collabing_with.append(potential_collab_mate.username)

    return users_worth_collabing_with
