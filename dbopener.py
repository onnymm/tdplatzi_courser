def extract_data():
    data = []
    with open("data.txt", "r+", encoding="utf-8") as file:
        for line in file:
            if line[-1:] == "\n":
                data.append(line[:-1])
            else:
                data.append(line)
    return data

def classes_classifier(lines):
    content = {}
    stage = ["Clase", "Repaso"]
    for i in stage:
        lessons = []
        for j in lines:
            if j.startswith("*"):
                lessons.append([f"* ◽{j[1:]}", 4])
            elif j.lower() == "quiz":
                lessons.append([j, 2])
            else:
                lessons.append([f"{j} `{i}`", 4])
        content[i] = lessons
    return content

def data_organizer():
    structure = {}
    data = extract_data()
    structure["title"] = data[0]
    structure["description"] = data[1]
    structure["content"] = classes_classifier(data[2:])
    print(structure)

data_organizer()