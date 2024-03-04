from fastapi import APIRouter, HTTPException, status
from models.users import User, UserSignIn

user_router = APIRouter(
    tags=["User"],
)
users={}

# /signup : 등록
@user_router.post("/signup")
async def sigin_new_user(data: User) -> dict:
    # 이미 등록되어 있는 사용자의 경우 오류 반환
    if data.email in users:
        raise HTTPException(
            status_code =status.HTTP_409_CONFLICT,
            detail="User with supplied username exists"
        )
    users[data.email] = data
    print(f"Register email : {data.email}")

    return {
        "message":"User successfully registered!"
    }

# /signin: 로그인
@user_router.post("/signin")
async def sign_user_in(user: UserSignIn) -> dict:
    # 사용자의 이메일을 찾을 수 없는 경우 오류 반환
    print("user list : ", users)
    print("sign user : ", user)
    print(f"Try sign in email : {user.email}")

    if user.email not in users:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail="User does not exist"
        )    
    if users[user.email].password != user.password:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Wrong credentials passed"
        )
    return {
        "message":"User signed in successfully."
    }