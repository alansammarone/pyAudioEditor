import numpy as np
import math as m

class Sample:

	sampleRate = 44100
	timeDuration = 1.0
	waveType = 1 # 1 = Sine wave, 2 = Triangle wave, 3 = Square wave
	frequencyType = None # 1 = Constant frequency, 2 = function-based frequency, None = doesn't apply (when sample is loaded from file)
	frequencySource = None


	sampleDuration = sampleRate*timeDuration
	waveForm = None # The amplitude as a function of time 


	def setFrequency(self, f):
		if type(f) is int:
			self.frequencyType = 1
			self.frequencySource = f
		elif type(f) is function:
			self.frequencyType = 2
			self.frequencySource = f
		else:
			raise Exception("Frequency of sample must be either an integer or a function of time.")

		self.buildWaveForm()



	def setDuration(self, t):
		self.timeDuration = t
		self.sampleDuration = t*self.sampleRate

	def leftPad(self, t):
		padSamples = t*self.sampleRate
		self.waveForm = np.concatenate((np.zeros(1, padSamples), self.waveForm))
		self.timeDuration += t
		self.sampleDuration += padSamples


	def rightPad(self, t):
		padSamples = t*self.sampleRate
		self.waveForm = np.concatenate((self.waveForm, np.zeros(1, padSamples)))
		self.timeDuration += t
		self.sampleDuration += padSamples


	def padSample(self, t):
		self.leftPad(t)
		self.rightPad(t)

	def leftTrim(self):
		return None

	def rightTrim(self):
		return None

	def trimSample(self):
		return None



	def applyEchoFilter(self, d, s):
		return None

	def makeEchoMatrix(self, d, s):
		return None

	@staticmethod
	def sineWaveFunction(t):
		return m.sin(2*m.pi*t)

	@classmethod
	def vectorizedSineWaveFunction(cls, tArray):
		vectorizedFunction = np.vectorize(cls.sineWaveFunction)
		return vectorizedFunction(tArray)


	def buildWaveForm(self):
		t = np.array([[s*self.timeDuration/self.sampleDuration for s in xrange(int(self.sampleDuration))]])
		self.waveForm = self.vectorizedSineWaveFunction(t)
		print self.waveForm.shape




s = Sample()
s.setFrequency(500)