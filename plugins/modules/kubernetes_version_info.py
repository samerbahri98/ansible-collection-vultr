#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
module: kubernetes_version_info
short_description: Gather information about the Vultr Kubernetes versions
description:
  - Gather information about versions available to deploy Kubernetes clusters.
version_added: "1.0.0"
author:
  - Samer Bahri (@samerbahri98)
  - "René Moser (@resmo)"
extends_documentation_fragment:
  - vultr.cloud.vultr_v2
"""

EXAMPLES = """
- name: Gather Vultr Kubernetes Versions information
  vultr.cloud.kubernetes_version_info:
  register: result

- name: Print the gathered information
  ansible.builtin.debug:
    var: result.vultr_kubernetes_versions
"""

RETURN = """
---
vultr_api:
  description: Response from Vultr API with a few additions/modification.
  returned: success
  type: dict
  contains:
    api_timeout:
      description: Timeout used for the API requests.
      returned: success
      type: int
      sample: 60
    api_retries:
      description: Amount of max retries for the API requests.
      returned: success
      type: int
      sample: 5
    api_retry_max_delay:
      description: Exponential backoff delay in seconds between retries up to this max delay value.
      returned: success
      type: int
      sample: 12
    api_endpoint:
      description: Endpoint used for the API requests.
      returned: success
      type: str
      sample: "https://api.vultr.com/v2"
vultr_kubernetes_versions:
  description: Response from Vultr API as list.
  returned: success
  type: list[str]
"""

from ansible.module_utils.basic import AnsibleModule

from ..module_utils.vultr_v2 import AnsibleVultr, vultr_argument_spec


def main():
    argument_spec = vultr_argument_spec()

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    vultr = AnsibleVultr(
        module=module,
        namespace="vultr_kubernetes_versions",
        resource_path="/kubernetes/versions",
        ressource_result_key_singular="version",
    )

    vultr.get_result(vultr.query_list())


if __name__ == "__main__":
    main()
