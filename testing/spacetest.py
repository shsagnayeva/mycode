#!/usr/bin/python3

import issspace
import pytest

def test_astros():
    with pytest.raises(RuntimeError) as slappysquirrel:
        issspace.astros()

    assert "Network access not allowed" in str(slappysquirrel.value)

