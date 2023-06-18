from fastapi import APIRouter, HTTPException

from app.api import crud
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema
from app.models.tortoise import SummarySchema

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema)\
        -> SummaryPayloadSchema:
    summary_id = await crud.post(payload)

    return {"id": summary_id, "url": payload.url}


@router.get("/{id}/", response_model=SummarySchema)
async def get_summary(id: int):
    summary = await crud.get_summary(id)
    if summary:
        return summary
    raise HTTPException(status_code=404, detail="Summary not found")


@router.get("/", response_model=list[SummarySchema])
async def get_all():
    return await crud.get_all()
