from hosting.proxmox import connect


class Storage:
    def __init__(self, auth):
        self.conn = connect.Connect(auth)

    def get_storage(self):
        return self.conn.connect('storage')

    def get_storage_by_id(self, id):
        return self.conn.connect('storage/' + id)

