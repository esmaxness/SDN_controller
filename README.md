# Example of use the RINA SBI Driver

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

This repository aims to provide an example to use the RINA SBI Driver to implement a SDN controller application to manage RINA-based devices at the infrastructure layer. 

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

This example depends on [IRATI Project](https://github.com/IRATI/stack) and RINA SBI Driver.

First, it is highly recommended to install IRATI stack in the same system that this example are going to run. To do so, the [IRATI Project](https://github.com/IRATI/stack) describes the steps to install IRATI. Also, it is important to install IRATI as root.

Finally, it is necessary to install the RINA SBI Driver using the rina_driver wheel available at [IRATI Project](https://github.com/esmaxness/RINA_Driver)

```
pip install rina-0.0.3-py3-none-any.whl
```

### Installing

1. Clone this repository in the same system with [IRATI Project](https://github.com/IRATI/stack).
2. Move the IRATI configuration files from the Configurations folder to the /etc.
3. Change the network interface name in the shim-eth-vlan.dif file with your system interface name. To validate your system interface name you could run ifconfig.
4. Create a folder with the DIF templates in the tmp folder and copy the templates files from the Templates folder.
```
sudo mkdir /tmp/DifTemplates
```
5. Run the management_DAF_up.sh script. This script are going to set a vlan id 100 in your interface, run the IRATI under the ipcm-management.conf, and run the net_manager
```
sudo ./managment_DAF_up.sh
```

If everything is ok, you will see the following IRATI console response:
```
Management Agent name: sdnController-1--
Management Agent active connections  ( Manager name | via DIF )
        terminet.manager-1-- | management

Current IPC processes (id | name | type | state | Registered applications | Port-ids of flows provided)
    1 | sdnController.100:1:: | shim-eth-vlan | ASSIGNED TO DIF 100 | sdnController.management-1-- | -
    2 | sdnController.management:1:: | normal-ipc | ASSIGNED TO DIF management | terminet.manager-1-- | 277, 276
```

6. Now, it is time to run the example application. To do so, it could be run by using Unicorn 

```
sudo python3 -m uvicorn main:app --reload
```
If everything is ok, you will see the following:
```
INFO:     Will watch for changes in these directories: ['/home/terminet/Documentos/Projects/SDN_controller']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [125754] using StatReload
INFO:     Started server process [125758]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```


## Usage <a name = "usage"></a>

The example exposes a well-defined REST API. It is possible to validate the REST API by using swagger at http://127.0.0.1:8000/docs.

To validate the connection with the RINA manager, run:
```
curl -X 'GET' \
  'http://127.0.0.1:8000/list_systems' \
  -H 'accept: application/json'
```

The RINA manager is going to response with the SDN Controller Management Agent because it is the only management agent register into the SDN Controller.
```
[
  {
    "portId": "7",
    "maName": "sdnController-1",
    "systemId": "1"
  }
]
```



