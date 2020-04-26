import sys
import math

total_party, total_votes = map(int, sys.stdin.readline().split())
vote_for_party = []
TOTAL_SEATS = 300  # 총 국회의원 의석 수수
PROP_JUN_SEATS = 30  # 준연동방식 배분 의석수
PROP_BYEONG_SEATS = 17  # 기존 병립형방식 배분 의석수
TOTAL_PROP_SEATS = PROP_JUN_SEATS + PROP_BYEONG_SEATS  # 총 비례대표 의석수
not_in_party = TOTAL_SEATS - TOTAL_PROP_SEATS # 무소속 당선자 수. 1단계에서 계산함
total_s_i = 0       # 1단계 계산용
new_total_s_i = 0   # 2~3단계 계산용
flag = -1


def get_input():
    for _ in range(total_party):
        global flag, not_in_party, vote_for_party
        name, region, prop = map(str, sys.stdin.readline().split())
        region = int(region)
        prop = int(prop)
        not_in_party -= region
        if region >= 5 or prop >= 0.03 * total_votes:
            is_prop_party = True
        else:
            is_prop_party = False
        vote_for_party.append({'flag': flag, 'name': name, 'r': region, 'p_votes': prop, 'p_rate': 0,
                               's_apos': 0, 's': 0, 't': 0, 'total': 0,
                               'is_p': is_prop_party, 'rem': 0})
        '''
            flag: 정당기호
            name: 정당명
            r: 지역구 의석
            p_votes: 비례 득표수
            p_rate: 비례 득표율(무효표 포함)
            s_apos: 연동 배분 의석 (1~2단계)
            s: 조정된 비례대표 의석 (1~2단계)
            t: 연동 배분 의석(3단계)
            total: 지역구 + 비례대표 의석(r + s + t)
            is_p: 비례대표 의석 받는 정당인지(봉쇄조항에 따른)
            rem: remainder            
        '''
        flag -= 1


def print_votes():
    print(f"{'flag':^4}|{'name':^25}|{'r':^5}|{'p_votes':^12}|{'p_rate':^20}|"
          f"{'s_ap':^5}|{'s':^5}|{'t':^5}|{'is_p':^5}|{'total':^6}|{'rem':^20}")
    for data in vote_for_party:
        print(f"{0 - data['flag']:4}|{data['name']:25}|{data['r']:5}|{data['p_votes']:12}|{data['p_rate']:20}|"
              f"{data['s_apos']:^5}|{data['s']:5}|{data['t']:5}|{data['is_p']:5}|{data['total']:6}|{data['rem']:20}|")




def step_1():
    global vote_for_party
    total_counted_votes = 0
    total_s = 0
    N = 300
    R = not_in_party
    # 무소속 당선자와 의석할당정당이 아닌 정당의 당선자를 제외하고,
    # 무효표와 의삭할당정당이 아닌 정당에 투표된 비례대표 득표를 제외한 유효총투표수 계산

    for data in vote_for_party:
        if not data['is_p']:
            R += data['r']
        else:
            total_counted_votes += data['p_votes']

    # 연동 배분 의석 수 s_i' 계산
    for data in vote_for_party:
        if data['is_p']:
            prop_rate = data['p_votes'] / total_counted_votes
            data['p_rate'] = prop_rate
            s_i = ((N - R) * prop_rate - data['r']) / 2
            if s_i < 1:
                s_i = 0
            else:
                s_i = round(s_i)
            data['s_apos'] += s_i
            total_s += s_i
    if total_s == PROP_JUN_SEATS:  # s_i의 합이 30과 같은지, 작은지, 큰지에 따라 3단계, 2-1단계, 2-2단계로 넘어감
        step_3()
    elif total_s < PROP_JUN_SEATS:
        step_2_1(total_s)
    elif total_s > PROP_JUN_SEATS:
        step_2_2(total_s)


def step_2_1(total_s):
    global vote_for_party

    for data in vote_for_party:
        total_s += data['s_apos']

    for data in vote_for_party:
        new_props = data['s_apos'] + (PROP_JUN_SEATS - total_s * data['p_rate'])
        data['s'], data['rem'] = math.floor(new_props), new_props - math.floor(new_props)
        total_s += data['s']

    distribute_remainder('s', PROP_JUN_SEATS)
    step_3()


def step_2_2(total_s):
    global vote_for_party
    for data in vote_for_party:
        new_props = (PROP_JUN_SEATS * data['s_apos']) / total_s
        data['s'], data['rem'] = math.floor(new_props), new_props - math.floor(new_props)
        total_s += data['s']

    distribute_remainder('s', PROP_JUN_SEATS)
    step_3()


def step_3():
    global vote_for_party
    for data in vote_for_party:
        new_props = PROP_BYEONG_SEATS * data['p_rate']
        added_seat, remainder = math.floor(new_props), new_props - math.floor(new_props)
        new_total_s += added_seat
        data['t'], data['rem'] = added_seat, remainder

    distribute_remainder('t', TOTAL_PROP_SEATS)


def distribute_remainder(key, limit):
    global vote_for_party
    vote_for_party = sorted(vote_for_party, key=lambda vote_for_party: (vote_for_party['rem'], vote_for_party['flag']), reverse=True)
    index = 0
    while new_total_s_i < limit:
        if vote_for_party[index]['is_p'] and vote_for_party[index]['rem'] >= 0:
            vote_for_party[index][key] += 1
            new_total_s_i += 1
            index += 1
        else:
            index = 0


def print_results():
    global vote_for_party
    for data in vote_for_party:
        data['total'] = data['r'] + data['s'] + data['t']

    vote_for_party = sorted(vote_for_party, key=lambda vote_for_party: vote_for_party['total'], reverse=True)
    for data in vote_for_party:
        print(f"{data['name']} {data['total']}")


if __name__ == '__main__':
    get_input()
    step_1()
    print_results()
