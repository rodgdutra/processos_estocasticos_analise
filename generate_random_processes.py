import numpy as np
from random import randrange
from random import random
from random import normalvariate
from random import uniform
from random import expovariate

'''
Random Processes Class - UFPA - 2019
Goal: Generate several different random processes to be later analyzed.
Code tested with Python 3.6.5.
@author: Aldebaro Klautau
'''

def get_realization_process_number_1(num_samples=100):
    '''
    Generate one realization of your (customized) random process
    :param num_samples: number of samples in this realization
    :return: the waveform (vector) corresponding to the realization
    '''
    x_shape = (num_samples,) #define a shape
    x = np.zeros(x_shape) #initialize
    previous_sample = -1
    for i in range(num_samples): #loop to generate all samples
        this_sample = previous_sample + randrange(10) + 5*random() - uniform(2.5, 10.0) + expovariate(1 / 4)
        x[i] = this_sample
        previous_sample = this_sample
    return x

def get_realization_process_number_2(num_samples=100):
    '''
    Generate one realization of your (customized) random process
    :param num_samples: number of samples in this realization
    :return: the waveform (vector) corresponding to the realization
    '''
    x_shape = (num_samples,) #define a shape
    x = np.zeros(x_shape) #initialize
    chosen_variance = 12 #variance for both distributions
    uniform_support = np.sqrt(12 * chosen_variance) #variance = support^2 / 12
    for i in range(num_samples): #loop to generate all samples
        coin = randrange(2)
        if coin == 0:
            this_sample = normalvariate(mu=0, sigma=np.sqrt(chosen_variance))
        elif coin == 1:
            this_sample = uniform(-uniform_support/2.0, uniform_support/2.0)
        else:
            raise Exception('Logic error!', coin)
        x[i] = this_sample
    return x


def generate_and_save_process_realizations(method_to_generate_realization=None,
                                           num_realizations=100,
                                           num_samples_per_realization=100):
    '''
    Generates realizations of a given process and save them into a single NPZ file.
    :param method_to_generate_realization: method that will be called to get realization
    :param num_realizations: number of realizations of the stochastic process
    :param num_samples_per_realization: number of samples in each realization
    :param output_file_name: name of file that will be written
    :return all realizations of the random process as a numpy array of dimension
            num_realizations x  num_samples_per_realization
    '''
    #initialize with zeros
    all_realizations = np.zeros( (num_realizations, num_samples_per_realization) )
    for m in range(num_realizations): #generate all realizations
        all_realizations[m] = method_to_generate_realization(num_samples=num_samples_per_realization)
    return all_realizations

#generate realizations of the two random processes
num_realizations=400
num_samples_per_realization=150

X1 = generate_and_save_process_realizations(method_to_generate_realization=get_realization_process_number_1,
                                       num_realizations=num_realizations,
                                       num_samples_per_realization=num_samples_per_realization)
X2 = generate_and_save_process_realizations(method_to_generate_realization=get_realization_process_number_2,
                                       num_realizations=num_realizations,
                                       num_samples_per_realization=num_samples_per_realization)

#write files for two processes, 1 and 2:
process_file_name='example_process.npz'
np.savez(process_file_name, X1=X1, X2=X2)

#read files that were saved
dictionary_with_arrays=np.load(process_file_name)
X1=dictionary_with_arrays['X1'] #extract array X1
print('X1=',X1)
X2=dictionary_with_arrays['X2'] #extract array X2
print('X2=',X2)
