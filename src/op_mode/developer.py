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
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys

import vyos.opmode
from vyos.config import Config

def _get_raw_data():
    conf = Config()
    developer_name = conf.return_value(['system', 'developer'])
    if not developer_name:
        developer_name = 'vyos'
    return {'developer': developer_name}

def _get_formatted_output(data):
    return f"Developer: {data['developer']}"

def show(raw: bool):
    developer_data = _get_raw_data()

    if raw:
        return developer_data
    else:
        return _get_formatted_output(developer_data)

if __name__ == '__main__':
    try:
        res = vyos.opmode.run(sys.modules[__name__])
        if res:
            print(res)
    except (ValueError, vyos.opmode.Error) as e:
        print(e)
        sys.exit(1)
