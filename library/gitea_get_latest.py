#!/usr/bin/python

import re
import requests
from bs4 import BeautifulSoup
from packaging import version
from ansible.module_utils.basic import AnsibleModule

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: gitea_get_latest

short_description: return the latest version of gitea
                   parsing the url https://dl.gitea.io/gitea/

version_added: "2.5"

description:
    - "return the latest version of gitea parsing
      the url https://dl.gitea.io/gitea/"

author:
    - Oscar Hermosa (ohermosa@gmail.com)
'''

EXAMPLES = '''
# Get latest version of gitea
- name: "get gitea version"
  gitea_get_latest:
  register: gitea_response

- debug: var=gitea_response.version
'''

RETURN = '''
version:
    description: The latest version of gitea
    type: string
    returned: always
'''


def get_fucking_latest(versions=[]):
    r = re.compile("^[0-9]+\.[0-9]+(\.[0-9])*$")
    stable_versions = list(filter(r.match, versions))
    for n, i in enumerate(stable_versions):
        stable_versions[n] = version.parse(i)
    return max(stable_versions).base_version


def get_latest():
    gitea_url = "https://dl.gitea.io/gitea/"
    gitea_text = requests.get(gitea_url)

    if gitea_text.status_code == 200:
        soup = BeautifulSoup(gitea_text.text, "html.parser")
        versions = []
        for item in soup.findAll("span", class_="name"):
            versions.append(item.text)
        if len(versions) == 0:
            return None
        else:
            return get_fucking_latest(versions)
    else:
        return None


def run_module():
    result = dict(
        changed=False,
        version=str
    )

    module = AnsibleModule(
        argument_spec={},
        supports_check_mode=True
    )

    result['version'] = get_latest()
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
