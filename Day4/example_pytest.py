"""Example for pytest usage"""
import pytest

def method1(x):
    return x+3

def test_method():
    print('hi')

method1(2)
test_method()