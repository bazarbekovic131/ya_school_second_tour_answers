from collections import deque

def process():
    num_elements, window_size = map(int, input().split())
    result = 0
    dq = deque()
    taken_count = [0] * num_elements
    values = list(map(int, input().split())) 
    
    for i in range(num_elements):
        value = values[i]
        # Remove elements that are out of this window's bounds
        while dq and dq[0][1] <= i - window_size:
            dq.popleft()
        # Maintain the deque such that the smallest elements are at the front
        while dq and dq[-1][0] >= value:
            dq.pop()
        # Add the current element to the deque
        dq.append((value, i))
        # Add the smallest element's value to the result
        result += dq[0][0]
        taken_count[dq[0][1]] += 1
    
    print(result)
    print(' '.join(map(str, taken_count)))

process()