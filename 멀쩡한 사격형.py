def solution(w, h):
    number = max(w, h)
    divisor = min(w, h)
    while (number % divisor) != 0:
        remainder = number % divisor
        number = divisor
        divisor = remainder
    return (w*h) - (w+h-(divisor))
