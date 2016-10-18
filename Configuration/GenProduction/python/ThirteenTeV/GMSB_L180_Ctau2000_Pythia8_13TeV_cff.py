import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",

    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    SLHAFileForPythia8 = cms.string('Configuration/Generator/data/GMSB_Lambda180_CTau2000.slha'),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
	'Main:timesAllowErrors    = 10000', 
        'ParticleDecays:limitTau0 = on',
	'ParticleDecays:tauMax = 10',
        'Tune:ee 3',
        'Tune:pp 5',
	'SUSY:all on',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters')
 
   )
)

ProductionFilterSequence = cms.Sequence(generator)
