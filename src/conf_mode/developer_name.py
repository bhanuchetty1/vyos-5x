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

from vyos.config import Config
from vyos import airbag

airbag.enable()

def get_config(config=None):
    if config:
        conf = config
    else:
        conf = Config()
    return conf.get_config_dict(['system', 'developer'])

def verify(config):
    pass

def generate(config):
    pass

def apply(config):
    pass

if __name__ == '__main__':
    try:
        c = get_config()
        if c is None:
            exit(0)
        verify(c)
        generate(c)
        apply(c)
    except Exception as e:
        print(e)
        exit(1)
