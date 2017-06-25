from proxmox import connect


class Pools:
    def __init__(self, auth):
        self.conn = connect.Connect(auth)

    def get_pools(self):
        return self.conn.connect('pools')

    def get_pool_by_id(self, id):
        return self.conn.connect('pools/' + id)

