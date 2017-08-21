#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 13:21:19 2017

@author: manoj
"""

from collections import defaultdict
import json
class Visual7wTell():
    def __init__(self,file=None):
        '''param: filename full path for Telling task.'''
        self.data = json.load(open(file,'r'))
        self.imgidtoqid = defaultdict(list)
        self.imgidtosplit = {} #val test train
        self.qidtoqa = {}
        for sample in self.data['images']:
            self.imgidtosplit[sample.get('image_id')] = sample.get('split')
            for qa in sample.get('qa_pairs'):
                self.imgidtoqid[sample.get('image_id')].append(qa.get('qa_id'))
                self.qidtoqa[qa.get('qa_id')]=qa

    def getQuesIds(self,quesType):
        '''Return all the question id starting from questType'''
        quesids=[]    
        if not len(quesType) == 0:
            for qid in self.qidtoqa.keys():
                qa = self.qidtoqa[qid]
                if qa.get('type') == quesType:
                    quesids.append(qa.get('qa_id'))
            return quesids

    def getCountquesids(self):
        '''Return all the question id starting from how many for counting'''
        qids = self.getQuesIds(quesType='how')
        quesids=[]
        if not len(qids) == 0:
            for qid in qids:
                question = self.qidtoqa[qid].get('question')
                if question.find('How many') == 0:
                    quesids.append(qid)
            return quesids

  
    def showQA(self,qid):
        '''param: qid -- question id
        Show QA in presentable format'''
        qa= self.qidtoqa[qid]
        print ("Img id: ",qa.get('image_id'))
        print (qa.get('question'))
        print ("Ans: ",qa.get('answer'))


    def info(self):
        '''show info'''
        print ("======= ",self.data.get('dataset'),self.data.get('version')," ======= ")

        
 
class Visual7wPoint():
    def __init__(self,file=None):
        '''param: filename full path for Pointing task.'''
        self.data = json.load(open(file,'r'))
        self.imgidtoqid = defaultdict(list)
        self.imgidtosplit = {} #val test train
        self.qidtoqa = {}
        self.boxidtobox = {}
        for sample in self.data['images']:
            self.imgidtosplit[sample.get('image_id')] = sample.get('split')
            for qa in sample.get('qa_pairs'):
                self.imgidtoqid[sample.get('image_id')].append(qa.get('qa_id'))
                qa['image_id'] = sample.get('image_id') # also add img_id 
                self.qidtoqa[qa.get('qa_id')]=qa

        for box in self.data['boxes']:
            self.boxidtobox[box.get('box_id')] = box      

    def getQuesIds(self):
        '''Return all the question id starting from which'''
        return list(self.qidtoqa.keys())
                     

    def showQA(self,qid):
        '''param: qid -- question id
        Show QA in presentable format'''
        qa= self.qidtoqa[qid]
        #multiple_choices = 
        print ("Multiple choices: ",qa.get('multiple_choices'))
        print ("Img id: ",qa.get('image_id'))
        print (qa.get('question'))
        print ("Ans: ",qa.get('answer'))
                
                
    def info(self):
        '''show info'''
        print ("======= ",self.data.get('dataset'),self.data.get('version')," ======= ")