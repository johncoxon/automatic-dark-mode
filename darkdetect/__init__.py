#-----------------------------------------------------------------------------
#  Copyright (C) 2019 Alberto Sottile
#
#  Distributed under the terms of the 3-clause BSD License.
#-----------------------------------------------------------------------------

__version__ = '0.1.1'

import sys
import platform

if sys.platform != "darwin":
    from ._dummy import *
else:
    if int(platform.mac_ver()[0].split(".")[1]) < 14:
        from ._dummy import *
    else:
        from ._detect import *

del sys, platform