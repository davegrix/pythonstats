# Proxmox
from proxmox.version import Version

from proxmox.auth import *
from proxmox.pools import Pools
from proxmox.storage import Storage

prox_auth = Auth("https://10.0.0.10:8006/api2/json/", "root@pam", "1butter22")

versions = Version(prox_auth)
pools = Pools(prox_auth)
storage = Storage(prox_auth)
print(versions.get_version())
print(pools.get_pools())
print(storage.get_storage())
print(storage.get_storage_by_id('local'))