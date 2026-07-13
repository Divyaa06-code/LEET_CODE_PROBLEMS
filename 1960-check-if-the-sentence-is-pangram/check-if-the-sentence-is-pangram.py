class Solution(object):
    def checkIfPangram(self, sentence):
       letters=set(sentence)
       return len(letters)==26