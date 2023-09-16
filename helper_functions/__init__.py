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
    missing_pieces = compile_missing_pieces_list(set_name=set_name, user=user)
    for potential_collab_mate in all_users:

        not_missing_pieces = []

        for piece, amount_missing in missing_pieces.items():
            potential_collab_missing = potential_collab_mate.collection.get(piece, 0)
            if amount_missing - potential_collab_missing <= 0:
                not_missing_pieces.append(piece)

        if len(missing_pieces.keys()) == len(not_missing_pieces):
            users_worth_collabing_with.append(potential_collab_mate.username)

    return users_worth_collabing_with


def buildable_sets_with_substitutable_colors(username):
    user = User(username)
    all_sets = BuildSet.get_all_buildSets()

    buildable_sets = []
    for build_set in all_sets:
        buildable = True
        pieces_that_already_works = [(temp_piece, missing) for (temp_piece, missing) in
                                     compile_missing_pieces_list(build_set.name, user).items() if missing <= 0]
        used_colors = list(set([temp_piece.color for (temp_piece, missing) in pieces_that_already_works]))

        set_collection_based_on_id = calculate_set_collection_based_on_id(build_set, pieces_that_already_works)

        user_collection_based_on_id = calculate_user_collection_based_on_id(used_colors,
                                                                            user)

        for piece_id, color_list in set_collection_based_on_id.items():
            if not buildable:
                break
            if piece_id not in user_collection_based_on_id.keys():
                buildable = False
                break
            relevant_user_pieces = calculate_relevant_pieces_from_user(user_collection_based_on_id.get(piece_id), used_colors)

            for color_dict in color_list:
                color_code_with_closest_amount = closest_value(relevant_user_pieces, next(iter(color_dict.values())))
                if not color_code_with_closest_amount:
                    buildable = False
                    break
                used_colors.append(color_code_with_closest_amount)
                relevant_user_pieces = calculate_relevant_pieces_from_user(relevant_user_pieces, used_colors)

        if buildable:
            buildable_sets.append(build_set.name)

    return buildable_sets


def calculate_user_collection_based_on_id(used_colors, user):
    user_collection_based_on_id = {}
    for user_piece, quantity in user.collection.items():
        if user_piece.color in used_colors:
            continue

        if user_piece.id not in user_collection_based_on_id.keys():
            user_collection_based_on_id[user_piece.id] = [{user_piece.color: quantity}]
        else:
            user_collection_based_on_id[user_piece.id].append({user_piece.color: quantity})
    return user_collection_based_on_id


def calculate_set_collection_based_on_id(build_set, pieces_that_already_works):
    set_collection_based_on_id = {}
    for set_piece, quantity in [
        (piece, quantity) for (piece, quantity) in build_set.collection.items()
        if piece not in [working_piece for working_piece, missing_amount in pieces_that_already_works]
    ]:
        if set_piece.id not in set_collection_based_on_id.keys():
            set_collection_based_on_id[set_piece.id] = [{set_piece.color: quantity}]
        else:
            set_collection_based_on_id[set_piece.id].append({set_piece.color: quantity})
    return set_collection_based_on_id


def calculate_relevant_pieces_from_user(relevant_user_pieces, used_colors):
    relevant_user_pieces = [color_dict for color_dict in relevant_user_pieces
                            if next(iter(color_dict.keys())) not in used_colors]
    return relevant_user_pieces


def closest_value(color_list: list, k: int) -> str:
    closest_key = None
    closest_val = float('inf')

    for color_dict in color_list:
        quantity = next(iter(color_dict.values()))
        if quantity >= k and abs(quantity - k) < abs(closest_val - k):
            closest_val = quantity
            closest_key = next(iter(color_dict.keys()))

    return closest_key
