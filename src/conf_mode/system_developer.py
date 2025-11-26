#!/usr/bin/env python3
#
# Copyright VyOS maintainers and contributors <maintainers@vyos.io>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 or later as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import re
import sys
import copy

from vyos.config import Config
from vyos import ConfigError
from vyos import airbag
airbag.enable()

default_config_data = {
    'developer': 'vyos',
}

def get_config(config=None):
    if config:
        conf = config
    else:
        conf = Config()

    developer_config = copy.deepcopy(default_config_data)

    developer_config['developer'] = conf.return_value(['system', 'developer'])

    if not developer_config['developer']:
        developer_config['developer'] = default_config_data['developer']

    return developer_config


def verify(developer_config):
    if developer_config is None:
        return None

    # pattern $VAR(@) "^[[:alnum:]][-.[:alnum:]]*[[:alnum:]]$" ; "invalid host name $VAR(@)"
    developer_regex = re.compile("^[A-Za-z0-9][-.A-Za-z0-9]*[A-Za-z0-9]$")
    if not developer_regex.match(developer_config['developer']):
        raise ConfigError('Invalid developer name ' + developer_config["developer"])

    # pattern $VAR(@) "^.{1,63}$" ; "invalid host-name length"
    length = len(developer_config['developer'])
    if length < 1 or length > 63:
        raise ConfigError(
            'Invalid developer name length, must be less than 63 characters')

    return None


def apply(developer_config):
    if developer_config is None:
        return None

    # For now, we'll just print the developer name
    print(f"Developer name set to: {developer_config['developer']}")

    return None


if __name__ == '__main__':
    try:
        c = get_config()
        verify(c)
        apply(c)
    except ConfigError as e:
        print(e)
        sys.exit(1)
