class Solution:

    def common2str(self,x:list, y:list)->list:
        res=[]
        dict2=self.string2dictn(y)
        for char in x:
            if char in dict2 and dict2[char]>0:
                res.append(char)
                dict2[char]-=1
        return res

    def string2dictn(self,val:list):
        map_str1={}
        for char in val:
            if char in map_str1:
                map_str1[char]+=1
            else:
                map_str1[char]=1
        return map_str1

A = ["bella", "label", "roller"] #[e,l,l]
# A=["","abcd","ab","a","abcde","abc"]


# obj=Solution()
# str_temp=[]
# str_temp=obj.common2str(A[0], A[1])

for i in range(2,len(A)):
    if len(str_temp)==0:
        break
    else:
        str_temp=obj.common2str(str_temp,list(A[i]))
print(str_temp)


