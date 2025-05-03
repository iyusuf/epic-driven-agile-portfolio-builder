import os
from doit import create_after

# Use relative path to Python scripts
DISCOVER_SCRIPT = "infra/pyinfra/explore.pyinfra.py"
PROVISION_SCRIPT = "infra/pyinfra/provision.pyinfra.py"
POSTPROVISION_SCRIPT = "infra/pyinfra/postprovision.pyinfra.py"

PROVISION_OUTPUT = "infra/pyinfra/provisioned-vms.json"
POSTPROVISION_OUTPUT = "infra/pyinfra/postprovision-summary.json"

def task_discover():
    """🔍 Discover Proxmox resources"""
    return {
        'actions': [f'python {DISCOVER_SCRIPT}'],
        'verbosity': 2,
        'file_dep': [DISCOVER_SCRIPT],
        'targets': ['infra/pyinfra/explore.proxmox.json'],
    }

@create_after('discover')
def task_provision():
    """🚀 Provision new VM (depends on discover)"""
    return {
        'actions': [f'python {PROVISION_SCRIPT}'],
        'verbosity': 2,
        'file_dep': ['infra/pyinfra/explore.proxmox.json', PROVISION_SCRIPT],
        'targets': [PROVISION_OUTPUT],
    }

@create_after('provision')
def task_postprovision():
    """🔎 Validate provisioned VMs and save summary"""
    return {
        'actions': [f'python {POSTPROVISION_SCRIPT}'],
        'verbosity': 2,
        'file_dep': ['infra/pyinfra/explore.proxmox.json', POSTPROVISION_SCRIPT],
        'targets': [POSTPROVISION_OUTPUT],
    }
