import argparse
import re
import time

start_time = time.time()

parser = argparse.ArgumentParser()
parser.add_argument("--file", '-f', type=str, required=True)
args = parser.parse_args()
inputFile = args.file

with open(inputFile, 'r') as f:
    inpt = f.read()


# Part 1

def reverse_string(st: str) -> str:
    return st[::-1]


def get_sum_calibration_value_1(st: str) -> int:
    nums = []
    for i, s in enumerate(st.split('\n')[:-1]):
        fstr = re.findall("\d+", s)[0][0]
        lstr = re.findall("\d+", reverse_string(s))[0][0]
        nums.append(int(fstr+lstr))
    return sum(nums)


# print(get_sum_calibration_value(inpt))

# Part 2

def check_nk_index(st: str, reversed=False) -> list:
    # print("################ check n index ###############")

    num = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
           'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    if reversed == True:
        num1 = dict()
        for k, v in num.items():
            num1[reverse_string(k)] = v
        num = num1
        st = reverse_string(st)

    firstkey = ''
    firstvalue = '0'
    for k in num.keys():
        if k in st:
            firstkey = k
            break
    for v in num.values():
        if str(v) in st:
            firstvalue = str(v)
            break

    if st.find(firstkey) < st.find(firstvalue):
        return [st.find(firstkey), num[firstkey]]
    else:
        return [st.find(firstvalue), int(firstvalue)]


def get_sum_calibration_value_2(st: str) -> int:
    for i, s in enumerate(st.split('\n')[:-1]):
        # sidha = check_nk_index(s)
        # ulta = check_nk_index(s, reversed=True)
        fstr = check_nk_index(s)[1]
        lstr = check_nk_index(s, reversed=True)[1]
        nums.append(int(fstr+lstr))
    return sum(nums)


def get_sum_calibration_value_2(st: str) -> int:
    nums = []
    num = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
           'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for i, s in enumerate(st.split('\n')[:-1]):
        # print(s)
        for k, v in num.items():
            s = re.sub(k, v, s.lower())
        fstr = re.findall("\d+", s)[0][0]
        lstr = re.findall("\d+", reverse_string(s))[0][0]
        # print('fstr, lstr', fstr, lstr)
        nums.append(int(fstr+lstr))
        with open('output/day1.txt', 'a') as f:
            f.write(fstr+lstr+'\t'+s+' \n')
    return sum(nums)


def get_sum_calibration_value_2(inpt):
    """
        Consider on the cases like oneeight:18, nineight:98, sevenine:79
    """
    finalSum = 0
    for i, s in enumerate(inpt.split('\n')[:-1]):
        num = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
               'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
        num3 = {'one': '1', 'two': '2', 'six': '6'}
        num4 = {'four': '4', 'five': '5', 'nine': '9'}
        num5 = {'three': '3', 'seven': '7', 'eight': '8'}
        tempList = []
        for i in range(len(s)):
            if s[i].isdigit():
                tempList.append(s[i])
            else:
                for n in num.keys():
                    if n in s[i:i+3] and len(n) == 3:
                        tempList.append(num[n])
                    if n in s[i:i+4] and len(n) == 4:
                        tempList.append(num[n])
                    if n in s[i:i+5] and len(n) == 5:
                        tempList.append(num[n])
        finalSum += int(tempList[0]+tempList[-1])
        # print(f'{s}\t{tempList} \t {tempList[0]+tempList[-1]}')
    return finalSum


print('Day 1 Trebuchet Part 1: ', get_sum_calibration_value_1(inpt))
print("------------ %s Seconds ---------------" % (time.time()-start_time))

start_time_part_2 = time.time()
print('Day 1 Trebuchet Part 2: ', get_sum_calibration_value_2(inpt))
print("------------ %s Seconds ---------------" %
      (time.time()-start_time_part_2))
