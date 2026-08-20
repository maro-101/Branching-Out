import json


def load_users(filepath="users.json"):
    """Load and return user data from a JSON file."""
    try:
        with open(filepath, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        return []


def print_results(filtered_users, filter_type):
    """Print the list of matched users or a fallback message if empty."""
    if filtered_users:
        for user in filtered_users:
            print(user)
    else:
        print(f"There is no entry for that {filter_type}.")


def filter_users_by_name(users, name):
    """Filter and display users matching the given name (case-insensitive)."""
    filtered = [u for u in users if u.get("name", "").lower() == name.lower()]
    print_results(filtered, "name")


def filter_users_by_age(users, age):
    """Filter and display users matching the given age."""
    filtered = [u for u in users if u.get("age") == age]
    print_results(filtered, "age")


def filter_users_by_email(users, email):
    """Filter and display users matching the given email (case-insensitive)."""
    filtered = [u for u in users if u.get("email", "").lower() == email.lower()]
    print_results(filtered, "email")


def main():
    """Prompt the user for a filter option and execute the search."""
    users = load_users()
    if not users:
        return

    filter_option = (
        input("What would you like to filter by? (name, age, email): ")
        .strip()
        .lower()
    )

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(users, name_to_search)

    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: ").strip())
            filter_users_by_age(users, age_to_search)
        except ValueError:
            print("Please enter a valid integer for age.")

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(users, email_to_search)

    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()