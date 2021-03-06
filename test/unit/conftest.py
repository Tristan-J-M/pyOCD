# pyOCD debugger
# Copyright (c) 2016-2020 Arm Limited
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest
import logging

# unittest.mock is available from Python 3.3.
try:
    from unittest import mock
except ImportError:
    import mock

from .mockcore import MockCore

@pytest.fixture(scope='function')
def mockcore():
    return MockCore()

# Ignore semihosting test that currently crashes on Travis
collect_ignore = [
    "test_semihosting.py",
    ]
