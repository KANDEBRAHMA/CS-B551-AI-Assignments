###################################
# CS B551 Spring 2021, Assignment #3
#
# Your names and user ids:
#
# (Based on skeleton code by D. Crandall)
#


import random
import math


# We've set up a suggested code structure, but feel free to change it. Just
# make sure your code still works with the label.py and pos_scorer.py code
# that we've supplied.
#
train = {}
label_count = {}
first_word_count_dict = {}
first_word_label = {}
transition_partsof_speech = {}
second_level_transition_dict = {}
transition_prob = {}
emission_prob = {}
second_level_transition_prob = {}
unique_parts_of_speech = []

class Solver:
    # Calculate the log of the posterior probability of a given sentence
    #  with a given part-of-speech labeling. Right now just returns -999 -- fix this!
    def add_transition_states(self,previous_pos,present_pos):
        if previous_pos in transition_partsof_speech:
            if present_pos in transition_partsof_speech[previous_pos]:
                transition_partsof_speech[previous_pos][present_pos] += 1
            else:
                transition_partsof_speech[previous_pos][present_pos] = 1
        else:
            transition_partsof_speech[previous_pos] = {present_pos:1}
    
    def get_prob_first_pos(self,label):
        return first_word_label[label]/sum(first_word_label.values())
    
    def prob_simple(self, words, tags):
        p = 0.000001
        for i in range(len(words)):
            p += math.log10(self.get_emision(words[i],tags[i]))+ math.log10(self.get_initial_probability(tags[i]))
        return p
    
    def first_word_count(self,word,partsofspeech):
        if word in first_word_count_dict:
            if partsofspeech in first_word_count_dict[word]:
                first_word_count_dict[word][partsofspeech] += 1
            else:
                first_word_count_dict[word][partsofspeech] = 1
        else:
            first_word_count_dict[word] = {partsofspeech:1}
        if partsofspeech in first_word_label:
            first_word_label[partsofspeech] += 1
        else:
            first_word_label[partsofspeech] = 1
    
    def get_transition_probability(self,transition_partsof_speech):
        for key,value in transition_partsof_speech.items():
            prob = {}
            for key1,value1 in value.items():
                prob[key1] = value1/sum(transition_partsof_speech[key].values())
            transition_prob[key] = prob
        return transition_prob
    
    def add_2nd_level_tran_states(self,grand_pos,parent_pos,present_pos):
        if grand_pos in second_level_transition_dict:
            if parent_pos in second_level_transition_dict[grand_pos]:
                if present_pos in second_level_transition_dict[grand_pos][parent_pos]:
                    second_level_transition_dict[grand_pos][parent_pos][present_pos] += 1
                else:
                    second_level_transition_dict[grand_pos][parent_pos][present_pos] = 1
            else:
                second_level_transition_dict[grand_pos][parent_pos] = {present_pos:1}
        else:
            second_level_transition_dict[grand_pos] = {parent_pos:{present_pos:1}}
            
    def get_second_level_tran_prob(self,pos1,pos2,pos3):
        if pos1 in second_level_transition_dict and pos2 in second_level_transition_dict[pos1] and pos3 in second_level_transition_dict[pos1][pos2]:
            return second_level_transition_dict[pos1][pos2][pos3]/sum(second_level_transition_dict[pos1][pos2].values())
        return 0.000001
        
    def get_emission_probability_train(self,train):
        for key,value in train.items():
            prob = {}
            for key1,value1 in value.items():
                prob[key1] = value1/label_count[key1]
            emission_prob[key] = prob
        return emission_prob
    
    def get_emision(self,word,tag):
        if word in emission_prob and tag in emission_prob[word]:
            return emission_prob[word][tag]
        return 0.000001
    
    def get_transition_prob(self,pos1,pos2):
        if pos1 in transition_prob and pos2 in transition_prob[pos1]:
            return transition_prob[pos1][pos2]
        return 0.000001
    
    def get_initial_probability(self,part_of_speech):
        if part_of_speech in label_count:
            return label_count[part_of_speech] / sum(label_count.values())
        return 0.000001
    
    def get_pos_tags(self,word):
        if word in train:
            return list(train[word].keys())
        return list(label_count.keys())


    def prob_complex(self, words, sample):
        first_tag = sample[0] 
        prob_s1 = math.log10(self.get_prob_first_pos(first_tag))
        transition_prob = 0
        emission_prob = 0
        second_level_transition_prob = 0

        for i in range(len(sample)):
            if self.get_emision(words[i], sample[i]) <= 0:
                value = 1
            else:
                value = self.get_emision(words[i], sample[i])
            emission_prob += math.log(value)
            if i == 0:
                transition_prob += math.log(self.get_transition_prob('start', sample[i]))
            if i != 0:
                transition_prob += math.log(self.get_transition_prob(sample[i - 1], sample[i]))
            '''
            if i > 1:
                second_level_transition_prob += math.log(self.get_second_level_tran_prob(sample[i - 2],sample[i - 1], sample[i]))
                '''
        return prob_s1+transition_prob+emission_prob
    
    def prob_viterbi_hmm(self,words,label):
        first_tag = label[0]
        prob_s1 = math.log10(self.get_prob_first_pos(first_tag))
        emission_prob = 0
        transition_prob = 0
        for i in range(len(label)):
            if self.get_emision(words[i], label[i]) <= 0:
                value = 1
            else:
                value = self.get_emision(words[i], label[i])
            emission_prob += math.log(value)
            if i == 0:
                transition_prob += math.log(self.get_transition_prob('start', label[i]),10)
            if i != 0:
                transition_prob += math.log(self.get_transition_prob(label[i - 1], label[i]),10)
                
        return prob_s1 + emission_prob + transition_prob
    
    def get_probability_from_log_prob(self,a,log_probability):
        probability_list = [0] * len(list(label_count.keys()))
        for i in range(len(log_probability)):
                log_probability[i] -= a
                probability_list[i] = math.pow(10, log_probability[i])
        return probability_list
    
    def sample_generation(self,words, sample):
        tags = list(label_count.keys())
        for index in range(len(words)):
            log_probability = [0] * len(tags)
            for j in range(len(tags)):
                sample[index] = tags[j]
                log_probability[j] = self.prob_complex(words, sample)

            a = min(log_probability)
            probability_list = self.get_probability_from_log_prob(a,log_probability)
            
            s = sum(probability_list)
            for i in range(len(probability_list)):
                probability_list[i] = probability_list[i]/s
                           
            rand = random.uniform(0,1)
            p = 0
            for i in range(len(probability_list)):
                p += probability_list[i]
                if rand < p:
                    sample[index] = tags[i]
                    break
        return sample


    def posterior(self, model, sentence, label):
        if model == "Simple":
            words = list(sentence)
            tags = list(label)
            return self.prob_simple(words,tags)
        elif model == "HMM":
            words = list(sentence)
            tags = list(label)
            return self.prob_viterbi_hmm(words,tags)
        elif model == "Complex":
            words = list(sentence)
            tags = list(label)
            return self.prob_complex(words,tags)
        else:
            print("Unknown algo!")

    # Do the training!
    #
    def train(self, data):
        for (s, gt) in data:
            i = 0
            previous_pos_tag = 'start'
            for word,pos in zip(s,gt):
                if i == 0:
                    self.first_word_count(word,pos)
                if label_count.get(pos):
                    label_count[pos] += 1
                else:
                    label_count[pos] = 1
                if word in train:
                    if pos in train[word]:
                        train[word][pos] += 1
                    else:
                        train[word][pos] = 1
                else:
                    train[word] = {pos:1}
                
                if previous_pos_tag is not None:
                    self.add_transition_states(previous_pos_tag,pos)
                previous_pos_tag = pos
                #if i == 1:
                   # self.add_2nd_level_tran_states('start',gt[i-1],gt[i])
                if i > 1:
                    self.add_2nd_level_tran_states(gt[i-2],gt[i-1],gt[i])
                i += 1
        unique_parts_of_speech = list(label_count.keys())
        self.get_transition_probability(transition_partsof_speech)
        self.get_emission_probability_train(train)
        return train

    # Functions for each algorithm. Right now this just returns nouns -- fix this!
    #
    def simplified(self, sentence):
        pos_label = ['noun']*len(sentence)
        unique_parts_of_speech = list(label_count.keys())
        for word in range(len(sentence)):
            previous_prob = 0
            for i in range(len(unique_parts_of_speech)):
                new_prob = self.get_emision(sentence[word],unique_parts_of_speech[i])*self.get_initial_probability(unique_parts_of_speech[i])
                if new_prob > previous_prob:
                    pos_label[word] = unique_parts_of_speech[i]
                    previous_prob = new_prob
        return pos_label

    def hmm_viterbi(self, sentence):
        V = [{}]
        
        for tag in list(label_count.keys()):
            prob = self.get_initial_probability(tag)*self.get_emision(sentence[0],tag)*self.get_transition_prob('start',tag)
            V[0][tag] = {"prob": prob, "prev": None}

        for i in range(1,len(sentence)):
            V.append({})
            for tag in self.get_pos_tags(sentence[i]):
                max_prob = 0
                for key in V[i-1].keys():
                    prob = V[i-1][key]["prob"]*self.get_emision(sentence[i],tag)*self.get_transition_prob(key,tag)
                    if prob> max_prob:
                        max_prob = prob
                        state = key
                V[i][tag] = {"prob":max_prob,"prev":state}

        path = ['']*len(sentence)
        
        max_value = -math.inf
        
        for key in V[len(V)-1].keys():
            value = V[len(V)-1][key]['prob']
            if value > max_value:
                pos = key
        path[len(sentence)-1] = pos
        
        for i in range(len(V)-1,0,-1):
            for key,value in V[i][path[i]].items():
                path[i-1] = V[i][path[i]]['prev']
        return path

    def complex_mcmc(self, sentence):
        gibbs_samples = []
        tags_list_count = []
        sample = self.simplified(sentence)
        iterations= 75 

        for i in range(iterations):
            sample = self.sample_generation(sentence, sample)
            gibbs_samples.append(sample)

        for j in range(len(sentence)):
            count_tags = {}
            for sample in gibbs_samples:
                try:
                    count_tags[sample[j]] += 1
                except KeyError:
                    count_tags[sample[j]] = 1
            tags_list_count.append(count_tags)

        tags = ['']*len(sentence)
        for i in range(len(sentence)):
            tags[i] = max(tags_list_count[i], key = tags_list_count[i].get)
        return tags



    # This solve() method is called by label.py, so you should keep the interface the
    #  same, but you can change the code itself. 
    # It should return a list of part-of-speech labelings of the sentence, one
    #  part of speech per word.
    #
    def solve(self, model, sentence):
        if model == "Simple":
            return self.simplified(sentence)
        elif model == "HMM":
            return self.hmm_viterbi(sentence)
        elif model == "Complex":
            return self.complex_mcmc(sentence)
        else:
            print("Unknown algo!")

