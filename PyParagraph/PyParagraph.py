import os
import re

#Open text file and remove \n
f = open("Resources/paragraph_1.txt", "r")
p1 = f.read().replace("\n", " ")

# f2 = open("Resources/paragraph_2.txt", "r")
# p2 = f2.read().replace("\n", " ")


def paragraph_summary(paragraph):
    #Split paragraph into strings; Each word becomes a string in a list
    words = paragraph.split(' ')

    #Calculate average letter count
    letter_counts=[]
    for letters in words:
        letter_counts.append(len(letters))

    average_lettercount = sum(letter_counts)/len(letter_counts)

    #Use re.split; Each sentence becomes a string in a list
    sentences = re.split("(?<=[.!?]) +", paragraph)

    #Calculate average sentence length
    sentence_word_counts=[]
    for sentence in sentences:
        sentence_word_counts.append(len(sentence.split(' ')))

    average_wordcount = sum(sentence_word_counts)/len(sentence_word_counts)

    #length of words
    word_count = len(words)

    #sentece count
    sentence_count = len(sentences)

    # Specify the file to write to
    output_path = os.path.join("analysis", "PyParagraphResults.txt")

    with open(output_path, 'w') as txtfile:

        txtfile.write('Paragraph Analysis')
        txtfile.write("\n")
        txtfile.write('-----------------------')
        txtfile.write("\n")
        txtfile.write(f'Approximate word count: {word_count}')
        txtfile.write("\n")
        txtfile.write(f'Approximate Sentence Count: {sentence_count}')
        txtfile.write("\n")
        txtfile.write(f'Average Letter Count: {average_lettercount}')
        txtfile.write("\n")
        txtfile.write(f'Average Sentence Length: {average_wordcount}')

paragraph_summary(p1)
#paragraph_summary(p2)


