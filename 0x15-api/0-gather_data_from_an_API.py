import requests
import sys

def get_employee_todo_progress(employee_id):
    # Make a GET request to the API endpoint
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    
    # Check if the request was successful
    if response.status_code == 200:
        todos = response.json()
        
        # Filter completed tasks
        completed_tasks = [todo['title'] for todo in todos if todo['completed']]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todos)
        
        # Get employee name
        user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        if user_response.status_code == 200:
            employee_name = user_response.json()['name']
        else:
            print("Failed to retrieve employee name.")
            return
        
        # Display employee TODO list progress
        print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task}")
    else:
        print("Failed to retrieve TODO list.")

# Check if the script was provided an employee ID parameter
if len(sys.argv) < 2:
    print("Please provide the employee ID as a parameter.")
else:
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)

