class datBae:
    def __init__(self, N, B, F):
        self.N = N
        self.B = B
        self.segments = []
        self.requestsAllowed = F
        self.unfailed = True
    
    def segmentTo16(self):
        request = ""
        added = 0
        numSegs16 = 0
        odd = True
        while added <= (self.N - 16):
            added += 16
            numSegs16 += 1
            if odd:
                request += "1"*16
            else:
                request += "0"*16
            odd = not odd
        remainder = self.N-added
        if remainder > 0:
            if odd:
                request += "1"*remainder
            else:
                request += "0"*remainder
        print(request, flush=True)
        received = input()
        if received == "-1":
            self.unfailed = False
        else:
            self.parseSegments(received, remainder)    
                
    def parseSegments(self, received, remainder):
        currChar = "1"
        segCount = 0
        numSegs = 0
        for char in received:
            if char == currChar:
                segCount += 1
            else:
                self.segments.append((16, 16-segCount))
                segCount = 1
                numSegs += 1
                if currChar == "1": currChar = "0"
                else: currChar = "1"
        if remainder == 0:
            self.segments.append((16, 16-segCount))
        else:
            self.segments.append((remainder, remainder-segCount))
    
    def request(self):
        request = ""
        for segment in self.segments:
            halfLength = segment[0]//2
            request += "1"*(halfLength)
            request += "0"*(segment[0]-halfLength)
        print(request, flush=True)
        
    def receive(self):
        received = input()
        if received == "-1":
            self.unfailed = False
        else:
            i = 0
            newSegments = []
            for segment in self.segments:
                numUnbroken = segment[0] - segment[1]
                halfLength = segment[0]//2
                segString = received[i:i+numUnbroken]
                ones = 0
                zeros = 0
                for letter in segString:
                    if letter == "1":
                        ones += 1
                    else: zeros += 1
                s1 = (halfLength, (halfLength-ones))
                newSegments.append(s1)
                length2 = segment[0]-halfLength
                s2 = (length2, (length2-zeros))
                newSegments.append(s2)
                i += numUnbroken
            self.segments = newSegments
            
    def presentBroken(self):
        i = 0
        brokenWorkers = []
        for segment in self.segments:
            if segment[1] >= 1:
                brokenWorkers.append(str(i))
            i += segment[0]  
        return " ".join(brokenWorkers)  
            
    def solveCase(self):
        self.segmentTo16()
        requested = 1
        while requested < self.requestsAllowed and self.unfailed:
            requested += 1
            self.request()
            self.receive()
        print(self.presentBroken(), flush=True)
        correct = input()
        if correct == "-1":
            self.unfailed = False

cases = int(input())
for case in range(1, cases+1):
    N, B, F = [int(s) for s in input().split(" ")]
    x = datBae(N, B, F)
    x.solveCase()
        
    