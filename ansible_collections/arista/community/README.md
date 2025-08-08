<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# arista.community - Community-driven collection of Arista plugins

## Description

Various Arista related Ansible plugins maintained by the community.

Some of these plugins were previously part of the `arista.avd` collection,
but got removed there, when they were no longer used/maintained there.

Everything can be used as-is, without any warranty and with best-effort problem resolution via [GitHub issues](https://github.com/arista-netdevops-community/ansible-community-collection/issues).

## Installation

Install the collection

```shell
ansible-galaxy collection install arista.community
```

Note that if you install the collection from Ansible Galaxy, it will not be upgraded automatically when you upgrade the Ansible package.

To upgrade the collection to the latest available version, run the following command:

```shell
ansible-galaxy collection install arista.community --upgrade
```

See [using Ansible collections](https://docs.ansible.com/ansible/devel/collections_guide/index.html) for more details.

### Additional Python Dependencies

The collection requires the installation of additional Python packages. To ensure you install the correct versions, run the following commands:

```shell
export ARISTA_AVD_DIR=$(ansible-galaxy collection list arista.community --format yaml | head -1 | cut -d: -f1)
pip3 install -r ${ARISTA_AVD_DIR}/arista/community/requirements.txt
```

### Enable Jinja2 Extensions

In your `ansible.cfg` file, add the following modifications:

```ini
[defaults]
jinja2_extensions=jinja2.ext.loopcontrols,jinja2.ext.do
duplicate_dict_key=error
```

### Testing

Every pull request is thoroughly tested by our extensive CI pipeline and reviewed by the AVD Maintainer team.

## Contributing

Contributing pull requests are gladly welcomed for this repository. If you are planning a significant change, please start a discussion first to ensure we can merge it. Please see [contribution guide](https://github.com/arista-netdevops-community/ansible-community-collection/CONTRIBUTE.md) for additional details.

You can also open an [issue](https://github.com/arista-netdevops-community/ansible-community-collection/issues) to report any problems or submit requests for enhancements.

## Support

- This is an open-source project maintained by the community around and within Arista. Everything can be used as-is, without any warranty and with best-effort problem resolution via [GitHub issues](https://github.com/arista-netdevops-community/ansible-community-collection/issues).

## License Information

Copyright (c) 2025 Arista Networks, Inc.

The project is published under [Apache 2.0 License](https://github.com/arista-netdevops-community/ansible-community-collection/blob/main/ansible_collections/arista/avd/LICENSE)
