import sys
import unittest
from unittest.mock import patch

from surfmap.lib.parameters import get_args


class ShellArgumentTests(unittest.TestCase):
    def test_shell_is_registered_once_as_a_standalone_input(self):
        argv = [
            "surfmap",
            "--shell",
            "example_shell.pdb",
            "-tomap",
            "bfactor",
            "--png",
            "--nosmooth",
            "--keep",
            "--clean-map",
            "-rad",
            "0.5",
            "-s",
            "2",
        ]

        with patch.object(sys, "argv", argv):
            args = get_args()

        self.assertEqual(args.shell, "example_shell.pdb")
        self.assertIsNone(args.pdb)
        self.assertIsNone(args.mat)
        self.assertEqual(args.tomap, "bfactor")


if __name__ == "__main__":
    unittest.main()
