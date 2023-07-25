#!/usr/bin/python3
import json
import urllib.request

def get_employee_todo_list_progress(employee_id):
    # API URL to get the employee's TODO list
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    try:
        # Send a GET request to the API
        with urllib.request.urlopen(url) as response:
            todo_list = json.loads(response.read())

            # Extract relevant information
            employee_name = todo_list[0]['name']
            total_tasks = len(todo_list)
            done_tasks = sum(1 for task in todo_list if task['completed'])
            completed_tasks_titles = [task['title'] for task in todo_list if task['completed']]

            # Print the results in the required format
            print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
            for task_title in completed_tasks_titles:
                print(f"\t{task_title}")

    except urllib.error.HTTPError as e:
        print(f"Error: Failed to fetch data. Status code: {e.code}")
    except urllib.error.URLError as e:
        print(f"Error: Failed to connect to the API: {e.reason}")
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON response from the API.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID should be an integer.")
        sys.exit(1)

    get_employee_todo_list_progress(employee_id)

