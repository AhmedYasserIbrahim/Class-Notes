# Byte Pair Encoding (BPE) Summary

**Byte Pair Encoding (BPE)** is a method commonly used in **subword tokenization** to break down complex or rare words into smaller, more frequent units. For example, instead of treating `"learning"` as a single token, BPE can split it into `"learn"` and `"ing"`, making it easier for the model to generalize and handle new words effectively.

## Steps for BPE Tokenization

1. **Collect the Corpus:** Gather all the words in your corpus.  
2. **Character Initialization:** Split every word into its individual characters and store all **unique characters** in your initial vocabulary.  
3. **Pair Frequency Count:** Identify all adjacent pairs of characters in the corpus and count their frequencies.  
4. **Merge the Most Frequent Pair:** Find the most frequently occurring pair, name it **X**, and merge it into a new token by replacing the pair with **X**.  
5. **Repeat with Updated Pairs:** Repeat the process by counting frequencies again, now considering the newly merged pairs, and merge the next most frequent pair.  
6. **Continue Until Vocabulary Size is Met:** Repeat this process until the desired number of tokens in your vocabulary is reached.  
7. **Tokenizing New Words:** When processing new words, break them down using the **final vocabulary** created during training. If a word is unfamiliar, BPE will tokenize it into subwords using the learned tokens.

## Key Insight

By the end of this process, the vocabulary will consist of **whole words, subwords, and characters**, improving the model's ability to handle rare words and reduce the vocabulary size.
