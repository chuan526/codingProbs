

def prodOfAllOtherElem(nums):
    forward = []
    backward = []

    for i, num in enumerate(nums):
        if not forward:
            forward.append(1)
        else:
            forward.append(forward[-1]*nums[i-1])
    for i in range(len(nums)-1, -1, -1):
        if not backward:
            backward.append(1)
        else:
            backward.append(backward[-1]*nums[i+1])

    res = []
    for right, left in zip(forward, reversed(backward)):
        res.append(left*right)
    print(res)


if __name__ == '__main__':
    nums1 = [5,2,3,4,2]
    nums2 = [0]
    nums3 = []
    nums4 = [-4, -1, 2, 3, 5]
    nums5 = [9,-8,-1,1,2,3,5]

    prodOfAllOtherElem(nums1)
    prodOfAllOtherElem(nums2)
    prodOfAllOtherElem(nums3)
    prodOfAllOtherElem(nums4)
    prodOfAllOtherElem(nums5)
