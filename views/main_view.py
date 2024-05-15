from fastapi import APIRouter, HTTPException



router = APIRouter()


@router.get('/')
async def index():
    return {'message':'Hello World'}
