from GN0.alpha_zero_general.NeuralNet import NeuralNet
from GN0.models import get_pre_defined
import os
import sys
import time

class NNetWrapper(NeuralNet):
    def __init__(self,game):
