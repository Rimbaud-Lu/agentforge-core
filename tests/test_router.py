from skills.router import select_skill
from model_execution.router import select_model

def test_skill_router():
    skill = select_skill("create api")
    assert skill is not None

def test_model_router():
    model = select_model("architecture")
    assert model is not None
