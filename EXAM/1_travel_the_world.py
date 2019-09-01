n = int(input())
m_paid = float(input())
made_reviews = 0

for item in range(n):
    to_decode = input()
    review_item = []
    if to_decode.isdigit():
        for char in range(1, len(to_decode), 2):
            digit_1 = to_decode[char-1]
            digit_2 = to_decode[char]
            digit = int(digit_1 + digit_2)
            letter = chr(digit)
            review_item.append(letter)
        print(f'Reviewing item - {"".join(review_item)}')
        made_reviews += 1
    elif to_decode.isalpha():
        review_item = ''.join(reversed(to_decode))
        print(f'Reviewing location - {review_item}')
        made_reviews += 1

print(f'{made_reviews} reviews have been made this month. Salary: {(made_reviews * m_paid):.2f}')