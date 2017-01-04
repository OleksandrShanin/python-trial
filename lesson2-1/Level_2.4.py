text = "hi hi hI ho hO hi Ho ho Hi hi ho ho ho hi"

text = text.lower()
hi_count = 0
while text.find("hi") >= 0:
    text = text.replace("hi", "bye", 1)
    print text
    hi_count = hi_count + 1

print text
print "%d hi's were replaced" % hi_count
