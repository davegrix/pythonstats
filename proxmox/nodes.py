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

    # lxc

    def get_lxc(self, node):
        return self.conn.connect('nodes/' + node + '/lxc')

    def get_lxc_firewall(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/firewall')

    def get_lxc_firewall_aliases(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/firewall/aliases')

    def get_lxc_firewall_aliases_by_name(self, node, vmid, name):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/firewall/aliases/' + name)

    def get_lxc_firewall_ipset(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/firewall/ipset')

    def get_lxc_firewall_ipset_by_name(self, node, vmid, name):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/firewall/ipset/' + name)

    def get_lxc_firewall_ipset_cdr_by_name(self, node, vmid, name, cidr):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/firewall/ipset/' + name + '/' + cidr)

    def get_lxc_firewall_rules(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/firewall/rules')

    def get_lxc_firewall_rules_by_pos(self, node, vmid, pos):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/firewall/rules/' + pos)

    def get_lxc_firewall_log(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/firewall/log')

    def get_lxc_firewall_options(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/firewall/options')

    def get_lxc_firewall_refs(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/firewall/refs')

    def get_lxc_snapshot(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/snapshot')

    def get_lxc_snapshot_by_name(self, node, vmid, name):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/snapshot/' + name)

    def get_lxc_status(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/status')

    def get_lxc_status_current(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/status/current')

    def get_lxc_config(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/config')

    def get_lxc_feature(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/feature')

    def get_lxc_rrd(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/rrd')

    def get_lxc_rrddata(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/rrddata')

    def get_lxc_vncwebsocket(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/lxc/' + vmid + '/vncwebsocket')

    # network

    def get_network(self, node):
        return self.conn.connect('nodes/' + node + '/network')

    def get_network_by_interface(self, node, iface):
        return self.conn.connect('nodes/' + node + '/network/' + iface)

    # qemu

    def get_qemu(self, node):
        return self.conn.connect('nodes/' + node + '/qemu')

    def get_qemu_firewall(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/firewall')

    def get_qemu_firewall_aliases(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/firewall/aliases')

    def get_qemu_firewall_aliases_by_name(self, node, vmid, name):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/firewall/aliases/' + name)

    def get_qemu_firewall_ipset(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/firewall/ipset')

    def get_qemu_firewall_ipset_by_name(self, node, vmid, name):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/firewall/ipset/' + name)

    def get_qemu_firewall_ipset_cdr_by_name(self, node, vmid, name, cidr):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/firewall/ipset/' + name + '/' + cidr)

    def get_qemu_firewall_rules(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/firewall/rules')

    def get_qemu_firewall_rules_by_pos(self, node, vmid, pos):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/firewall/rules/' + pos)

    def get_qemu_firewall_log(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/firewall/log')

    def get_qemu_firewall_options(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/firewall/options')

    def get_qemu_firewall_refs(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/firewall/refs')

    def get_qemu_snapshot(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/snapshot')

    def get_qemu_snapshot_by_name(self, node, vmid, name):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/snapshot/' + name)

    def get_qemu_status(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/status')

    def get_qemu_status_current(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/status/current')

    def get_qemu_config(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/config')

    def get_qemu_feature(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/feature')

    def get_qemu_pending(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/pending')

    def get_qemu_rrd(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/rrd')

    def get_qemu_rrddata(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/rrddata')

    def get_qemu_vncwebsocket(self, node, vmid):
        return self.conn.connect('nodes/' + node + '/qemu/' + vmid + '/vncwebsocket')

    # scan

    def get_scan_methods(self, node):
        return self.conn.connect('nodes/' + node + '/scan')

    def scan_glusterfs(self, node):
        return self.conn.connect('nodes/' + node + '/scan/glusterfs')

    def scan_iscsi(self, node):
        return self.conn.connect('nodes/' + node + '/scan/iscsi')

    def scan_lvm(self, node):
        return self.conn.connect('nodes/' + node + '/scan/lvm')

    def scan_lvm_thin(self, node):
        return self.conn.connect('nodes/' + node + '/scan/lvmthin')

    def scan_nfs(self, node):
        return self.conn.connect('nodes/' + node + '/scan/nfs')

    def scan_usb(self, node):
        return self.conn.connect('nodes/' + node + '/scan/usb')

    def scan_zfs(self, node):
        return self.conn.connect('nodes/' + node + '/scan/zfs')

    # services

    def get_services(self, node):
        return self.conn.connect('nodes/' + node + '/services')

    def get_service_by_service(self, node, service):
        return self.conn.connect('nodes/' + node + '/services/' + service)

    def get_service_state(self, node, service):
        return self.conn.connect('nodes/' + node + '/services/' + service + '/state')

    # storage

    def get_storage(self, node):
        return self.conn.connect('nodes/' + node + '/storage')

    def get_storage_by_storage(self, node, storage):
        return self.conn.connect('nodes/' + node + '/storage/' + storage)

    def get_storage_by_storage_content(self, node, storage):
        return self.conn.connect('nodes/' + node + '/storage/' + storage + '/content')

    def get_storage_by_storage_content_by_volume(self, node, storage, volume):
        return self.conn.connect('nodes/' + node + '/storage/' + storage + '/content/' + volume)

    def get_storage_rrd(self,node,storage):
        return self.conn.connect('nodes/' + node + '/storage/' + storage + '/rrd')

    def get_storage_rrddata(self,node,storage):
        return self.conn.connect('nodes/' + node + '/storage/' + storage + '/rrddata')

    def get_storage_status(self,node,storage):
        return self.conn.connect('nodes/' + node + '/storage/' + storage + '/status')

    # tasks

    def get_tasks(self, node):
        return self.conn.connect('nodes/' + node + '/tasks')

    def get_tasks_by_upid(self, node, upid):
        return self.conn.connect('nodes/' + node + '/tasks/' + upid)

    def get_tasks_by_upid_log(self, node, upid):
        return self.conn.connect('nodes/' + node + '/tasks/' + upid + '/log')

    def get_tasks_by_upid_status(self, node, upid):
        return self.conn.connect('nodes/' + node + '/tasks/' + upid + '/status')


    def get_aplinfo(self,node):
        return self.conn.connect('nodes/' + node + '/aplinfo')

    def get_dns(self,node):
        return self.conn.connect('nodes/' + node + '/dns')

    def get_netstat(self,node):
        return self.conn.connect('nodes/' + node + '/netstat')

    def get_report(self,node):
        return self.conn.connect('nodes/' + node + '/report')

    def get_rrd(self,node):
        return self.conn.connect('nodes/' + node + '/rrd')

    def get_rrddata(self, node):
        return self.conn.connect('nodes/' + node + '/rrddata')

    def get_status(self, node):
        return self.conn.connect('nodes/' + node + '/status')

    def get_subscription(self, node):
        return self.conn.connect('nodes/' + node + '/subscription')

    def get_syslog(self, node):
        return self.conn.connect('nodes/' + node + '/syslog')

    def get_time(self, node):
        return self.conn.connect('nodes/' + node + '/time')

    def get_version(self, node):
        return self.conn.connect('nodes/' + node + '/version')

    def get_vnc_websocket(self, node):
        return self.conn.connect('nodes/' + node + '/vncwebsocket')









