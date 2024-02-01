def strangeCounter(t):
    fn = 1
    ln = 3
    counter = 3

    while t < fn or t > ln:
        fn += counter
        counter *= 2
        ln += counter

    fv = fn + 2
    lv = 1

    mn, mv = (fn + ln) // 2, (fv + lv) // 2
    while mn != t:
        if t > mn:
            fn = mn
            mn = (fn + ln) / 2
            fv = mv
            mv = (fv + lv) / 2
        elif t < mn:
            ln = mn
            mn = (fn + ln) / 2
            lv = mv
            mv = (fv + lv) / 2
        print('mn right now:', mn, '->', mv, '| with fn ln:', fn, ln)

    result = math.ceil(round(mv, 2))

    return result
