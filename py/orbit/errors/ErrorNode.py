"""
Module. Includes classes for error accelerator nodes.
"""

import sys
import os
import math

# import the function that finalizes the execution
from orbit.utils import orbitFinalize

# import physical constants
from orbit.utils import consts

# import general accelerator elements and lattice
from orbit.lattice import AccLattice, AccNode,\
     AccActionsContainer, AccNodeBunchTracker

# import teapot drift class
from orbit.teapot import DriftTEAPOT

#import error packages
from error_base import drifti
from error_base import CoordDisplacement
from error_base import QuadKicker
from error_base import QuadKickerOsc
from error_base import DipoleKickerOsc
from error_base import LongDisplacement
from error_base import StraightRotationXY
from error_base import StraightRotationXSI
from error_base import StraightRotationXSF
from error_base import StraightRotationYSI
from error_base import StraightRotationYSF
from error_base import BendFieldI
from error_base import BendFieldF
from error_base import BendDisplacementXI
from error_base import BendDisplacementXF
from error_base import BendDisplacementYI
from error_base import BendDisplacementYF
from error_base import BendDisplacementLI
from error_base import BendDisplacementLF
from error_base import RotationI
from error_base import RotationF
from error_base import derf
from error_base import root_normal
from error_base import getGauss


# Displace the coordinates of a bunch
class CoordDisplacement(DriftTEAPOT):

    def __init__(self, dx, dxp, dy, dyp, dz, dE,\
	    name = "Coordinate Displacement"):
        """
            Constructor. Creates CoordDisplacement element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("coordinate displacement node")
        self.setLength(0.0)
        self.dx  = dx
        self.dxp = dxp
        self.dy  = dy
        self.dyp = dyp
        self.dz  = dz
        self.dE  = dE

    def trackBunch(self, bunch):
        """
            The CoordDisplacement-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        dx  = self.dx
        dxp = self.dxp
        dy  = self.dy
        dyp = self.dyp
        dz  = self.dz
        dE  = self.dE
        CoordDisplacement(bunch, dx, dxp, dy, dyp, dz, dE)

    def track(self, paramsDict):
        """ 
            The CoordDisplacement-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        dx  = self.dx
        dxp = self.dxp
        dy  = self.dy
        dyp = self.dyp
        dz  = self.dz
        dE  = self.dE
        CoordDisplacement(bunch, dx, dxp, dy, dyp, dz, dE)


# Quadrupole kick a bunch
class QuadKicker(DriftTEAPOT):

    def __init__(self, k,\
	    name = "Quad Kicker"):
        """
            Constructor. Creates QuadKicker element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("quadrupole kicker node")
        self.setLength(0.0)
        self.k = k

    def trackBunch(self, bunch):
        """
            The QuadKicker-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        k = self.k
        QuadKicker(bunch, k)

    def track(self, paramsDict):
        """ 
            The QuadKicker-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        k = self.k
        QuadKicker(bunch, k)


# Oscillating quadrupole kick a bunch
class QuadKickerOsc(DriftTEAPOT):

    def __init__(self, k, phaselength, phase,\
	    name = "Quad Kicker Osc"):
        """
            Constructor. Creates QuadKickerOsc element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("oscillating quadrupole kicker node")
        self.setLength(0.0)
        self.k = k
        self.phaselength = phaselength
        self.phase = phase

    def trackBunch(self, bunch):
        """
            The QuadKickerOsc-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        k = self.k
        phaselength = self.phaselength
        phase = self.phase
        QuadKickerOsc(bunch, k, phaselength, phase)

    def track(self, paramsDict):
        """ 
            The QuadKickerOsc-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        k = self.k
        phaselength = self.phaselength
        phase = self.phase
        QuadKickerOsc(bunch, k, phaselength, phase)


# Oscillating dipole kick a bunch
class DipoleKickerOsc(DriftTEAPOT):

    def __init__(self, k, phaselength, phase,\
	    name = "Dipole Kicker Osc"):
        """
            Constructor. Creates DipoleKickerOsc element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("oscillating dipole kicker node")
        self.setLength(0.0)
        self.k = k
        self.phaselength = phaselength
        self.phase = phase

    def trackBunch(self, bunch):
        """
            The DipoleKickerOsc-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        k = self.k
        phaselength = self.phaselength
        phase = self.phase
        DipoleKickerOsc(bunch, k, phaselength, phase)

    def track(self, paramsDict):
        """ 
            The DipoleKickerOsc-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        k = self.k
        phaselength = self.phaselength
        phase = self.phase
        DipoleKickerOsc(bunch, k, phaselength, phase)


