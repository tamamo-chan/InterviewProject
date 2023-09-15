import brickfan35
import dr_crocodile
import landscape_artist

if __name__ == '__main__':
    print(f"BrickFan35 can build the following sets: {brickfan35.main()}")
    print("landscape-artist can collaborate with the following users to build the tropical island set: "
          f"{landscape_artist.main()}")
    print("User dr_crocodile would be able to build the following sets "
          f"if he is able to substitute colors of certain pieces: {dr_crocodile.main()}")


