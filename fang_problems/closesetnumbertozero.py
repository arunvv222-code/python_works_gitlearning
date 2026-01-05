class ClosesetNnumberToZero:

    def solution(self,arr):

        closest_number=arr[0] #-1

        for num in arr:# -1

            if abs(num)<abs(closest_number):#  1<2

                closest_number=num

        if closest_number <0 and abs(closest_number) in arr:

            return (abs(closest_number))

        else:

            return(closest_number)
    
class_instanance=ClosesetNnumberToZero()

print(class_instanance.solution([-4,-3,-2,-1,1,2,3,4]))