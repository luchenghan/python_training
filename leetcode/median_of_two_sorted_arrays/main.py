def findMedianSortedArrays(nums1, nums2) -> float:
    # Merge the two sorted arrays
    merged = sorted(nums1 + nums2)
    length = len(merged)

    # Check if the total length is even or odd
    if length % 2 == 0:
        # If even, return the average of the two middle elements
        return (merged[length // 2 - 1] + merged[length // 2]) / 2
    else:
        # If odd, return the middle element
        return merged[length // 2]

if __name__ == "__main__":
    # Example usage
    nums1 = [1, 3]
    nums2 = [2]
    result = findMedianSortedArrays(nums1, nums2)
    print(f"Median: {result}")  # Output: 2.0

    nums1 = [1, 2]
    nums2 = [3, 4]
    result = findMedianSortedArrays(nums1, nums2)
    print(f"Median: {result}")  # Output: 2.5