# This file is part of Buildbot.  Buildbot is free software: you can
# redistribute it and/or modify it under the terms of the GNU General Public
# License as published by the Free Software Foundation, version 2.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#
# Copyright Buildbot Team Members

import sys
import os

# apply the same patches the buildmaster does when it starts
from buildbot import monkeypatches
monkeypatches.patch_all(for_tests=True)

# import mock so we bail out early if it's not installed
try:
    import mock
    mock = mock
except ImportError:
    print >>sys.stderr, ("\nBuildbot tests require the 'mock' module; "
                         "try 'pip install mock'")
    os._exit(1)

if map(int, mock.__version__.split('.')[:2]) < [0, 8]:
    print >>sys.stderr, ("\nBuildbot tests require mock version 0.8.0 or "
                         "higher; try 'pip install -U mock'")
    os._exit(1)
