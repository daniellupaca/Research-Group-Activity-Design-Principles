tasks = []

def add_task(description):
    tasks.append({"description": description, "done": False})

def list_tasks():
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['description']}")

def complete_task(index):
    if 0 < index <= len(tasks):
        tasks[index - 1]["done"] = True

# Example usage:
if __name__ == "__main__":
    add_task("Finish article for Dev.to")
    add_task("Record explanation video")
    print("Initial task list:")
    list_tasks()
    complete_task(1)
    print("\nAfter completing task 1:")
    list_tasks()