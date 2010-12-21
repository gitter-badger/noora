#!/usr/bin/env python

import core.Connector as Connector
import os
import subprocess
import core.NooraException as NooraException
import traceback

class OracleConnector(Connector.Connector):
  
  def __init__(self):
    Connector.Connector.__init__(self)
  
  def getScriptDir(self):
    return self.getNooraDir()+os.sep+'scripts'
  
  def execute(self, oracleSid, oracleUser, oraclePasswd, oracleScript, paramA, paramB):
    try:
      projectHelper=self.getProjectHelper()
      handle=open('feedback.log','wb')
      connectString=oracleUser+'/'+oraclePasswd+'@'+oracleSid
      startupInfo=subprocess.STARTUPINFO()
      startupInfo.dwFlags |=subprocess.STARTF_USESHOWWINDOW
      startupInfo.wShowWindow=subprocess.SW_HIDE
      templateScript=projectHelper.cleanPath('@'+self.getScriptDir()+os.sep+'template.sql')
      result=subprocess.call(['sqlplus','-l','-s',connectString , templateScript, oracleScript, paramA, paramB],shell=False,stdout=handle,stderr=handle,startupinfo=startupInfo,creationflags=subprocess.SW_HIDE)
      
      if result!=0:
        stream=projectHelper.readFile('feedback.log')
        raise NooraException.NooraException(stream)
    except OSError:
      raise NooraException.NooraException("Could not execute sqlplus. Is it installed and in your path?")




