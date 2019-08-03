def a(inp, answer_func, sol):
    print('-------------')
    result = answer_func(inp)
    if result != sol:
        print('Input: ', inp)
        print('Real answer: ', sol)
        print('Answer: ', result)
    else:
        print('Correct ', result)