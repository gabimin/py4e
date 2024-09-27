def solution(string):
    new = ''
    for c in string:
        new = c + new
    return new

print(solution('luna'))