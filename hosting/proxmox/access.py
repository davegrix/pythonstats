from hosting.proxmox import connect


class Access:
    def __init__(self, auth):
        self.conn = connect.Connect(auth)

    def get_access(self):
        return self.conn.connect('access')

    # domains
    def get_access_domains(self):
        return self.conn.connect('access/domains')

    def get_access_domains_by_realm(self, realm):
        return self.conn.connect('access/domains/' + realm)

    # groups
    def get_access_groups(self):
        return self.conn.connect('access/groups')

    def get_access_groups_by_id(self, id):
        return self.conn.connect('access/groups/' + id)

    # roles
    def get_access_roles(self):
        return self.conn.connect('access/roles')

    def get_access_roles_by_id(self,id):
        return self.conn.connect('access/roles/' + id)

    # users
    def get_access_users(self):
        return self.conn.connect('access/users')

    def get_access_users_by_id(self, userid):
        return self.conn.connect('access/users/' + userid)

    def get_access_acl(self):
        return self.conn.connect('acl')

    def get_access_ticket(self):
        return self.conn.connect('ticket')

