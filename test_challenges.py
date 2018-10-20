import pytest
from median_challenge import Median
from mouse_challenge import Mouse

class TestChallenges(object):

    def test_median_00(self):
        """Open test file and compare rows"""
        idx = 0
        with open('files/median/output00.txt') as median_file:
            rows = [float(x.rstrip('\n')) for x in median_file.readlines()]  # Strip out return and convert string into number
            for result in Median().gen_median('files/median/input00.txt'):
                assert result == rows[idx]
                idx += 1

    def test_median_01(self):
        """Open test file and compare rows"""
        idx = 0
        with open('files/median/output01.txt') as median_file:
            rows = [float(x.rstrip('\n')) for x in median_file.readlines()]  # Strip out return and convert string into number
            for result in Median().gen_median('files/median/input01.txt'):
                assert result == rows[idx]
                idx += 1

    def test_median_02(self):
        """Open test file and compare rows"""
        idx = 0
        with open('files/median/output02.txt') as median_file:
            rows = [float(x.rstrip('\n')) for x in median_file.readlines()]  # Strip out return and convert string into number
            for result in Median().gen_median('files/median/input02.txt'):
                assert result == rows[idx]
                idx += 1

    def test_median_03(self):
        """Open test file and compare rows"""
        idx = 0
        with open('files/median/output03.txt') as median_file:
            rows = [float(x.rstrip('\n')) for x in median_file.readlines()]  # Strip out return and convert string into number
            for result in Median().gen_median('files/median/input03.txt'):
                assert result == rows[idx]
                idx += 1

    def test_median_04(self):
        """Open test file and compare rows"""
        idx = 0
        with open('files/median/output04.txt') as median_file:
            rows = [float(x.rstrip('\n')) for x in median_file.readlines()]  # Strip out return and convert string into number
            for result in Median().gen_median('files/median/input04.txt'):
                assert result == rows[idx]
                idx += 1

    def test_mouse_00(self):
        """Open test file and compare rows"""
        idx = 0
        with open('files/mouse/output00.txt') as median_file:
            rows = [x.rstrip('\n') for x in median_file.readlines()]  # Strip out return
            for result in Mouse().gen_mouse('files/mouse/input00.txt'):
                assert result == rows[idx]
                idx += 1

    def test_mouse_01(self):
        """Open test file and compare rows"""
        idx = 0
        with open('files/mouse/output01.txt') as median_file:
            rows = [x.rstrip('\n') for x in median_file.readlines()]  # Strip out return and convert string into number
            for result in Mouse().gen_mouse('files/mouse/input01.txt'):
                if result != rows[idx]:
                    assert False
                idx += 1
