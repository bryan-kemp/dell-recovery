#!/usr/bin/python
#
# Dell Recovery Media install script
# Copyright (C) 2008, Dell Inc.
#  Author: Mario Limonciello <Mario_Limonciello@Dell.com>
#
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from distutils.core import setup

import subprocess, glob, os.path

setup(
    name="dell-recovery-media",
    author="Mario Limonciello",
    author_email="Mario_Limoncielo@Dell.com",
    maintainer="Mario Limonciello",
    maintainer_email="Mario_Limonciello@Dell.com",
    url="http://linux.dell.com/",
    license="gpl",
    description="Creates a piece of recovery media for a Dell Factory image",
    packages=["Dell"],
    data_files=[("share/dell/glade", glob.glob("Dell/*.glade")),
                ("share/dell/bin", glob.glob("bin/dell-recovery-media")),
                ("share/dell/bin", glob.glob("bin/create-new-uuid")),
                ("share/applications", glob.glob("applications/*.desktop"))],
    scripts=["dell-recovery-media"],
)

