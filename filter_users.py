import json


def filter_users_by_name(name):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print("There is no entry for that name.")

def filter_users_by_age(age):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print("There is no entry for that age.")

def filter_by_email(email):
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print("There is no entry for that email.")






if __name__ == "__main__":
    filter_option = input("What would you like to filter by? (Currently, only 'name', 'age' and 'email' are supported): ").strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)

    elif filter_option == "age":
        age_to_search = int(input("Enter a age to filter users: ").strip())
        filter_users_by_age(age_to_search)

    elif filter_option == "email":
        email_to_search = input("Enter a email to filter users: ").strip()
        filter_by_email(email_to_search)

    else:
        print("Filtering by that option is not yet supported.")
