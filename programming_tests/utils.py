def compare(test_instance, inputs, answer_func, expected_output):
    result = answer_func(*inputs)
    test_instance.assertEqual(
        result, expected_output,
        '''
        Inputs: {}
        Your Answer: {}
        Real Answer: {}
        '''.format(inputs, result, expected_output)
        
    )
    