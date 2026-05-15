N = int(input())
unique_courses = set()

for _ in range(N):
    courses = input().split()
    for course in courses:
        unique_courses.add(course)

print(len(unique_courses))