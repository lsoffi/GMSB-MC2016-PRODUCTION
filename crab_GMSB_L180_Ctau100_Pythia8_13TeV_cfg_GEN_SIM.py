from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'GMSB_L180_Ctau100_Pythia8_13TeV_cff_py_GEN_SIM_1810'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'PrivateMC'
#config.JobType.generator = 'lhe'
config.JobType.psetName = 'GMSB_L180_Ctau100_Pythia8_13TeV_cff_py_GEN_SIM.py'

config.Data.outputPrimaryDataset = 'GMSB_L180_Ctau100_Pythia8_13TeV_cff_py_GEN_SIM_1810'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 500
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/soffi/' # or '/store/group/<subdir>'
config.Data.publication = True
config.Data.publishDBS = 'phys03'
config.Data.outputDatasetTag = 'GMSB_L180_Ctau100_Pythia8_13TeV_cff_py_GEN_SIM_1810'

#config.Site.blacklist = ["T2_US_UCSD"]
#config.Site.whitelist = ['T2_CH_CERN']
config.Site.storageSite = 'T2_IT_Rome'

