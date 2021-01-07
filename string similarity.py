import math
text1 = '''Java is a class-based, object-oriented programming language that is designed to have as few implementation dependencies as possible. It is a general-purpose programming language intended to let application developers write once, run anywhere (WORA),[17] meaning that compiled Java code can run on all platforms that support Java without the need for recompilation.[18] Java applications are typically compiled to bytecode that can run on any Java virtual machine (JVM) regardless of the underlying computer architecture. The syntax of Java is similar to C and C++, but has fewer low-level facilities than either of them. The Java runtime provides dynamic capabilities (such as reflection and runtime code modification) that are typically not available in traditional compiled languages. As of 2019, Java was one of the most popular programming languages in use according to GitHub,[19][20] particularly for client-server web applications, with a reported 9 million developers'''
text2 = '''Java is a programming language and computing platform first released by Sun Microsystems in 1995. There are lots of applications and websites that will not work unless you have Java installed, and more are created every day. Java is fast, secure, and reliable. From laptops to datacenters, game consoles to scientific supercomputers, cell phones to the Internet, Java is everywhere!'''

#Similarity
#1.tokenization -> tokens
token1 = text1.split()
token2 = text2.split()

#2.Remove StopWords->is,am,are,we,has,have,it ,they..
from nltk.corpus import stopwords
stopwords = stopwords.words('english')

for s_word in stopwords:
    if s_word in token1:
        token1.remove(s_word)
    if s_word in token2:
        token2.remove(s_word)

set1 = set(token1)
set2 = set(token2)
#3 Jaccards Index
union = set1.union(set2)
intersection = set1.intersection(set2)
ji = len(intersection)/len(union)
print(f"perc = {math.floor(ji*100)}%")
'''
for word in token1:
    if word in stopwords:
        token1.remove(word)

for word in token2:
    if word in stopwords:
        token2.remove(word)
'''
