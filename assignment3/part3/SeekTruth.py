# SeekTruth.py : Classify text objects into two categories
#
# PLEASE PUT YOUR NAMES AND USER IDs HERE
#
# Based on skeleton code by D. Crandall, October 2021
#

import sys
import re
from math import log

def text_clean(text):
    stopwords=set(['you', '', 'then', 'i', 'we','only', 'does', 'when', 'by', 'theyre', 'mustnt', 'these', 'am', 'yourself', 'from', 'can', 'hers', 'now', 'should', 'during', 'there', 'than', 'id', 'up', 'but', 'too', 'y', 'such', 'mightnt', 'before', 'no', 'has', 'didn', 'an', 'haven', 'themselves', 'those', 'his', 'that', 'below', 'ill', 'theyd', 'couldnt', 'under', 'theirs', 'which', 'how', 'is', 'theyve', 'they', 'been', 've', 'your', 'itself', 'my', 'shan', 'other', 'hes', 'didnt', 'are', 'out', 'd', 'him', 'while', 'very', 'whens', 'werent', 'having', 'wed', 'arent', 'their', 'just', 'any', 'over', 'hasnt', 'wheres', 'herself', 'did', 'its', 'needn', 'would', 'most', 'had', 'same', 'against', 'between', 'hasn', 'wouldn', 'wasn', 'havent', 'about', 'at', 'aren', 'whom', 'shes', 's', 'or', 'a', 'all', 'll', 'cant', 'after', 'further', 'shouldve', 'once', 'because', 'not', 'ought', 'both', 'if', 'each', 'as', 'heres', 'ma', 'cannot', 'i', 'of', 'where', 'who', 'shell', 'won', 'theyll', 'thats', 'some', 'ourselves', 'and', 'weve', 'doing', 'o', 'youve', 'this', 'wouldnt', 'have', 'ain', 'youll', 'yours', 'youre', 'for', 'down', 'weren', 't', 're', 'was', 'myself', 'be', 'theres', 'hed', 'neednt', 'mustn', 'dont', 'don', 'we', 'few', 'shant', 'with', 'isn', 'own', 'here', 'whats', 'doesn', 'whys', 'isnt', 'into', 'hell', 'off', 'himself', 'whos', 'lets', 'im', 'it', 'doesnt', 'ours', 'shouldn', 'shouldnt', 'until', 'couldn', 'the', 'yourselves', 'she', 'in', 'hows', 'youd', 'her', 'wont', 'so', 'do', 'hadn', 'our', 'on', 'being', 'well', 'thatll', 'shed', 'm', 'more', 'will', 'he', 'above', 'wasnt', 'again', 'them', 'what', 'were', 'why', 'me', 'nor', 'could', 'ive', 'through', 'hadnt', 'to', 'mightn'])
     
    text = re.sub('[^a-zA-Z\s]+', '', text)
    text = re.sub(' +', ' ', text)
    text = text.lower()
    text = text.split()
    text=[word for word in text if not word in stopwords]            
    text = ' '.join(text)
    return text

def review_counter(train_data):
    review_count = {}
    for r in train_data["labels"]:
        label = r
        if(review_count.get(label)):
            review_count[label] = review_count[label] + 1
        else:
            review_count[label] = 1
    return review_count

def cal_priori_prob(review_count, total_review):
    label_prob = {}
    for i in review_count:
        label_prob[i] = log(float(review_count[i])/total_review)
    
    return label_prob

def load_file(filename):
    objects=[]
    labels=[]
    with open(filename, "r") as f:
        for line in f:
            parsed = line.strip().split(' ',1)
            labels.append(parsed[0] if len(parsed)>0 else "")
            objects.append(text_clean(parsed[1] if len(parsed)>1 else ""))
    return {"objects": objects, "labels": labels, "classes": list(set(labels))}

def distinct_word_dict(train_data,allWord_dict):
    for row in train_data["objects"]:
        for word in row.split():
            if allWord_dict.get(word):
                allWord_dict[word] += 1
            else:
                allWord_dict[word]  = 1 