# Longitudinally displace a bunch
class LongDisplacement(DriftTEAPOT):

    def __init__(self, ds,\
	    name = "Longitudinal Displacement"):
        """
            Constructor. Creates LongDisplacement element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("longitudinal displacement node")
        self.setLength(0.0)
        self.ds = ds

    def trackBunch(self, bunch):
        """
            The LongDisplacement-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        ds = self.ds
        LongDisplacement(bunch, ds)

    def track(self, paramsDict):
        """ 
            The LongDisplacement-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        ds = self.ds
        LongDisplacement(bunch, ds)


# XY rotate a bunch
class StraightRotationXY(DriftTEAPOT):

    def __init__(self, anglexy,\
	    name = "XY Rotation"):
        """
            Constructor. Creates StraightRotationXY element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("xy rotation node")
        self.setLength(0.0)
        self.anglexy = anglexy

    def trackBunch(self, bunch):
        """
            The StraightRotationXY-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        anglexy = self.anglexy
        LongDisplacement(bunch, anglexy)

    def track(self, paramsDict):
        """ 
            The StraightRotationXY-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        anglexy = self.anglexy
        LongDisplacement(bunch, anglexy)


# XS rotate a bunch entering element
class StraightRotationXSI(DriftTEAPOT):

    def __init__(self, anglexsi, lengthelt,\
	    name = "XSI Rotation"):
        """
            Constructor. Creates StraightRotationXSI element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("xsi rotation node")
        self.setLength(0.0)
        self.anglexsi = anglexsi
        self.lengthelt = lengthelt

    def trackBunch(self, bunch):
        """
            The StraightRotationXSI-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        anglexsi = self.anglexsi
        lengthelt = self.lengthelt
        StraightRotationXSI(bunch, anglexsi, lengthelt)

    def track(self, paramsDict):
        """ 
            The StraightRotationXSI-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        anglexsi = self.anglexsi
        lengthelt = self.lengthelt
        StraightRotationXSI(bunch, anglexsi, lengthelt)


# XS rotate a bunch leaving element
class StraightRotationXSF(DriftTEAPOT):

    def __init__(self, anglexsf, lengthelt,\
	    name = "XSF Rotation"):
        """
            Constructor. Creates StraightRotationXSF element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("xsf rotation node")
        self.setLength(0.0)
        self.anglexsf = anglexsf
        self.lengthelt = lengthelt

    def trackBunch(self, bunch):
        """
            The StraightRotationXSF-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        anglexsf = self.anglexsf
        lengthelt = self.lengthelt
        StraightRotationXSF(bunch, anglexsf, lengthelt)

    def track(self, paramsDict):
        """ 
            The StraightRotationXSF-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        anglexsf = self.anglexsf
        lengthelt = self.lengthelt
        StraightRotationXSF(bunch, anglexsf, lengthelt)


# YS rotate a bunch entering element
class StraightRotationYSI(DriftTEAPOT):

    def __init__(self, angleysi, lengthelt,\
	    name = "YSI Rotation"):
        """
            Constructor. Creates StraightRotationYSI element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("ysi rotation node")
        self.setLength(0.0)
        self.angleysi = angleysi
        self.lengthelt = lengthelt

    def trackBunch(self, bunch):
        """
            The StraightRotationYSI-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        angleysi = self.angleysi
        lengthelt = self.lengthelt
        StraightRotationYSI(bunch, angleysi, lengthelt)

    def track(self, paramsDict):
        """ 
            The StraightRotationYSI-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        angleysi = self.angleysi
        lengthelt = self.lengthelt
        StraightRotationYSI(bunch, angleysi, lengthelt)


# YS rotate a bunch leaving element
class StraightRotationYSF(DriftTEAPOT):

    def __init__(self, angleysf, lengthelt,\
	    name = "YSF Rotation"):
        """
            Constructor. Creates StraightRotationYSF element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("ysf rotation node")
        self.setLength(0.0)
        self.angleysf = angleysf
        self.lengthelt = lengthelt

    def trackBunch(self, bunch):
        """
            The StraightRotationYSF-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        angleysf = self.angleysf
        lengthelt = self.lengthelt
        StraightRotationYSF(bunch, angleysf, lengthelt)

    def track(self, paramsDict):
        """ 
            The StraightRotationYSF-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        angleysf = self.angleysf
        lengthelt = self.lengthelt
        StraightRotationYSF(bunch, angleysf, lengthelt)


