import csv

from fastapi import APIRouter,HTTPException

from models import User

router = APIRouter(prefix="/users", tags=["users"])

@router.get('')
def get_users():
    with open('db/users.csv',"r",newline="",encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        users=list(csv_dict_reader)
        for user in users:
            user.pop("id")
        return users

@router.get('/get_users')
def get_user(username:str):
    with open('db/users.csv',"r",newline="",encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile)
        for user in csv_dict_reader:
            if username.lower() in user["username"].lower():
                user.pop("id")
                return user
        raise HTTPException(status_code=404, detail="User not found")

@router.post('/create')
def create_user(user:User):
    field_names=["id","username","password"]
    with open('db/users.csv',"r+",newline="",encoding="utf-8") as csvfile:
        csvfile.seek(0)
        lines = len(csvfile.readlines())
        csv_dict_writer = csv.DictWriter(csvfile, fieldnames=field_names)
        csv_dict_writer.writerow({"id":lines,"username":user.username,"password":user.password})
        return "Added user successfully"



@router.post('/login')
def login(user: User):
    field_names = ["username", "password"]
    with open('db/users.csv', "r", newline="", encoding="utf-8") as csvfile:
        csv_dict_reader = csv.DictReader(csvfile, fieldnames=field_names)
        for record in csv_dict_reader:
            if record["username"] == user.username:
                if record["password"] == user.password:
                    return {"message": "Login successful", "user": record["username"]}
                else:
                    raise HTTPException(status_code=401, detail="Incorrect password")
        raise HTTPException(status_code=404, detail="User not found")