def make_word_dict(train_data,true_word_dict,dec_word_dict):
    for i in range(len(train_data["labels"])):
        if train_data["labels"][i]=="deceptive":
            for word in train_data["objects"][i].split():
                if dec_word_dict.get(word):
                    dec_word_dict[word] += 1
                else:
                    dec_word_dict[word] = 1
        else:
            for word in train_data["objects"][i].split():
                if true_word_dict.get(word):
                    true_word_dict[word] += 1
                else:
                    true_word_dict[word] = 1

def cal_count(count_dict):
    w_count=0
    for i in count_dict:
        w_count+=count_dict[i]
    return w_count

def predict(test_data,true_word_dict,dec_word_dict,true_word_count,dec_word_count,priori_prob):
    for i in range(len(test_data["objects"])):
        t_prob=1.0
        d_prob=1.0
        for word in test_data["objects"][i].split():
            if true_word_dict.get(word):
                t_prob+=log(float((true_word_dict[word]+1)/(true_word_count+2)))
            else:
                t_prob+=log(float(1/(true_word_count+2)))


            if dec_word_dict.get(word):
                d_prob+=log(float((dec_word_dict[word]+1)/(dec_word_count+2)))
            else:
                d_prob+=log(float(1/(dec_word_count+2)))

        t_prob*=(priori_prob["truthful"])
        d_prob*=(priori_prob["deceptive"])

        if t_prob/d_prob<1:
            test_data["labels"].append("truthful")
        else:
            test_data["labels"].append("deceptive")




# classifier : Train and apply a bayes net classifier
#
# This function should take a train_data dictionary that has three entries:
#        train_data["objects"] is a list of strings corresponding to reviews
#        train_data["labels"] is a list of strings corresponding to ground truth labels for each review
#        train_data["classes"] is the list of possible class names (always two)
#
# and a test_data dictionary that has objects and classes entries in the same format as above. It
# should return a list of the same length as test_data["objects"], where the i-th element of the result
# list is the estimated classlabel for test_data["objects"][i]
#
# Do not change the return type or parameters of this function!
#
def classifier(train_data, test_data):

    counter=review_counter(train_data)
    total_reviews= len(train_data["labels"])

    priori_prob=cal_priori_prob(counter, total_reviews)

   # print("Priori Probilities",priori_prob)

    allWord_dict={}
    distinct_word_dict(train_data,allWord_dict)


    true_word_dict = {}
    dec_word_dict= {}
    make_word_dict(train_data,true_word_dict,dec_word_dict)

    true_word_count=cal_count(true_word_dict)
    dec_word_count=cal_count(dec_word_dict)

    predict(test_data,true_word_dict,dec_word_dict,true_word_count,dec_word_count,priori_prob)

    #word_dict = get_most_freq(word_dict)
    
    return test_data["labels"] 


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Usage: classify.py train_file.txt test_file.txt")

    (_, train_file, test_file) = sys.argv
    # Load in the training and test datasets. The file format is simple: one object
    # per line, the first word one the line is the label.
    train_data = load_file(train_file)
    test_data = load_file(test_file)



    if(sorted(train_data["classes"]) != sorted(test_data["classes"]) or len(test_data["classes"]) != 2):
        raise Exception("Number of classes should be 2, and must be the same in test and training data")

    # make a copy of the test data without the correct labels, so the classifier can't cheat!
    test_data_sanitized = {"objects": test_data["objects"],"labels":[], "classes": test_data["classes"]}
    #print(test_data_sanitized['classes'])

    results= classifier(train_data, test_data_sanitized)

    # calculate accuracy
    correct_ct = sum([ (results[i] == test_data["labels"][i]) for i in range(0, len(test_data["labels"])) ])
    print("Classification accuracy = %5.2f%%" % (100.0 * correct_ct / len(test_data["labels"])))
