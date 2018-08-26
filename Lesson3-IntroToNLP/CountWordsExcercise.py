
# coding: utf-8

# In[6]:


"""Count words."""

def count_words(text):
    """Count how many times each unique word occurs in text."""
    counts = dict()  # dictionary of { <word>: <count> } pairs to return
    
    # TODO: Convert to lowercase
    text = text.lower()
    # TODO: Split text into tokens (words), leaving out punctuation
    # (Hint: Use regex to split on non-alphanumeric characters)
    import re
   # split into words by white space
    words = text.split()
    # remove punctuation from each word
    import string
    table = str.maketrans('', '', string.punctuation)
    text = [w.translate(table) for w in words]
    
    print(text)
    # TODO: Aggregate word counts using a dictionary
    
    for item in text:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    return counts


def test_run():
    with open("D:/NanoDegree/NLPNanoDegree/Lesson3-IntroToNLP/input.txt", "r") as f:
        text = f.read()
        print("Text : ",text)
        counts = count_words(text)
        sorted_counts = sorted(counts.items(), key=lambda pair: pair[1], reverse=True)
        
        print("10 most common words:\nWord\tCount")
        for word, count in sorted_counts[:10]:
            print("{}\t{}".format(word, count))
        
        print("\n10 least common words:\nWord\tCount")
        for word, count in sorted_counts[-10:]:
            print("{}\t{}".format(word, count))


if __name__ == "__main__":
    test_run()

