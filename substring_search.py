import sys

class SubstringSearch:
    def __init__(self):
        pass

    @staticmethod
    def brute_search(pat, txt):
        M = len(pat)
        N = len(txt)
        print('M = {0}, N = {1}'.format(M, N))
        
        for i in range(N-M+1):
            count = 0
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else:
                    count += 1
            print ('count is {0}'.format(count))
            if (count == M):
                return i
        return N

    @staticmethod
    def brute_search_alt(pat, txt):
        M = len(pat)
        N = len(txt)
        print('M = {0}, N = {1}'.format(M, N))
        
        for i in range(N):
            print('i is {0}'.format(i))
            for j in range(M):
                if (txt[i] == pat[j]):
                    j += 1
                else:
                    i -= j
                    j = 0
        print('j is {0}'.format(j))

        if (j == M): 
            return i - M
        else:
            return N

if __name__ == "__main__":
    pat = sys.argv[1]
    txt = sys.argv[2]
    idx = SubstringSearch.brute_search_alt(pat, txt)
    print('match found at {0}'.format(idx))
