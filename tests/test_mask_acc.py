import pytest
from src.functions import mask_acc

def test_mask_acc():
    assert mask_acc('Счет 82781399328834147668') == '**7668'
    assert mask_acc('Счет 90817634362091276762') == '**6762'
