def solution(s):
    s = s.lower()
    return False if s.count("p") != s.count("y") else True
