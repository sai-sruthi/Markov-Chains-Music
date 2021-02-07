# Markov-Chains-Music
Application of Markov Chains in Music

Markov Chains are a sequence of random numbers, where the current random number only depends on one previous state. 
In the domain of music, it can be used to predict the notes of a song, given that it has had a song to work on before.
In essence, it allows for some amount of machine learning probabilistic modeling of music.
With the notes of the input song, 
we can construct an adjacency matrix for a Markov Chain by calculating the probabilities of the occurrence of a note,
depending on its previous note. The output is a clear, noiseless melody which is similar to the one given as the input.

