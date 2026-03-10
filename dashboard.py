def show_dashboard(user):
    """
    Sample function to demonstrate a dashboard view.
    """
    if not user:
        print("No user specified.")
        return

    print(f"Welcome to the dashboard, {user}!")
    data = get_dashboard_data(user)
    print("Your dashboard data:")
    for key, value in data.items():
        print(f"{key}: {value}")

def get_dashboard_data(user):
    """
    Sample data retrieval function for the dashboard.
    """
    # Sample data
    return {
        "tasks_completed": 7,
        "messages": 3,
        "notifications": 5,
        "last_login": "2024-06-10"
    }

if __name__ == "__main__":
    user = "Alice"
    show_dashboard(user)