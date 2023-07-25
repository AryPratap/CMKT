from cmkt.tasks import TaskToolKit
print("\nCMKT tasks  toolkit Demo")
print()

# Initialize hinglish and SpanishEnglish toolkits
hien_toolkit = TaskToolKit("hineng")


# Search tasks available based on task type
# Available Task types, "syntactic", "semantic", "generational" 
task_list_hi = hien_toolkit.list_tasks(task_type="syntactic")
print("Tasks for hinglish toolkit language") 
print(task_list_hi)
print()

# List model information based on task 
model_ner = hien_toolkit.task_model_info(task="ner", details=False)
print("models for ner task")
print(model_ner)
print()

model_lid = hien_toolkit.task_model_info(task="lid", details=True)
print("models for lid task")
print(model_lid)
print()

model_pos = hien_toolkit.task_model_info(task="pos", details=True)
print("models for pos task")
print(model_pos)
print()