# Bend field strength error to a bunch entering element
class BendFieldI(DriftTEAPOT):

    def __init__(self, drho,\
	    name = "BendI Field"):
        """
            Constructor. Creates BendFieldI element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("bendi field node")
        self.setLength(0.0)
        self.drho = drho

    def trackBunch(self, bunch):
        """
            The BendFieldI-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        drho = self.drho
        BendFieldI(bunch, drho)

    def track(self, paramsDict):
        """ 
            The BendFieldI-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        drho = self.drho
        BendFieldI(bunch, drho)


# Bend field strength error to a bunch leaving element
class BendFieldF(DriftTEAPOT):

    def __init__(self, drho,\
	    name = "BendF Field"):
        """
            Constructor. Creates BendFieldF element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("bendf field node")
        self.setLength(0.0)
        self.drho = drho

    def trackBunch(self, bunch):
        """
            The BendFieldF-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        drho = self.drho
        BendFieldF(bunch, drho)

    def track(self, paramsDict):
        """ 
            The BendFieldF-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        drho = self.drho
        BendFieldF(bunch, drho)


# X displacement error to a bunch entering bend
class BendDisplacementXI(DriftTEAPOT):

    def __init__(self, anglexi, disp,\
	    name = "BendXI Displacement"):
        """
            Constructor. Creates BendDisplacementXI element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("xi bend displacement node")
        self.setLength(0.0)
        self.anglexi = anglexi
        self.disp = disp

    def trackBunch(self, bunch):
        """
            The BendDisplacementXI-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        anglexi = self.anglexi
        disp = self.disp
        BendDisplacementXI(bunch, anglexi, disp)

    def track(self, paramsDict):
        """ 
            The BendDisplacementXI-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        anglexi = self.anglexi
        disp = self.disp
        BendDisplacementXI(bunch, anglexi, disp)


# X displacement error to a bunch leaving bend
class BendDisplacementXF(DriftTEAPOT):

    def __init__(self, anglexf, disp,\
	    name = "BendXF Displacement"):
        """
            Constructor. Creates BendDisplacementXF element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("xf bend displacement node")
        self.setLength(0.0)
        self.anglexf = anglexf
        self.disp = disp

    def trackBunch(self, bunch):
        """
            The BendDisplacementXF-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        anglexf = self.anglexf
        disp = self.disp
        BendDisplacementXF(bunch, anglexf, disp)

    def track(self, paramsDict):
        """ 
            The BendDisplacementXF-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        anglexf = self.anglexf
        disp = self.disp
        BendDisplacementXF(bunch, anglexf, disp)


# Y displacement error to a bunch entering bend
class BendDisplacementYI(DriftTEAPOT):

    def __init__(self, disp,\
	    name = "BendYI Displacement"):
        """
            Constructor. Creates BendDisplacementYI element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("yi bend displacement node")
        self.setLength(0.0)
        self.disp = disp

    def trackBunch(self, bunch):
        """
            The BendDisplacementYI-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        disp = self.disp
        BendDisplacementYI(bunch, disp)

    def track(self, paramsDict):
        """ 
            The BendDisplacementYI-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        disp = self.disp
        BendDisplacementYI(bunch, disp)


# Y displacement error to a bunch leaving bend
class BendDisplacementYF(DriftTEAPOT):

    def __init__(self, disp,\
	    name = "BendYF Displacement"):
        """
            Constructor. Creates BendDisplacementYF element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("yf bend displacement node")
        self.setLength(0.0)
        self.disp = disp

    def trackBunch(self, bunch):
        """
            The BendDisplacementYF-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        disp = self.disp
        BendDisplacementYF(bunch, disp)

    def track(self, paramsDict):
        """ 
            The BendDisplacementYF-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        disp = self.disp
        BendDisplacementYF(bunch, disp)


