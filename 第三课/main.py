import pytest
import os

if __name__ == '__main__':
    print(__file__)
    default_folder = os.path.dirname(__file__)
    print(default_folder)
    pytest.main(['-vvs', default_folder])