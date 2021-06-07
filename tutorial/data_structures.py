evaluations = []
evaluations.append({'task_id': 1, 'setting_id': 11, 'setting_name': 'a'})
evaluations.append({'task_id': 2, 'setting_id': 21, 'setting_name': 'b'})
tasks = [e['task_id'] for e in evaluations]
print(type(tasks))
print(tasks)

print("======================================================")
# A tuple consists of a number of values separated by commas,
# they may be input with or without surrounding parentheses
t = 1,
print(type(t))  # tuple
d = (1)
print(type(d))  # int

# set
# Note: to create an empty set you have to use set(), not {};
# {}是dict类型
