import heapq
A=[]
heapq.heappush(A,5)
heapq.heappush(A,10)
print(A[0])
menor=heapq.heappop(A)
print(len(A))