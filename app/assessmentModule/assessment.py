from fastapi import APIRouter

router = APIRouter(
    prefix="/assess",
    tags=["assessment"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_assessment():
    return {"This is the assessment api"}
