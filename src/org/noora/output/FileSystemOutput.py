from org.noora.output.Outputable import Outputable

class FileSystemOutput(Outputable):

  def __init__(self):
    Outputable.__init__(self)
  
  def initialize(self):
    pass
  
  def terminate(self):
    pass
  
  def processOutput(self, what, content):
    print content