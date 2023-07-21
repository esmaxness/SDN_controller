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

First, it is highly recommended to install IRATI stack in the same system that this example are going to run. To do so, the [IRATI Project](https://github.com/IRATI/stack) describes the steps to install IRATI. 

Finally, it is necessary to install the RINA SBI Driver using the rina_driver wheel available at [IRATI Project](https://github.com/esmaxness/RINA_Driver)

```
pip install rina-0.0.3-py3-none-any.whl
```

### Installing

1. Clone this repository in the same system with [IRATI Project](https://github.com/IRATI/stack)
2. Create a folder with the DIF templates.
```
sudo mkdir /tmp/DifTemplates
```

## Usage <a name = "usage"></a>

1. Crea
