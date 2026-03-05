
from fastapi import APIRouter

router = APIRouter()

@router.get("/test")
def get_test():
    return {"message": "test endpoint"}
