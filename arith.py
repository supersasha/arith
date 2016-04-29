# -*- coding: utf-8 -*-
import sys
import random
from termcolor import colored

LVL = 20
N = 10
P_sum = 0.5
MAX_ERRORS = 1
MIN_ELEM = 1
MIN_SUM = 11

def gen_sub_primer(min_sum, max_sum):
    a = random.randint(min_sum, max_sum)
    b = random.randint(1, a - 1)
    return a, b, a - b, '-'

#def gen_add_primer(min_sum, max_sum):
#    a = random.randint(2, max_sum - 1)
#    b = random.randint(1, min(a, max_sum - a))
#    return a, b, a + b, '+'

def gen_add_primer(min_sum, max_sum):
    s, a, b, _ = gen_sub_primer(min_sum, max_sum)
    return a, b, s, '+'

def gen_primer(min_sum, max_sum):
    rnd = random.random()
    if rnd < P_sum:
        return gen_add_primer(min_sum, max_sum)
    else:
        return gen_sub_primer(min_sum, max_sum)

def main():
    print "Уровень:", LVL
    random.seed()
    were = []
    err = 0
    i = 1
    a = None
    b = None
    done = True
    while True:
        if done:
            a, b, ans, sign = gen_primer(MIN_SUM, LVL)
            if (a, b) in were:
                continue
            if a < MIN_ELEM or b < MIN_ELEM:
                continue
        done = False
        sys.stdout.write('{}) {} {} {} = '.format(i, a, sign, b))
        sAns = sys.stdin.readline()
        if sAns.strip() == '.':
            return
        try:
            if int(sAns) == ans:
                were.append((a, b))
                print colored('Правильно!', 'green')
            else:
                print colored('Неправильно.', 'red'), 'Правильный ответ:', colored('{} {} {} = {}'.format(a, sign, b, ans), 'magenta')
                err = err + 1
            i = i + 1
            done = True
        except:
            continue
        if i > N:
            break
    print 'Ошибок:', err
    if err <= MAX_ERRORS:
        print colored('Сдал!', 'green')
    else:
        print colored('Не сдал.', 'red')

if __name__ == '__main__':
    main()
