import unittest
import subprocess
import random
import os

class TestProjector(unittest.TestCase):

	def setUp(self):
		self.empty_project = str(random.randint(0, 1e6))
		os.mkdir(self.empty_project)

	def test_build(self):
		subprocess.run([f"cd {self.empty_project} && projector build"])
		self.assertTrue(os.path.exists(self.empty_project + '/' + '.projector'))
		self.assertTrue(os.path.exists(self.empty_project + '/' + 'PROJECTFILE'))

if __name__ == '__main__':
    unittest.main()