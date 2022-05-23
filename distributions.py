import numpy as np

def get_sample(eta):
    alphas = np.random.randint(0,2,eta)
    betas = np.random.randint(0,2,eta)

    return sum(alphas-betas)
def run_test(eta1, eta2, iterations):
    q = {}
    print(2**(2*(eta1+eta2)))
    for i in range(iterations):
        e1 = [get_sample(eta1) for i in range(0, 2**(2*(eta1+eta2)))]
        e2 = [get_sample(eta2) for i in range(0, 2**(2*(eta1+eta2)))]

        e3 = [e1[i]*e2[i] for i in range(0,2**(2*(eta1+eta2)))]
        for e in e3:
            if e in q.keys():
                q[e] += 1
            else:
                q[e] = 1
    return q

def find_expected_and_variance(q):
    no_of_samples = sum(q.values())
    expected, variance = 0,0
    
    for k,v in q.items():
        expected += k*v / no_of_samples

    for k,v in q.items():
        variance += (k-expected)**2*v / no_of_samples
    return expected, variance

def print_results(q, iterations):
    min = list(q.keys())[0]
    max = list(q.keys())[0]
    for k,_ in q.items():
        if k < min:
            min = k
        if k > max:
            max = k
    for i in range(min, max+1):
        if i in q.keys():
            print(i, q[i]/iterations)



iterations = 10
test_2_3 = run_test(2,3, iterations)
test_2_2 = run_test(2,2, iterations)
expected_2_3, variance_2_3 = find_expected_and_variance(test_2_3) 
expected_2_2, variance_2_2 = find_expected_and_variance(test_2_2) 


print_results(test_2_3, iterations)
print("________________________")
print_results(test_2_2, iterations)

