from todoist_api_python.api import TodoistAPI
from dbopener import data_organizer, get_token
from tasks_creator import course_maker

api = TodoistAPI(get_token())

task = data_organizer()

course_maker(task)