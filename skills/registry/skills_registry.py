skills = {}

def register(name, fn):
    skills[name] = fn

def get_skill(name):
    return skills.get(name)
