from todoist_api_python.api import TodoistAPI
from dbopener import get_token, get_project

def course_maker(structure):
    # Se inicializa ToDoist API
    api = TodoistAPI(get_token())

    # Se asigna ID del proyecto
    project = get_project()

    # Se crea tarea principal contenedora de las tareas del curso
    main = api.add_task(
        content=(f"**{structure['title']}**"),
        description=structure["description"],
        project_id=project,
        labels=["Mi11T", "Laptop", "Platzi", "Curso"],
        priority=4
        )
    
    # Se crea la sección de las lecciones
    lesson = api.add_task(
        content="* ◽Clases",
        parent_id=main.id
    )

    # Se crean las tareas de las lecciones
    for i in structure["content"]["Clase"]:
        api.add_task(
            content=i[0],
            priority=i[1],
            parent_id=lesson.id
        )

    # Se crea la sección de los repasos
    review = api.add_task(
        content="* ◽Repaso",
        parent_id=main.id
    )

    # Se crean las tareas del repaso
    for i in structure["content"]["Repaso"]:
        api.add_task(
            content=i[0],
            priority=i[1],
            parent_id=review.id
        )

    # Se crea la tarea del examen de acreditación
    api.add_task(
        content="Examen de acreditación",
        priority=4,
        parent_id=main.id
        )