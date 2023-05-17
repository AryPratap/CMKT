# Code Mixed Text Toolkit
"""
Language specific toolkits for searching, loading and running models for different NLP tasks.
"""

from cmtt.tasks.LID import *
from cmtt.tasks.NER import *
from cmtt.tasks.POS import *
import os 
import json
from tabulate import tabulate

path = os.path.dirname(os.path.realpath(__file__))
tasks_file_path = os.path.join(path, "tasks.json")

# write all languages in small letters

class LanguageToolKit:
    '''Provides model filtering functions based on tasks and languages'''
    def __init__(self, lang, tasks_file = tasks_file_path):
        self.lang = lang
        self.tasks = self.load_tasks(tasks_file)

    def load_tasks(self, task_file):
        '''
        Returns the list of all the tasks provided by cmtt library
        :param task_file: path of tasks.json file
        :type key: str
        :return: list of dictionaries with info about all the tasks. 
        :rtype: list 
        '''
        f = open(task_file)
        data = json.load(f)
        tasks = data["tasks"]
        f.close()
        return tasks # list of all the dictionaries in tasks

    def list_tasks(self, task_type=''):
        '''
        Returns the list of tasks under a particular task type 
        :param key: task_type (task types available: "Syntactic", "Semantic", "Generational")
        :type key: str
        :return: list of tasks available
        :rtype: list
        '''
        task_list = []
        for i in self.tasks:
            if self.lang in i['language'] and i['task_type'].lower() == task_type.lower():
                task_list.append(i['task'])
        if len(task_list)==0:
            return f"No tasks found in task type {task_type}"
        return task_list
    
    
    def model_info_file(self, task):
        model_file = ""
        for i in self.tasks:
            if self.lang in i['language'] and i['task'].lower() == task.lower():
                model_file = i['model_info']
                break
        if model_file == "":
            return None
        model_info_path = os.path.join(path, model_file)
        f = open(model_info_path)
        data = json.load(f)
        list_of_dic = data["model"]
        f.close()
        return list_of_dic # list of dictionaries in model info 
    
    def task_model_info(self, task='', details=False):
        '''
        Returns the information about available models for the given task.
        :param key: task (for e.g. "lid", "pos" etc)
        :type key: str
        :param details: to specify whether to fetch complete info table or just names of models.
        :type details: bool
        :return: list or table of all the available models for the given task
        :rtype: list (if details = False) or str (if details = True)
        '''

        model_info = self.model_info_file(task)
        if model_info == None:
            return f"No models found for task {task}"
        
        headers = model_info[0].keys()
        rows = []
        model_list = []
        for i in model_info:
            if self.lang == i["language"] and i["task"].lower() == task.lower():
                if details:
                    rows.append(i.values())
                else:
                    model_list.append(i["Model name"])

        if details:
            table = tabulate(rows, headers=headers, tablefmt="grid")
            return table   
        return model_list
  
    
class HinglishToolKit(LanguageToolKit):
    '''Toolkit for Hindi English mixed text'''
    XLM_HIEN_LID = XLM_HIEN_LID
    XLM_HIEN_NER = XLM_HIEN_NER
    XLM_HIEN_POS = XLM_HIEN_POS

    def __init__(self):
        super().__init__('hineng')

class SpanishEnglishToolKit(LanguageToolKit):
    '''Toolkit for Spanish English mixed text'''
    def __init__(self):
        super().__init__('spaeng')

        

    



