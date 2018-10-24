# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# THIS FILE IS MANAGED BY THE GLOBAL REQUIREMENTS REPO - DO NOT EDIT
import setuptools

# In python < 2.7.4, a lazy loading of package `pbr` will break
# setuptools if some other modules registered functions in `atexit`.
# solution from: http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing  # noqa
except ImportError:
    pass

setuptools.setup(
    name="aci-integration-module",
    version="0.14.3",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*",
                                               "tests.*", "tests"]),
    author="Cisco Systems, Inc.",
    author_email="apicapi@noironetworks.com",
    url="http://github.com/noironetworks/aci-integration-module/",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description="Integration Module for ACI.",
    entry_points = {
      'console_scripts': [
         'aimctl = aim.tools.services.cli:aimctl',
         'aimdebug = aim.tools.services.cli:aimdebug',
         'aim-aid = aim.tools.services.aid:aid',
         'aim-event-service-polling = aim.tools.services.aid:event_polling',
         'aim-event-service-rpc = aim.tools.services.aid:rpc',
         'aim-http-server = aim.tools.services.cherrypy_server:http_server']})
