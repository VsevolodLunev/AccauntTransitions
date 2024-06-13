import pytest
from src.functions import mask_cart_number


def test_mask_cart_number():
    assert mask_cart_number('9175985085449563') == '9175 98** **** 9563'
    assert mask_cart_number('9657499677062945') == '9657 49** **** 2945'