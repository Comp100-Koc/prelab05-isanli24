def remove_adjacent_duplicates(s):
    '''
    Given a string remove all the adjacent duplicate characters and return the string
    '''
    #
    #
    j=0
    if len(s)<2:
        return s
    while j<len(s)-1:
        if s[j]==s[j+1]:
            s=s[:j]+s[j+2:]
            j=0
        else:
            j+=1
                
    return s
            
    
    
    
    

        
        
        
