import uuid
import user
import local_json
import ssh

print("""input "adduser <email>" to add user""")

def add_user(email):
    id = str(uuid.uuid4())
    new_user = user.User(id, email)
    local_json.addUser(new_user)
    ssh.ssh()
    print('user added')

while True:
    instruction = input()
    if instruction.split()[0] == 'adduser':
        add_user(instruction.split()[1])