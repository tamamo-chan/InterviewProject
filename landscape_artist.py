from typing import List

import helper_functions
from helper_functions.api_data_retrieval import get_all_users
from objects.User import User


def main():
    username = "landscape-artist"
    set_name = "tropical-island"
    user = User(username)

    return helper_functions.users_worth_collaborating_with(set_name, user)



if __name__ == "__main__":
    print(main())
