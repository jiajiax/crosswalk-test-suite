#!/usr/bin/env python
#
# Copyright (c) 2015 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Hongjuan, Wang<hongjuanx.wang@intel.com>

import unittest
import os
import sys
import commands
import comm


class TestPackertoolsFunctions(unittest.TestCase):

    def test_projectonly1(self):
        comm.setUp()
        os.chdir(comm.ConstPath + "/res")
        cmd = "python %smake_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=./manifest.json --project-only" % \
            (comm.Pck_Tools, comm.ARCH, comm.MODE)
        packstatus = commands.getstatusoutput(cmd)
        errormsg = "--project-only must be used with --project-dir"
        self.assertNotEqual(packstatus[0], 0)
        self.assertIn(errormsg, packstatus[1])

    def test_projectonly2(self):
        comm.setUp()
        cmd = "python %smake_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=./manifest.json --project-only --project-dir=example" % \
            (comm.Pck_Tools, comm.ARCH, comm.MODE)
        packstatus = commands.getstatusoutput(cmd)
        self.assertEqual(packstatus[0], 0)
        result = os.listdir(comm.ConstPath + "/res")
        self.assertNotIn("Example.apk", result)
        self.assertIn("example", result)
        if os.path.exists(comm.ConstPath + "/res/example"):
            try:
                shutil.rmtree(comm.ConstPath + "/res/example")
            except Exception as e:
                os.system("rm -rf " + comm.ConstPath + "/res/example")

if __name__ == '__main__':
    unittest.main()
