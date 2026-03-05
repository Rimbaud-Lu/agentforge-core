
from fastapi import APIRouter

router = APIRouter()

@router.get("/create api")
def get_create api():
    return {"message": "create api endpoint"}
