def factorial(number):
    if number == 1:
        return 1
    fact_m_minus_1 = factorial(number - 1)
    return number * fact_m_minus_1


def calculating_math_func(data):
    return pow(factorial(data) / pow(data, 3), 10)

# зачет!
