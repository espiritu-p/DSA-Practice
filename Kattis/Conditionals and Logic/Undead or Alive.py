sentence = input()

if ":)" in sentence and ":(" in sentence:
    print("double agent")
elif ":)" in sentence:
    print("alive")
elif ":(" in sentence:
    print("undead")
else:
    print("machine")
