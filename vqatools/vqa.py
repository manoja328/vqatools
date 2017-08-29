# %load vqatools/vqa.py
from collections import defaultdict,Counter
import json
import os
class VQA():
    def __init__(self,annotation_file=None,question_file=None):
        self.answers = {}
        self.questions = {}
        self.qidtoAns={}
        self.imgidtoQids={}
        self.qidtoQues={}
        if not annotation_file == None and not question_file == None:
                print ('Loading VQA annotations and questions in memory...')
                self.answers = json.load(open(annotation_file, 'r'))
                self.questions = json.load(open(question_file, 'r'))
                self.qidtoAns = defaultdict(list)
                self.imgidtoQids = defaultdict(list)
                self.qidtoQues = defaultdict(list)
                print ('Creating index ..')
                for answer in self.answers['annotations']:
                    self.qidtoAns[answer['question_id']] = answer #question id to answer
                    self.imgidtoQids[answer['image_id']].append(answer['question_id'])  # imageid to question id

                for question in self.questions['questions']:
                    self.qidtoQues[question['question_id']] = question #question id to questions
                print ('Index created ..')
                       
                       
    def showQA(self,qid):
        """
        Display the specified question and annotations.
        :param qids (array of object): question ID's to display
        :return: None
        """
        question = self.qidtoQues[qid]
        answer = self.qidtoAns[qid]
        imgId = question['image_id']
        print ("Question: %s" %(question['question']))
        for ans in answer['answers']:
            print ("Answer %d: %s" %(ans['answer_id'], ans['answer']))
        return question['image_id'] #return imageid
                
                
    def getQuesIds(self,quesType):
        """
        Get question ids that satisfy given filter conditions.
                quesTypes (str array)   : get question ids for given question types
        :return:    ids   (int array)   : integer array of question ids
        """
        quesids=[]    
        if not len(quesType) == 0:
            for answer in self.answers['annotations']:
                if answer['question_type'] == quesType:
                    quesids.append(answer['question_id'])
        return quesids
    
    def info(self):
        print ("======= ",self.answers.get('data_type'),"/",self.answers.get('data_subtype')," ======= ")
        print (self.answers.get('info'))
        
                
    def getimgname(self,imgDir,imgid):
        '''get image full name
        Input: imgDir --- main image directory
               imgid  --- image id
        output: int (if on qid) or list (if many qids)
        '''    

        dataSubType = self.answers.get('data_subtype')
        imgFilename = dataSubType+'/COCO_' + dataSubType + '_'+ str(imgid).zfill(12) + '.jpg'
        return  os.path.join(imgDir,imgFilename)


    def showimage(self,img_path):
        '''show image
        Input: img_path --- image path
        output: None
        '''      
        from PIL import Image
        import matplotlib.pyplot as plt
        import numpy as np
        img = Image.open(img_path)
        plt.imshow(np.asarray(img))
        plt.show()

    def getquestion(self,qid):
        '''In: question id 
        out : question (str)'''
        question = self.qidtoQues[qid]
        question_str = question.get('question')
        return question_str

    def getanswer(self,qid):
        '''In: question id 
        out : answer (str)'''
        answers = []
        for ans in self.qidtoAns[qid].get('answers'):
            answers.append(ans['answer'])
        final_answer = Counter(answers).most_common()[0][0]
        return final_answer

    def getimgid(self,qid):
        '''In: question id 
        out : image id(int)'''
        question = self.qidtoAns[qid]
        imgid = question.get('image_id')
        return imgid

    def getqid(self,imgid):
        '''get questions for an image
        Input:image-id 
        output: int (if on qid) or list (if many qids)
        '''
        return self.imgidtoQids[imgid]

