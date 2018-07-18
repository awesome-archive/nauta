#
# INTEL CONFIDENTIAL
# Copyright (c) 2018 Intel Corporation
#
# The source code contained or described herein and all documents related to
# the source code ("Material") are owned by Intel Corporation or its suppliers
# or licensors. Title to the Material remains with Intel Corporation or its
# suppliers and licensors. The Material contains trade secrets and proprietary
# and confidential information of Intel or its suppliers and licensors. The
# Material is protected by worldwide copyright and trade secret laws and treaty
# provisions. No part of the Material may be used, copied, reproduced, modified,
# published, uploaded, posted, transmitted, distributed, or disclosed in any way
# without Intel's prior express written permission.
#
# No license under any patent, copyright, trade secret or other intellectual
# property right is granted to or conferred upon you by disclosure or delivery
# of the Materials, either expressly, by implication, inducement, estoppel or
# otherwise. Any license under such intellectual property rights must be express
# and approved by Intel in writing.
#

import click
from tabulate import tabulate

from util.aliascmd import AliasCmd
from cli_state import common_options
from version import VERSION
from util.config import DLS4EConfigMap

HELP = "Displays the version of the installed dlsctl application."


@click.command(short_help=HELP, cls=AliasCmd, alias='v')
@common_options(verify_dependencies=False, verify_config_path=False)
def version():
    """
    Returns the version of the installed dlsctl application.
    """
    version_table = [["dlsctl application", VERSION],
                     ["dls4e platform", DLS4EConfigMap().platform_version]]

    click.echo(tabulate(version_table,
                        headers=['Component', 'Version'],
                        tablefmt="orgtbl"))
