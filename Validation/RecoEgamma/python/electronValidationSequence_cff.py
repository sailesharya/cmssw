import FWCore.ParameterSet.Config as cms

from Validation.RecoEgamma.electronIsoFromDeps_cff import *
from Validation.RecoEgamma.ElectronMcSignalValidator_cfi import *
from Validation.RecoEgamma.ElectronMcFakeValidator_cfi import *

electronValidationSequence = cms.Sequence(electronIsoFromDeps+electronMcSignalValidator+electronMcFakeValidator)

