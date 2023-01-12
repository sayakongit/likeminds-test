import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--addAccess', type=str, choices=['READ', 'WRITE'])
parser.add_argument('--addResource', type=str)
parser.add_argument('--addAccessOnResource', type=str, nargs=2)
parser.add_argument('--addRole', type=str)
parser.add_argument('--addUser', type=str)
parser.add_argument('--addAccessOnResourceToRole', type=str, nargs=3)
parser.add_argument('--addRoleToUser', type=str, nargs=2)
parser.add_argument('--checkAccess', type=str, nargs=3)

arg1 = parser.parse_args()
resources = {}
roles = {}
users = {}


if arg1.addAccess:
    print(arg1.addAccess, "access has been given")
    
if arg1.addResource:
    resources[arg1.addResource] = []
    print(arg1.addResource, "has been added as a resource")
    
if arg1.addAccessOnResource:
    access, resource = arg1.addAccessOnResource
    resources[resource].append(access)
    print(resource, "has been given", access, 'access')
    
if arg1.addAccessOnResourceToRole:
    access, resource, role = arg1.addAccessOnResourceToRole
    temp = {
        'access': access,
        'resource': resource
    }
    roles[role].append(temp)
    print(resource, "has been given", access, 'access to', role)
    
if arg1.addRole:
    roles[arg1.addRole] = []
    print(arg1.addRole, "role has been created")
    
if arg1.addUser:
    users[arg1.addUser] = []
    print(arg1.addUser, "has been created")
    
if arg1.addRoleToUser:
    role, user = arg1.addRoleToUser
    users[user] = role
    print(user, "has been given", role, 'roll')
    
if arg1.checkAccess:
    user, resource, access = arg1.checkAccess
    temp_user = users[user]
    if temp_user['resource'] == resource and temp_user['access'] == access:
        print('Yes')
    
    print("No")