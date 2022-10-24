RESTful APIs with following. 

# Specifications:
# where each task can have more than one assignee, and each project has multiple tasks
    ##• There are two roles: 
        ###◦ Developer
        ###◦ Project Manager

Developers can:
    • Add task and assign it to themself
    • Retrieve all tasks on their project
Project Manager can:
    • Add/Retrieve projects
    • Assign projects to Developers
    • Add/Retrieve tasks within their own projects
End Points: 
  login,
  signup,
  list of tasks in a project (developers can see others’ tasks in the project too),
  list of user’s tasks in the project, Project Manager assigns task to a developer (check permissions).
