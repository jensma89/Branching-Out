import json


def get_user_data(file_path):
    """Read the JSON file."""
    with open(file_path, "r") as file:
        return json.load(file)


def filter_by_email(email):
    """Filter user data by e-mail address."""
    users = get_user_data("users.json")
    filtered_users_by_email = [user for user in users
                               if user['email'].lower() == email.lower()]

    for user in filtered_users_by_email:
        print(user)


def filter_by_age(age):
    """Filter the user data by age."""
    users = get_user_data("users.json")
    filtered_users_by_age = [user for user in users
                             if user['age'] == age]

    for user in filtered_users_by_age:
        print(user)


def filter_users_by_name(name):
    """Filter the user data by name."""
    users = get_user_data("users.json")
    filtered_users = [user for user in users
                      if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? "
                          "('name', 'age' or by 'e-mail'): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name "
                               "to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "age":
        age_to_search = int(input("Enter an age "
                                  "to filter users: ").strip())
        filter_by_age(age_to_search)
    elif filter_option == "e-mail":
        email_to_search = input("Enter an e-mail address "
                                "to filter users: ").strip()
        filter_by_email(email_to_search)
    else:
        print("Filtering by that option is not yet supported.")

