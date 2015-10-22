import pprint
import json
import corenlp
import os

corenlp_dir =os.environ['HOME']+"/bosswork/stanford-corenlp-full-2013-06-20"
user_properties=os.environ['HOME']+"/bosswork/study/LanguageProcessing/user_properties"
paser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir,properties=user_properties)

result_json= json.loads(paser.parse("This video is so very high price!"))
pprint.pprint(result_json)

