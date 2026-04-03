def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    #her bir harf üzrinden git onu merkez kabul et ona göre en uzununu ölç 
    #ama iki duerum var  birinci tek sayıda harftemn oluşan o basit diğeri ise çift harf 
    #
    #
    
    
    current=""
    longest=""
    for i in range(len(s)):
        l,r=i,i
        while l>=0 and r<=len(s)-1 and s[l]==s[r]:
            current=s[l:r+1]
            l-=1
            r+=1
            if len(current)>len(longest):
                longest=current
                
    for i in range(len(s)-1):
        
        l,r=i,i+1
        while l>=0 and r<=len(s)-1 and s[l]==s[r]:
            current=s[l:r+1]
            l-=1
            r+=1
            if len(current)>len(longest):
                longest=current
    if len(longest)<2:
        return ""
    return longest
            