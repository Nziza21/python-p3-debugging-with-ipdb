#!/usr/bin/env python3

from ipdb_debugging import plus_two

class TestIpdbDebugging:
    '''ipdb_debugging.py'''
    
    def test_adds_two(self):
        '''adds_two() adds 2 to input arg and returns sum.'''
        result = plus_two(3)
        print(f"Result: {result}")
        assert result == 5

