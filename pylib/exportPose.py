import maya.cmds as mc
import os
import datetime
import json

# Collect Control attribute and attribute attribute values

selectionList = mc.ls(sl=True)

controlInfoList = {}

for eachSelection in selectionList :
    attributeList = mc.listAttr(eachSelection, k=True, u=True, sn=True)
    attributeInfoList = {}
    if attributeList :
        for eachAttribute in attributeList :
            attriValue = mc.getAttr ('%s.%s'% (eachSelection, eachAttribute))
            attributeInfoList.setdefault(eachAttribute,attriValue)

        currentControl      = eachSelection
        # Check the Reference
        if mc.referenceQuery (eachSelection, inr=True) :
            referencePath   = mc.referenceQuery(eachSelection, f=True)
            nameSpace       = mc.file(referencePath, q=True, ns=True)
            currentControl  = eachSelection.replace ('%s:'% nameSpace, '')

        controlInfoList.setdefault (currentControl.encode(), attributeInfoList)

print controlInfoList

# Data history
owner           = os.getenv('USERNAME')
time            = datetime.datetime.now ().strftime("%A, %B %d, %Y %Y %H:%M %p")
mayaVersions    = mc.about(q=True, v=True)
versions        = '0.1'
dataList        = {'control':controlInfoList, 'history':[owner, time, mayaVersions, versions]}

#  Writre Pose Data
dataPath        = 'D:/work/Maya/PoseLibrary/PoseData/MyPose.pose'
poseData        = open (dataPath, 'w')
jsonData        = json.dumps (dataList, indent=4)
poseData.write (jsonData)
poseData.close ()

# Create Pose Icon
poseIconPath    = dataPath.replace('.pose', '.png')
currentFrame    = mc.currentTime(q=True)

modelPanelList  = mc.getPanel (type='modelPanel')
for eachModelPanel in modelPanelList :
    mc.modelEditor (eachModelPanel, e=True, alo=False)
    mc.modelEditor (eachModelPanel, e=True, pm=True)

playBlast       = mc.playblast(st=currentFrame, et=currentFrame, fmt='image',
                               cc=True, v=False, orn=False, fp=True, p=100, c='png',
                               wh=[512,512], cf=poseIconPath)