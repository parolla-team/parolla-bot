from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.api.schemas.exceptions.errors import DoesNotExistsError
from app.api.schemas.request.user import UserCreateRequest
from app.api.schemas.response.user import UserGetResponse, UsersListResponse
from app.containers import Container
from app.infra.unit_of_work.database import Uow

router = APIRouter(prefix="/v1/users")


@router.get("/", response_model=UsersListResponse)
@inject
async def get_user_list(uow: Uow = Depends(Provide[Container.db.container.uow])) -> UsersListResponse:
    users = await uow.users.all()
    return UsersListResponse(users=[UserGetResponse.model_validate(user_row) for user_row in users])


@router.get("/{user_id}", response_model=UserGetResponse)
@inject
async def get_user(user_id: int, uow: Uow = Depends(Provide[Container.db.container.uow])) -> UserGetResponse:
    user = await uow.users.get_by_id(user_id)
    if user is None:
        raise DoesNotExistsError
    return UserGetResponse.model_validate(user)


@router.post("/", response_model=UserGetResponse)
@inject
async def create_user(user_in: UserCreateRequest, uow: Uow = Depends(Provide[Container.db.container.uow])) -> dict:
    await uow.users.save(UserCreateRequest.model_validate(user_in))
    return {"status": "created"}
