import os


_version = "0.0.1"


def main():
    user = os.getuid()
    print(f"Hello {user}!")


if __name__ == "__main__":
    main()
