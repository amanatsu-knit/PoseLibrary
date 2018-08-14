"""Import the pose data to scene."""

import maya.cmds as mc
import json

dataPath = 'D:/work/Maya/PoseLibrary/PoseData/MyPose.pose'
readData = open(dataPath, 'r')
dataList = json.load(readData)

selectionList = mc.ls(sl=True)

for eachSelection in selectionList:
    referencePath = mc.referenceQuery(eachSelection, f=True)
    nameSpace = mc.file(referencePath, q=True, ns=True)
    currentControl = eachSelection.replace('%s:' % nameSpace, '')

    if currentControl in dataList['control']:
        attributeList = dataList['control'][currentControl]

        for eachAttribute in attributeList:
            attributeValue = attributeList[eachAttribute]
            mc.setAttr('%s.%s' % (eachSelection, eachAttribute), attributeValue)
