from hosting.proxmox import connect


class Version:
    def __init__(self, auth):
        self.conn = connect.Connect(auth)

    def get_version(self):
        return self.conn.connect('version')
