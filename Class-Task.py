class Task:
    def __init__(self):
        # Список для хранения задач
        self.tasks = []

    def add_task(self, description, deadline):
        # Добавляем задачу в виде словаря
        self.tasks.append({"description": description, "deadline": deadline, "status": "Не выполнено"})

    def mark_task_completed(self, description):
        # Ищем задачу по описанию и отмечаем ее выполненной
        for task in self.tasks:
            if task["description"] == description:
                task["status"] = "Выполнено"
                print(f"Задача '{description}' выполнена")
                return
        print(f"Задача '{description}' не найдена")

    def all_task(self):
        print("Текущие задачи:")
        # Выводим все задачи, которые не выполнены
        for task in self.tasks:
            if task["status"] == "Не выполнено":
                print(f"{task['description']} - {task['deadline']}")

task_manager = Task()

task_manager.add_task("Complete project", "2024-10-20")
task_manager.add_task("Go shopping", "2024-10-18")
task_manager.mark_task_completed("Go shopping")
task_manager.all_task()