# L displacement error to a bunch entering bend
class BendDisplacementLI(DriftTEAPOT):

    def __init__(self, angleli, disp,\
	    name = "BendLI Displacement"):
        """
            Constructor. Creates BendDisplacementLI element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("li bend displacement node")
        self.setLength(0.0)
        self.angleli = angleli
        self.disp = disp

    def trackBunch(self, bunch):
        """
            The BendDisplacementLI-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        angleli = self.angleli
        disp = self.disp
        BendDisplacementLI(bunch, angleli, disp)

    def track(self, paramsDict):
        """ 
            The BendDisplacementLI-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        angleli = self.angleli
        disp = self.disp
        BendDisplacementLI(bunch, angleli, disp)


# L displacement error to a bunch leaving bend
class BendDisplacementLF(DriftTEAPOT):

    def __init__(self, anglelf, disp,\
	    name = "BendLF Displacement"):
        """
            Constructor. Creates BendDisplacementLF element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("lf bend displacement node")
        self.setLength(0.0)
        self.anglelf = anglelf
        self.disp = disp

    def trackBunch(self, bunch):
        """
            The BendDisplacementLF-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        anglelf = self.anglelf
        disp = self.disp
        BendDisplacementLF(bunch, anglelf, disp)

    def track(self, paramsDict):
        """ 
            The BendDisplacementLF-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        anglelf = self.anglelf
        disp = self.disp
        BendDisplacementLF(bunch, anglelf, disp)


# General rotation error to a bunch entering element
class RotationI(DriftTEAPOT):

    def __init__(self, anglei, rhoi, theta, lengthelt, et, rotype,\
	    name = "RotationI General"):
        """
            Constructor. Creates RotationI element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("generali rotation node")
        self.setLength(0.0)
        self.anglei = anglei
        self.rhoi = rhoi
        self.theta = theta
        self.lengthelt = lengthelt
        self.et = et
        self.rotype = rotype

    def trackBunch(self, bunch):
        """
            The RotationI-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        anglei = self.anglei
        rhoi = self.rhoi
        theta = self.theta
        lengthelt = self.lengthelt
        et = self.et
        rotype = self.rotype
        RotationI(bunch, anglei, rhoi, theta, lengthelt, et, rotype)

    def track(self, paramsDict):
        """ 
            The RotationI-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        anglei = self.anglei
        rhoi = self.rhoi
        theta = self.theta
        lengthelt = self.lengthelt
        et = self.et
        rotype = self.rotype
        RotationI(bunch, anglei, rhoi, theta, lengthelt, et, rotype)


# General rotation error to a bunch leaving element
class RotationF(DriftTEAPOT):

    def __init__(self, anglef, rhoi, theta, lengthelt, et, rotype,\
	    name = "RotationF General"):
        """
            Constructor. Creates RotationF element.
        """
        DriftTEAPOT.__init__(self, name)
        self.setType("generalf rotation node")
        self.setLength(0.0)
        self.anglef = anglef
        self.rhoi = rhoi
        self.theta = theta
        self.lengthelt = lengthelt
        self.et = et
        self.rotype = rotype

    def trackBunch(self, bunch):
        """
            The RotationF-teapot class implementation of the
            AccNodeBunchTracker class trackBunch(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        anglef = self.anglef
        rhoi = self.rhoi
        theta = self.theta
        lengthelt = self.lengthelt
        et = self.et
        rotype = self.rotype
        RotationF(bunch, anglef, rhoi, theta, lengthelt, et, rotype)

    def track(self, paramsDict):
        """ 
            The RotationF-teapot class implementation of the
            AccNodeBunchTracker class track(probe) method.
        """
        length = self.getLength(self.getActivePartIndex())
        bunch = paramsDict["bunch"]
        anglef = self.anglef
        rhoi = self.rhoi
        theta = self.theta
        lengthelt = self.lengthelt
        et = self.et
        rotype = self.rotype
        RotationF(bunch, anglef, rhoi, theta, lengthelt, et, rotype)
