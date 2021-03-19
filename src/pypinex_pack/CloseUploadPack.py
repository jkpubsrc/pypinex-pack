



import os
import typing
import io

import jk_uploadpack

from pypine import *






class CloseUploadPack(AbstractProcessor):

	################################################################################################################################
	## Constructor
	################################################################################################################################

	#
	# Constructor method.
	#
	def __init__(self):
		super().__init__()
	#

	def initializeProcessing(self, ctx:Context):
		self.__up = ctx.localData.get("uploadpack")
		if self.__up is None:
			raise Exception("No upload pack created!")
	#

	################################################################################################################################
	## Public Properties
	################################################################################################################################

	################################################################################################################################
	## Helper Methods
	################################################################################################################################

	################################################################################################################################
	## Public Methods
	################################################################################################################################

	def processingCompleted(self, ctx:Context):
		self.__up.close()

		f2 = DiskFile.fromFile(
			os.path.dirname(self.__up.filePath),
			self.__up.filePath,
		)

		ctx.printVerbose(self, "Archive created: " + f2.absFilePath)

		return f2
	#

#





