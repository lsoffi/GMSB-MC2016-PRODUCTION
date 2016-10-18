# GMSB-MC2016-PRODUCTION
************************************************************************************************
                                                    RELEASE CMSSW_7_1_25_patch1
************************************************************************************************

scram project -n CMSSW7-1-25-GMSBstep1 CMSSW CMSSW_7_1_25_patch1
cd CMSSW7-1-25-GMSBstep1/src/
cmsenv

curl -s https://raw.githubusercontent.com/cms-sw/genproductions/master/python/ThirteenTeV/GMSB_L180_Ctau100_Pythia8_13TeV_cff.py --retry 2 --create-dirs -o Configuration/GenProduction/python/ThirteenTeV/GMSB_L180_Ctau100_Pythia8_13TeV_cff.py

curl -s https://raw.githubusercontent.com/cms-sw/genproductions/eb45213db83babe397f28221eafef9c57d0fc785/python/ThirteenTeV/Hadronizer_TuneCUETP8M1_13TeV_generic_LHE_pythia8_cff.py --retry 2 Configuration/GenProduction/python/

---> merge to fragments

curl -s https://raw.githubusercontent.com/cms-cvs-history/Configuration-Generator/master/data/GMSB_Lambda180_CTau100_7TeV_pythia6.slha --retry 2 --create-dirs -o Configuration/Generator/data/GMSB_L180_Ctau100_Pythia8_13TeV.slha

mv Configuration/Generator/data/GMSB_L180_Ctau100_Pythia8_13TeV.slha  Configuration/Generator/data/GMSB_Lambda180_CTau100.slha

scram b

**************************************************************************************
                                                             TEST
**************************************************************************************
Test the py fragment:
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/GMSB_L180_Ctau100_Pythia8_13TeV_cff.py --fileout file:GMSB_L180_Ctau100_Pythia8_13TeV_FULLSIM.root --mc --eventcontent AODSIM --datatier GEN-SIM --conditions auto:mc --step GEN --python_filename GMSB_L180_Ctau100_Pythia8_13TeV_FULLSIM_cfg.py --no_exec -n 5

cmsRun GMSB_L180_Ctau100_Pythia8_13TeV_FULLSIM_cfg.py

This should produce:
GMSB_L180_Ctau100_Pythia8_13TeV_FULLSIM.root with 5 entries


**************************************************************************************
                                                             STEP 0  GEN->SIM
**************************************************************************************
cmsDriver.py Configuration/GenProduction/python/ThirteenTeV/GMSB_L180_Ctau100_Pythia8_13TeV_cff.py --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM --conditions MCRUN2_71_V1::All --beamspot Realistic50ns13TeVCollision --step GEN,SIM --magField 38T_PostLS1 GMSB_L180_Ctau100_Pythia8_13TeV_GENSIM.root

cmsRun GMSB_L180_Ctau100_Pythia8_13TeV_cff_py_GEN_SIM.py

************************************************************************************************
                                                           NEW RELEASE CMSSW_8_0_20
************************************************************************************************
scram project -n CMSSW8-0-20-GMSBstep12 CMSSW CMSSW_8_0_20
cd CMSSW8-0-20-GMSBstep12/src
cmsenv
cp ../../CMSSW7-1-25-GMSBstep1/src/GMSB_L180_Ctau100_Pythia8_13TeV_cff_py_GEN_SIM.root .
 voms-proxy-init -voms cms -rfc  -> needed to access dbs


**************************************************************************************
                                                             STEP 1 SIM->RAW
**************************************************************************************

cmsDriver.py step1 --mc --eventcontent RAWSIM --pileup 2016_25ns_Moriond17MC_PoissonOOTPU --datatier GEN-SIM-RAW --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v2 --step DIGI,L1,DIGI2RAW,HLT:@frozen2016 --era Run2_2016  --filein file:GMSB_L180_Ctau100_Pythia8_13TeV_cff_py_GEN_SIM.root --fileout file:GMSB_L180_Ctau100_Pythia8_13TeV_cff_py_DIGI_L1_HLT.root --pileup_input "dbs:/MinBias_TuneCUETP8M1_13TeV-pythia8/RunIISummer15GS-MCRUN2_71_V1_ext1-v1/GEN-SIM"

cmsRun step1_DIGI_L1_DIGI2RAW_HLT_PU.py

**************************************************************************************
                                                             STEP 2 RAW->AODSIM
**************************************************************************************

cmsDriver.py step2 --mc --eventcontent AODSIM,DQM --runUnscheduled --datatier AODSIM,DQMIO --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v2 --step RAW2DIGI,L1Reco,RECO,EI,DQM:DQMOfflinePOGMC --era Run2_2016 --filein file:GMSB_L180_Ctau100_Pythia8_13TeV_cff_py_DIGI_L1_HLT.root --fileout file:GMSB_L180_Ctau100_Pythia8_13TeV_cff_py_DIGI2RAW_RECO_AODSIM.root

cmsRun step2_RAW2DIGI_L1Reco_RECO_EI_DQM.py


**************************************************************************************
                                                             STEP 3  AODSIM->MINIAODSIM
**************************************************************************************

cmsDriver.py step3-miniAOD-prod --mc --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM --conditions 80X_mcRun2_asymptotic_2016_TrancheIV_v4 --step PAT --era Run2_2016 --filein file:GMSB_L180_Ctau100_Pythia8_13TeV_cff_py_DIGI2RAW_RECO_AODSIM.root --fileout file:GMSB_L180_Ctau100_Pythia8_13TeV_cff_py_MINIAOD.root --no_exec

cmsRun step3-miniAOD-prod_PAT.py
