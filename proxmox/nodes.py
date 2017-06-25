from proxmox import connect


class Nodes:
    def __init__(self, auth):
        self.conn = connect.Connect(auth)

    def get_nodes(self):
        return self.conn.connect('nodes')

    # apt
    def get_apt(self, node):
        return self.conn.connect('nodes/' + node + '/apt')

    def get_apt_versions(self, node):
        return self.conn.connect('nodes/' + node + '/apt/versions')

    def get_apt_updates(self, node):
        return self.conn.connect('nodes/' + node + '/apt/update')

    def get_apt_changelog(self, node):
        return self.conn.connect('nodes/' + node + '/apt/changelog')

    # ceph

    def get_ceph_flags(self, node):
        return self.conn.connect('nodes/' + node + '/ceph/flags')

    def get_ceph_mon(self, node):
        return self.conn.connect('nodes/' + node + '/ceph/mon')

    def get_ceph_osd(self, node):
        return self.conn.connect('nodes/' + node + '/ceph/osd')

    def get_ceph_pools(self, node):
        return self.conn.connect('nodes/' + node + '/ceph/pools')

    def get_ceph_config(self, node):
        return self.conn.connect('nodes/' + node + '/ceph/config')

    def get_ceph_crushmap(self, node):
        return self.conn.connect('nodes/' + node + '/ceph/crush')

    def get_ceph_disks(self, node):
        return self.conn.connect('nodes/' + node + '/ceph/disks')

    def get_ceph_logs(self, node):
        return self.conn.connect('nodes/' + node + '/ceph/log')

    def get_ceph_status(self, node):
        return self.conn.connect('nodes/' + node + '/ceph/status')

    # disks
    def get_disks(self, node):
        return self.conn.connect('nodes/' + node + '/disks')

    def get_disks_lists(self, node):
        return self.conn.connect('nodes/' + node + '/disks/list')

    def get_disks_smart(self, node):
        return self.conn.connect('nodes/' + node + '/disks/smart')

    # firewall

    def get_firewall(self, node):
        return self.conn.connect('nodes/' + node + '/firewall')

    def get_firewall_rules(self, node):
        return self.conn.connect('nodes/' + node + '/firewall/rules')

    def get_firewall_rules_atposition(self, node, position):
        return self.conn.connect('nodes/' + node + '/firewall/rules/' + position)

    def get_firewall_log(self, node):
        return self.conn.connect('nodes/' + node + '/firewall/log')

    def get_firewall_options(self, node):
        return self.conn.connect('nodes/' + node + '/firewall/options')
