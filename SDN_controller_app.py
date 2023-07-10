from rina.coreManager import *
from rina.manager import *

cm1 = RinaCoreManager()
cm1.add_system("http://192.168.10.255:5000", "core1", "master", "10")
cm1.list_systems()
cm1.create_dif("10","7")