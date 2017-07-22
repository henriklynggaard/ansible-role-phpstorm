PhpStorm (https://www.jetbrains.com/phpstorm)
=========

This role installs PhpStorm and configured plugins. It has been tested on Linux Mint 18 but should work on most 
distributions. By default it installs PhphStorm 2017.2 and no additional plugins

By default PhphStorm is installed under the user's home directory and _become_ is not needed.

Requirements
------------

None


Role Variables
--------------

    phpstorm_version: 2017.2
    phpstorm_download_mirror: https://download.jetbrains.com/webide/
    phpstorm_plugin_download_mirror: "https://plugins.jetbrains.com/plugin/download?updateId="
    phpstorm_plugins: []
    phpstorm_download_directory: /tmp
    phpstorm_user_dir: "~{{ (phpstorm_install_user is defined) | ternary(phpstorm_install_user, ansible_user_id) }}"
    phpstorm_install_directory: "{{ phpstorm_user_dir | expanduser }}/Tools"
    phpstorm_install_user: <undefined>

    # calculated
    phpstorm_install_file: "PhpStorm-{{ phpstorm_version }}.tar.gz"
    phpstorm_download_url: "{{ phpstorm_download_mirror }}{{ phpstorm_install_file }}"
    phpstorm_location: "{{ phpstorm_install_directory }}/phpstorm-{{ phpstorm_version }}"
    phpstorm_desktop_file_location: "{{ phpstorm_user_dir | expanduser  }}/.local/share/applications/phpstorm-{{ phpstorm_version }}.desktop"

* phpstorm_plugins is a list of names which get appended to phpstorm_plugin_download_mirror to form a full download  
* Defining phpstorm_install_user allows the role to install under a different user, however become is required

Dependencies
------------

None

Example 
-------

__Example playbook__


    - hosts: localhost
      connection: local
    
    roles:
      - henriklyngaard.phpstorm
      
__Exmaple inventory for plugins__

The below IDs have been found by going to https://plugins.jetbrains.com/phpstorm and searching for the plugin. 
Once found copy the link location for the desired version and use the _updateId=XXXXX_ part at the end        
      
    phpstorm_plugins:
      # ignore 1.7.6
      - 32828
      # bash support 1.6.5.171
      - 31610
      # ansible 0.9.4
      - 27616
      # docker 2.5.3
      - 33621
      # markdown 2017.1.20170302
      - 33092      
      
 Alternatively upload the required plugins to a webserver and adjust _phpstorm_plugin_download_mirror_ and 
 _phpstorm_plugins_ accordingly
      
      
License
-------

MIT

Change log
----------

* 1.1: Allow installation under another user
* 1.0: Initial version
