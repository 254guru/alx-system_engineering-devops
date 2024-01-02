#!/usr/bin/python3
"""
script that uses a REST API for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    function that crawls the API and returns the employee progress
    """
    base_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(base_url)

    if response.status_code == 200:
        todos = response.json()

        # Fetching user data separately to get the user's name
        user_res = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        if user_res.status_code == 200:
            user_data = user_response.json()
            employee_name = user_data['name']
        else:
            print(f"Failed to fetch user data. Status code: {user_res.status_code}")
            return

        completed_tasks = [task['title'] for task in todos if task['completed']]
        total_tasks = len(todos)

        print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        employee_id = sys.argv[1]
        fetch_employee_todo_progress(employee_id)
