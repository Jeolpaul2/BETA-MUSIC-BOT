#
# Copyright 2021-2022 Jeolpaul2
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# All rights reserved.

import os

from config import autoclean


async def auto_clean(popped):
    try:
        rem = popped["file"]
        autoclean.remove(rem)
        count = autoclean.count(rem)
        if count == 0:
            if (
                "vid_" not in rem
                or "live_" not in rem
                or "index_" not in rem
            ):
                try:
                    os.remove(rem)
                except:
                    pass
    except:
        pass
