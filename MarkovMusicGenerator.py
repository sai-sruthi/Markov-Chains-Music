from MarkovChainBuilder import MarkovChainBuilder
import pysynth

class MarkovMusicGenerator:
	def __init__(self):
		self._note_prev = None
		self._markov = MarkovChainBuilder(['a', 'a#', 'b', 'c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#'])
		self._timings = MarkovChainBuilder([1, 2, 4, 8, 16])

	def add(self, note_to):
		if(self._note_prev is None):
			self._note_prev = note_to
			return
		note_from = self._note_prev
		self._markov.add(note_from[0], note_to[0])
		self._timings.add(note_from[1], note_to[1])
		self._note_prev = note_to

	def note_next(self, note_from):
		return [self._markov.value_next(note_from[0]), self._timings.value_next(note_from[1])]

learn_music = MarkovMusicGenerator()

learn_music.add(["f", 4])
learn_music.add(["f", 4])
learn_music.add(["c", 4])
learn_music.add(["c", 4])

learn_music.add(["d", 4])
learn_music.add(["d", 4])
learn_music.add(["c", 2])

learn_music.add(["b", 4])
learn_music.add(["b", 4])
learn_music.add(["a", 4])
learn_music.add(["a", 4])

learn_music.add(["g", 4])
learn_music.add(["g", 4])
learn_music.add(["f", 2])

learn_music.add(["c", 4])
learn_music.add(["c", 4])
learn_music.add(["b", 4])
learn_music.add(["b", 4])

learn_music.add(["a", 4])
learn_music.add(["a", 4])
learn_music.add(["g", 4])

random_score = []
note_current = ['f', 4]
for i in range(0, 100):
	print note_current[0] + ',' + str(note_current[1])
	note_current = learn_music.note_next(note_current)
	random_score.append(note_current)

pysynth.make_wav(random_score, fn = "first_score.wav")
