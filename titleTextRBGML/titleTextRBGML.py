class titleTextRBGML:
    def __init__(self):
        pass
    
    def getColorOfTitle(self, redValue, greenValue, blueValue):
        L = (0.2126 * redValue) + (0.7152*greenValue) + (0.0722*blueValue)
	if L > 0.179:
	    return 'black' #000000
        else:
            return 'white' #FFFFFF


