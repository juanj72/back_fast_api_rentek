from fastapi import APIRouter, HTTPException



router = APIRouter()


@router.get('/{id}')
async def index(id):
    message = f'Este es mi id : {id}'

    return {'message':message}
