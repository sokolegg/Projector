import unittest
import subprocess
import random
import os
import time

class TestProjector(unittest.TestCase):

	def setUp(self):
		self.empty_project = str(random.randint(0, 1e6))
		os.mkdir(self.empty_project)

	def test_build(self):
		subprocess.call(["cd", self.empty_project, "&&", "projector", "build"], shell=True)
		self.assertTrue(os.path.exists(self.empty_project + '/' + '.projector'))
		self.assertTrue(os.path.exists(self.empty_project + '/' + 'PROJECTFILE'))

	def test_run_ubuntu(self):
		subprocess.run(f"pkill nautilus".split())
		time.sleep(1)
		subprocess.run(f"cd {self.empty_project} && projector build test_open_folder".split(), shell=True)
		subprocess.run(f"cd {self.empty_project} && projector run".split(), shell=True)
		result = subprocess.run([f"pidof nautilus"])
		self.assertTrue(int(result.stdout) > 0)

if __name__ == '__main__':
    unittest.main()