''' 
	Synthesizer handles and glues together many Sample instances, 
	producing and saving the final wav file.

'''


import numpy as np
import scipy.io.wavfile 
import math as m
import os
import copy

class Synthesizer:

	samplesList = []
	samplesMatrix = None
	sampleRate = 44100
	timeDuration = 0


	def addSample(self, sample, start_time=0, loop_times=1, loop_seconds=None):

		sample = copy.deepcopy(sample)


		if loop_seconds is not None:
			loop_times = loop_seconds * self.sampleRate

		if start_time is not 0:
			sample.leftPad(start_time)




		if self.timeDuration is 0:
			self.timeDuration = sample.timeDuration
		elif self.timeDuration > sample.timeDuration:
			sample.rightPad(self.timeDuration - sample.timeDuration)
		elif self.timeDuration < sample.timeDuration:
			self.timeDuration = sample.timeDuration




		sample.applyLoop(loop_times)


		self.samplesList.append(sample)	
		if self.samplesMatrix is None:
			self.samplesMatrix = sample.waveForm
		else:
			self.samplesMatrix = np.concatenate((self.samplesMatrix, sample.waveForm))



	def removeSample(self, s):
		return None

	def getWaveForm(self):
		return np.sum(self.samplesMatrix, 0)	

	def saveWaveForm(self, waveForm, fname):
			

		waveForm = np.array([s*2**15 for s in waveForm.tolist()], np.int16)
		if os.path.isfile(fname): os.remove(fname)
		scipy.io.wavfile.write(fname, self.sampleRate, waveForm)		

'''

def subbass_f(t):
	return 40 

subbass = Sample()
subbass.setDuration(1)
subbass.setFrequency(subbass_f)

s = Sample()
s.loadFromFile("kicks/kick1.wav")

subbass.addSample(s, start_time=1)


a = Synthesizer()

a.addSample(subbass, loop_times=5)
a.saveWaveForm(a.getWaveForm(), "shakeyourbody.wav")

'''
