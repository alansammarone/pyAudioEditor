# pyAudioEditor

This is a simple audio synthesizer and editor written in Python. 

## Usage

You can create a varying frequency sample, 2 seconds long, whose frequency is defined by a function of time: 

```python
def frequency1(t):
	return 40.0 + 10.0*m.cos(t*m.pi*2.0)

sample1 = Sample()
sample1.setDuration(2.0)
sample1.setFrequency(frequency1)
```

...then, create a second sample, a quarter of second long, with a constant frequency of 440 Hz:
 
```python
sample2 = Sample()
sample2.setDuration(.25)
sample2.setFrequency(440)
```

... then add the second to the first: 
```python
sample1.addSample(sample2, start_time=1.75)
```

...then save it, looped 3 times, to a wav file:

```python
syn = Synthesizer()
syn.addSample(sample1, loop_times=3)
syn.saveWaveForm(syn.getWaveForm(), "shakeyourbody.wav")

```

## Documentation

Documentation will be available soon.





