from collections import defaultdict
import json
class VQA():
    def __init__(self,annotation_file=None,question_file=None):
        self.answers = {}
        self.questions = {}
        self.qa={}
        self.imgToQA={}
        self.qqa={}
        if not annotation_file == None and not question_file == None:
                print ('Loading VQA annotations and questions in memory...')
                self.answers = json.load(open(annotation_file, 'r'))
                self.questions = json.load(open(question_file, 'r'))
                self.qa = defaultdict(list)
                self.imgToQA = defaultdict(list)
                self.qqa = defaultdict(list)
                print ('Creating index ..')
                for answer in self.answers['annotations']:
                    self.qa[answer['question_id']] = answer #question id to answer
                    self.imgToQA[answer['image_id']].append(answer['question_id'])  # imageid to question id

                for question in self.questions['questions']:
                    self.qqa[question['question_id']] = question #question id to questions
                print ('Index created ..')
                       
                       
    def showQA(self,qid):
        """
        Display the specified question and annotations.
        :param qids (array of object): question ID's to display
        :return: None
        """
        question = self.qqa[qid]
        answer = self.qa[qid]
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
        
                
