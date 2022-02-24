'''
3. 양팔저울(DFS)
무게가 서로 다른 K개의 추와 빈 그릇이 있다. 모든 추의 무게는 정수이고, 그릇의 무게는 0으로 간주한다.
양팔저울을 한 번만 이용하여 원하는 물의 무게를 그릇에 담고자 한다.
주어진 모든 추 무게의 합을 S라 하자. 예를 들어, 추가 3개이고, 각 추의 무게가 {1, 2, 6}이면,
S=9이고, 양팔저울을 한 번만 이용하여 1부터 S사이에 대응되는 모든 무게의 물을 다음과 같이 그릇에 담을 수 있다.
만약 추의 무게가 {1, 5, 7}이면 S=13이고, 그릇에 담을 수 있는 물의 무게는 {1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13}이고,
1부터 S사이에서 무게에서 9와 10에 대응하는 무게의 물을 담을수 없다.

K(3<=K<=13)개의 추 무게가 주어지면, 1부터 S사이의 정수 중 측정이 불가능한 물의 무게는
몇 가지가 있는 지 출력하는 프로그램을 작성하세요.
'''
from collections import Counter

def DFS(i, sum_w):
    if i == num_len:
        if sum_w < 1:
            return
        if sum_w <= max_num:
            check[sum_w] += 1
    else:
        DFS(i+1, sum_w)
        DFS(i+1, sum_w + num_list[i])
        DFS(i+1, sum_w - num_list[i])

if __name__ == '__main__':
    num_len = int(input())
    num_list = list(map(int, input().split()))

    max_num = sum(num_list)
    check = [0] * (max_num + 1)
    DFS(0, 0)

    count = Counter(check[1:])
    print(count[0])

