

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Tarefa '{task}' adicionada com sucesso.")

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Tarefa '{task}' removida com sucesso.")
        else:
            print(f"Tarefa '{task}' não encontrada na lista.")

    def display_tasks(self):
        if self.tasks:
            print("Lista de Tarefas:")
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        else:
            print("Nenhuma tarefa na lista.")

# Instanciando a lista de tarefas
to_do_list = ToDoList()

# Adicionando tarefas
to_do_list.add_task("Estudar Python")
to_do_list.add_task("Fazer exercícios físicos")

# Exibindo as tarefas
to_do_list.display_tasks()

# Removendo uma tarefa
to_do_list.remove_task("Fazer exercícios físicos")

# Exibindo as tarefas atualizadas
to_do_list.display_tasks()



