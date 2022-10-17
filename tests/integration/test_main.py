import os

from importlib.machinery import SourceFileLoader
from importlib.util import spec_from_loader, module_from_spec
from unittest.mock import patch

REL_LOCATION = "../../src/"
ABS_LOCATION = os.path.join(os.path.split(os.path.realpath(__file__))[0], REL_LOCATION)


def run_main(absolute_path, args, env):
    with patch.dict("os.environ", env), patch("sys.argv", args):
        loader = SourceFileLoader("__main__", absolute_path)
        spec = spec_from_loader(loader.name, loader)
        module = module_from_spec(spec)
        loader.exec_module(module)


class Test:
    def setup_class(self):
        self.abs_path = os.path.join(ABS_LOCATION, "api.py")

    def test_main_flow(self):
        env = {"foo": "bar"}
        args = ["api.py", "--name", "Jane Doe"]
        run_main(self.abs_path, args, env)
