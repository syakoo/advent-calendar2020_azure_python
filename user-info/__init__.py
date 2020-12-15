import azure.functions as func
from azfunc_extensions import doc2dc

from utils.users import User 


def main(req: func.HttpRequest, users: func.DocumentList) -> func.HttpResponse:
    name = req.route_params.get('userName')
    if users:
        u = doc2dc(users[0], User)

        return func.HttpResponse(f"[user-info] Hello, {name}. Your age is {u.age}.")

    return func.HttpResponse(f"[user-info] Hello, {name}.")
