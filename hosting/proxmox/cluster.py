from hosting.proxmox import connect


class Cluster:
    def __init__(self, auth):
        self.conn = connect.Connect(auth)

    def get_cluster(self):
        return self.conn.connect('cluster')

    # backup

    def get_cluster_backup(self):
        return self.conn.connect('cluster/backup')

    def get_cluster_backup_by_id(self, id):
        return self.conn.connect('cluster/backup/' + id)

    # config

    def get_cluster_config(self):
        return self.conn.connect('cluster/config')

    def get_cluster_config_nodes(self):
        return self.conn.connect('cluster/config/nodes')

    def get_cluster_config_totem(self):
        return self.conn.connect('cluster/config/totem')

    # firewall

    def get_cluster_firewall(self):
        return self.conn.connect('cluster/firewall')

    def get_cluster_firewall_aliases(self):
        return self.conn.connect('cluster/firewall/aliases')

    def get_cluster_firewall_aliases_by_name(self, name):
        return self.conn.connect('cluster/firewall/aliases/' + name)

    def get_cluster_firewall_groups(self):
        return self.conn.connect('cluster/firewall/groups')

    def get_cluster_firewall_groups_by_group(self,group):
        return self.conn.connect('cluster/firewall/groups/' + group)

    def get_cluster_firewall_groups_by_group_by_posiiton(self,group, pos):
        return self.conn.connect('cluster/firewall/groups/' + group + '/' + pos)

    def get_cluster_firewall_ipset(self):
        return self.conn.connect('cluster/firewall/ipset')

    def get_cluster_firewall_ipset_by_name(self,name):
        return self.conn.connect('cluster/firewall/ipset/' + name)

    def get_cluster_firewall_ipset_by_name_by_cidr(self,name,cidr):
        return self.conn.connect('cluster/firewall/ipset/' + name + '/cidr')

    def get_cluster_firewall_rules(self):
        return self.conn.connect('cluster/firewall/rules')

    def get_cluster_firewall_rules_by_position(self, pos):
        return self.conn.connect('cluster/firewall/rules/' + pos)

    def get_cluster_firewall_macros(self):
        return self.conn.connect('cluster/firewall/macros')

    def get_cluster_firewall_options(self):
        return self.conn.connect('cluster/firewall/options')

    def get_cluster_firewall_refs(self):
        return self.conn.connect('cluster/firewall/refs')


    # ha

    def get_cluster_ha(self):
        return self.conn.connect('cluster/ha')

    def get_cluster_ha_groups(self):
        return self.conn.connect('cluster/ha/groups')

    def get_cluster_ha_groups_by_group(self, group):
        return self.conn.connect('cluster/ha/groups/' + group)

    def get_cluster_ha_resources(self):
        return self.conn.connect('cluster/ha/resources')

    def get_cluster_ha_resources_by_sid(self,sid):
        return self.conn.connect('cluster/ha/resources/' + sid)

    def get_cluster_ha_status(self):
        return self.conn.connect('cluster/ha/status')

    def get_cluster_ha_status_current(self):
        return self.conn.connect('cluster/ha/status/current')

    def get_cluster_ha_status_manager_status(self):
        return self.conn.connect('cluster/ha/status/manager_status')


    def get_cluster_log(self):
        return self.conn.connect('cluster/log')

    def get_cluster_nextid(self):
        return self.conn.connect('cluster/nextid')

    def get_cluster_options(self):
        return self.conn.connect('cluster/options')

    def get_cluster_resources(self):
        return self.conn.connect('cluster/resources')

    def get_cluster_status(self):
        return self.conn.connect('cluster/status')

    def get_cluster_tasks(self):
        return self.conn.connect('cluster/tasks')

























