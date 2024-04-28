import pytest
import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# @pytest.fixture()
# def AnsibleDefaults():
#     with open("defaults/main.yml", 'r') as stream:
#         return yaml.safe_load(stream)


@pytest.mark.parametrize("name,version", [
    ("radicale", "any"),
    ("python3", "3"),
])
def test_packages(host, name, version):
    pkg = host.package(name)
    assert pkg.is_installed
    if version != 'any':
        assert pkg.version.startswith(version)


@pytest.mark.parametrize("dirs", [
    "/var/lib/radicale",
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/etc/radicale/users",
    "/etc/radicale/config",
    "/etc/systemd/system/radicale.service",
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_some_command_output(host):
    run = host.run("cat /etc/os-release")
    out = run.stdout+run.stderr
    assert "NAME" in out
