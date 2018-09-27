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

COMMENT='# autocomplete for dlsctl application'

if [ ! -f ~/.bashrc ]; then
    touch ~/.bashrc
fi

if grep -q "_DLSCTL_COMPLETE" ~/.bashrc; then
    echo 'Autocompletion for dlsctl application has been already set up.'
    exit 1
fi

FILE=$(realpath dlsctl)

echo -e '\n' >> ~/.bashrc
echo '# autocomplete for dlsctl application' >> ~/.bashrc
echo 'eval "$(_DLSCTL_COMPLETE=source '${FILE}')"' >> ~/.bashrc