def longest_unique_range(nums):
    # اگر لیست خالی باشد
    if not nums:
        return (0, (-1, -1))

    left = 0                  # ابتدای پنجره
    freq = {}                 # شمارش عناصر داخل پنجره
    best_len = 0
    best_l = 0
    best_r = 0

    # حرکت دادن انتهای پنجره
    for right in range(len(nums)):
        x = nums[right]
        freq[x] = freq.get(x, 0) + 1

        # اگر تکراری شد، از چپ جمع کن
        while freq[x] > 1:
            left_val = nums[left]
            freq[left_val] -= 1
            left += 1

        # طول پنجره فعلی
        current_len = right - left + 1

        # اگر بهتر از قبلی بود، ذخیره کن
        if current_len > best_len:
            best_len = current_len
            best_l = left
            best_r = right

    return (best_len, (best_l, best_r))
