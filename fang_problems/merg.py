# intervals=[[1,3],[2,6],[8,10],[15,18]]

# merg=[]

# merg.append(intervals[0])# 1,3

# for lst in intervals:# 2,6

#     if merg[-1][1] >= lst[0]:

#         merg[-1][1]=lst[1]

#     else:

#         merg.append(lst)

# print(merg)


class MergedIntervals:

    def solution(self,intervals):

        merg=[]

        merg.append(intervals[0])

        for lst in intervals:

            if merg[-1][1]>=lst[0]:

                merg[-1][1]=lst[1]

            else:

                merg.append(lst)
        return merg

class_instance=MergedIntervals()

print(class_instance.solution([[1,3],[2,6],[8,10],[15,18]]))