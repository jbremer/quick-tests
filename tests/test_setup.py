# Copyright (C) 2017 Jurriaan Bremer.

import os
import tempfile
import yara

def test_yara():
    fd, filepath = tempfile.mkstemp()
    os.write(fd, "VMXh")
    os.close(fd)

    r = yara.compile("qt/vmdetect.yar")
    m, = r.match(filepath)
    assert m.rule == "vmdetect"
