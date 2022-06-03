import numpy as np

def get_sample(eta):
    alphas = np.random.randint(0,2,eta)
    betas = np.random.randint(0,2,eta)

    return sum(alphas-betas)
def run_test(eta1, eta2, iterations):
    q = {}
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
        

def add_distributions(d1,d2):
    q = {}
    for i in d1.keys():
        for j in d2.keys():
            if i+j in q.keys():
                q[i+j] += d1[i] * d2[j]
            else:
                q[i+j] = d1[i] * d2[j]
    return q

def multiply_distributions(d1,d2):
    q = {}
    for i in d1.keys():
        for j in d2.keys():
            if i*j in q.keys():
                q[i*j] += d1[i] * d2[j]
            else:
                q[i*j] = d1[i] * d2[j]
    return q

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
## Approach 1
B2 = {-2:1, -1:4, 0:6, 1:4, 2:1}
B2B2 = multiply_distributions(B2, B2)

## for testing with eta_2 = 3 instead of eta_1 = eta_2 = 2
# B3 = {-3:1, -2:6, -1:15, 0:20, 1:15, 2:6, 3:1}


first_two_terms = add_distributions(B2B2, B2B2)
N = add_distributions(first_two_terms, B2)
total = sum(list(N.values()))
print_results(N,total)

#####################################################################################################################
#####################################################################################################################
#####################################################################################################################
## Approach 2


## number of iterations to run the tests
iterations = 10

eta = 2
## for testing with eta_2 = 3 instead of eta_1 = eta_2 = 2
# test_2_3 = run_test(2,3, iterations)
# expected_2_3, variance_2_3 = find_expected_and_variance(test_2_3) 

# samples_2 = [get_sample(eta) for i in range(0, iterations*2**(2*(eta)))]
# test_2_2 = run_test(2,2, iterations)
# expected_2_2, variance_2_2 = find_expected_and_variance(test_2_2) 
# ## supposing that the terms are uncorrelated (since they are sampled)


# expected = 2*expected_2_2 + expected_2
# variance = variance_2_2 
# print(f"The expected value of B2*B2 is {expected} and the variance is {variance}")





