from flask import Blueprint, jsonify
from .apis import APIS

endpoints_bp = Blueprint(__name__, __name__)


@endpoints_bp.route("/")
def get_users():

    apis = APIS()
    memberships = apis.get_project_memberships()
    memberships = membership_dict(memberships)
    unregister_users = apis.get_unregister_users()
    register_users = apis.get_register_users()
    all_users = register_users+unregister_users

    for i in range(len(all_users)):
        user_id = all_users[i]['id']
        all_users[i]['projectIds'] = memberships.get(user_id, [])

    return jsonify(all_users)


def membership_dict(memberships):
    result = {}
    for record in memberships:
        user_id = record['userId']
        project_id = record.get('projectId')
        if user_id not in result:
            result[user_id] = []
        result[user_id].append(project_id)

    return result
