import unittest
import subprocess
import random
import os
import time
import projector

class TestProjector(unittest.TestCase):

	projector = "../env/bin/projector"

	def setUp(self):
		self.empty_project = str(random.randint(0, 1e6))
		os.mkdir(self.empty_project)

	def test_build(self):
		subprocess.call(["cd", self.empty_project, "&&", self.projector, "build"], shell=True)
		self.assertTrue(os.path.exists(self.empty_project + '/' + '.projector'))
		self.assertTrue(os.path.exists(self.empty_project + '/' + 'PROJECTFILE'))

	def test_run_ubuntu(self):
		subprocess.run(f"pkill nautilus".split())
		time.sleep(1)
		subprocess.call(f"cd {self.empty_project} && {self.projector} build test_open_folder".split(), shell=True)
		subprocess.call(f"cd {self.empty_project} && {self.projector} run".split(), shell=True)
		result = subprocess.call([f"pidof nautilus"], shell=True)
		print(result)
		self.assertTrue(result > 0)


if __name__ == '__main__':
	unittest.main()