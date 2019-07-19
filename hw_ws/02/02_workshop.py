# 1. 두 개의 정수 n과 m이 주어질 때, 반복문을 사용하여 별(*) 문자를 이용해 가로의 길이가 n, m인 사각형을 출력하시오.
n = 5
m = 9

i=0
while i < m:
    print('*'*n, end='\n')
    i+=1

# 2. 과목명과 점수가 담긴 student dictionary에서 평균 점수를 출력하시오.
student = {'python': 80, 'algorithm': 99, 'django': 89, 'flask': 83}
score_sum = sum(student.values())
num = len(student.values())
print(sum(student.values())/num)



# # 3. 혈액형 문제 딕셔너리(반복문을 사용하여 key는 혈액형 종류, value는 인원 수)
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']

# # cntA, cntB, cntO, cntAB = 0, 0, 0, 0
# # for i in blood_types:
# #     if i == 'A':
# #         cntA +=1
# #     elif i == 'B':
# #         cntB +=1
# #     elif i == 'O':
# #         cntO +=1
# #     else:
# #         cntAB +=1

# '''
# bt_dict = {
#     'A': 0,
#     'B': 0,
#     'O': 0,
#     'AB': 0
# }

# # a = blood_types.count('A')
# # b = blood_types.count('B')
# # o = blood_types.count('O')
# # ab = blood_types.count('AB')

# # bt_dict['A'] = a
# # bt_dict['B'] = b
# # bt_dict['O'] = o
# # bt_dict['AB'] = ab
# '''
# # blood_dict2 = {}
# #blood_dict = dict()

#내장함수 collections 이용하는 방법.
import collections
blood_types_str = "A B A O AB AB O A B O B AB"
print(collections.Counter(blood_types))
