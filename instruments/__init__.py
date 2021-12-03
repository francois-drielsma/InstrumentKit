#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines globally-available subpackages and symbols for the instruments package.
"""

# IMPORTS ####################################################################

__all__ = ["units"]


from . import abstract_instruments
from .abstract_instruments import Instrument

from . import agilent
from . import generic_scpi
from . import fluke
from . import gentec_eo
from . import glassman
from . import holzworth
from . import hp
from . import keithley
from . import lakeshore
from . import minghe
from . import newport
from . import oxford
from . import phasematrix
from . import picowatt
from . import qubitekk
from . import rigol
from . import srs
from . import tektronix
from . import teledyne
from . import thorlabs
from . import toptica
from . import yokogawa

from .config import load_instruments
from .units import ureg as units

# VERSION METADATA ###########################################################
# In keeping with PEP-396, we define a version number of the form
# {major}.{minor}[.{postrelease}]{prerelease-tag}

__version__ = "0.6.0"

__title__ = "instrumentkit"
__description__ = "Test and measurement communication library"
__uri__ = "https://instrumentkit.readthedocs.org/"

__author__ = "Steven Casagrande"
__email__ = "scasagrande@galvant.ca"

__license__ = "AGPLv3"
__copyright__ = "Copyright (c) 2012-2020 Steven Casagrande"
