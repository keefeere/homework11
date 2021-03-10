import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_is_nomad_installed(host):
    assert host.file("/usr/bin/nomad").exists
    assert host.file("/usr/bin/nomad").mode == 0o755
    assert host.file("/usr/bin/nomad").user == "nomad"

def test_is_nomad_executable(host):
    hello_world_run = host.run("/usr/bin/nomad status")
    assert 'No running jobs' in hello_world_run.stdout
