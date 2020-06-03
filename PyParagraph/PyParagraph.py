import re

#Open text file
f = open("paragraph_1.txt", "r")
p1 = f.read().replace("\n", " ")


f2 = open("paragraph_2.txt", "r")
p2 = f2.read().replace("\n", " ")

def paragraph_summary(paragraph):
    #Split paragraph into strings
    words = paragraph.split(' ')

    #Average letter count
    letter_counts=[]
    for letters in words:
        letter_counts.append(len(letters))

    average_lettercount = sum(letter_counts)/len(letter_counts)

    #Use re.split; 
    sentences = re.split("(?<=[.!?]) +", paragraph)

    #Average sentence length
    sentence_word_counts=[]
    for sentence in sentences:
        sentence_word_counts.append(len(sentence.split(' ')))

    average_wordcount = sum(sentence_word_counts)/len(sentence_word_counts)

    print('Paragraph Analysis')
    print('-----------------------')
    print('Approximate word count: ', len(words))
    print('Approximate Sentence Count: ', len(sentences))
    print('Average Letter Count: ', average_lettercount)
    print('Average Sentence Length: ', average_wordcount)

paragraph_summary(p1)
paragraph_summary(p2)