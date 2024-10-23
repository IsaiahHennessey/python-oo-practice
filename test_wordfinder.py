from wordfinder import WordFinder, SpecialWordFinder


print("Testing WordFinder:")
wf = WordFinder("words.txt")
print(wf.random())
print(wf.random())
print(wf.random())

print("\nTesting SpecialWordFinder:")
swf = SpecialWordFinder("words.txt")
print(swf.random())
print(swf.random())
print(swf.random())