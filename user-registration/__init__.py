import logging

import azure.functions as func
from azfunc_extensions import doc2dc, dc2doc

from utils.users import User


def main(req: func.HttpRequest, users: func.DocumentList, outusers: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    req_body = req.get_json()
    name = req_body.get('name')
    age = req_body.get('age')

    if name and age:
        doc_users = list(filter(lambda x: x.get("name") == name, users))
        if doc_users:
            user = doc2dc(doc_users[0], User)
            user.name = name
            user.age = age
        else:
            user = User(name=name, age=age)
        outusers.set(dc2doc(user))

        return func.HttpResponse(f"[user-registration] Hello, {name}.")
    else:
        return func.HttpResponse(
            "The request body must contain a name and age",
            status_code=200
        )