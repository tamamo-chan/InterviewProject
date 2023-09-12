from typing import List

import helper_functions
from helper_functions.api_data_retrieval import get_all_users


def main():
    username = "landscape-artist"
    set_name = "tropical-island"
    user_collection = helper_functions.get_user_collection_by_username(username=username)

    return helper_functions.users_worth_collaborating_with(set_name, user_collection)



if __name__ == "__main__":
    print(main())
