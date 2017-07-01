class average :

    count = 1
    avg = 0

    def __init__(self,secret_text) :
        self.message = secret_text
        self.var = len(self.message.split())
        average.avg = (average.avg + self.var)/ average.count
        average.count+=1
        print ("Average of sending words: "+str(average.avg))





