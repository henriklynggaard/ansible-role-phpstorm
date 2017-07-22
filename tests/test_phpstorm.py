import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


desktop_file_location = "/root/.local/share/applications/phpstorm-2017.2.desktop"


def test_desktop_file_exists(File):
    f = File(desktop_file_location)

    assert f.exists
    assert f.is_file


def test_desktop_file_contains_fullpath(File):
    f = File(desktop_file_location)

    assert f.contains("/root/Tools/phpstorm-2017.2/bin/phpstorm.png")
    assert f.contains("/root/Tools/phpstorm-2017.2/bin/phpstorm.sh")


def test_desktop_file_contains_right_name(File):
    f = File(desktop_file_location)

    assert f.contains("PhpStorm 2017.2")


def test_start_file_exists(File):
    f = File('/root/Tools/phpstorm-2017.2/bin/phpstorm.sh')

    assert f.exists
    assert f.is_file
