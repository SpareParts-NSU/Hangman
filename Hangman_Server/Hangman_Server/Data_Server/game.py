from random_word import RandomWords

seed = 0
RandomWord = RandomWords()

wordType = ["noun", "verd", "adjective", "adverb"]
minDict = 1
maxDict = 10
minLen = 5
maxLen = 10
sortedBy = ["alpha", "count"]
sortOrder = ["asc", "desc"]
limit = 3

Words = RandomWord.get_random_words(hasDictionaryDef = "true", includePartOfSpeech = wordType[0], minCorpusCount = 1, maxCorpusCount = 10, minDictionaryCount = 1, maxDictionaryCount = 10, minLength = 5, maxLength = 10, sortBy = sortedBy[0], sortOrder = sortOrder[1], limit = limit)

#print(Words)

