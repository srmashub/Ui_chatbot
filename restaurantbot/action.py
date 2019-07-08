from rasa_nlu.config import RasaNLUModelConfig 
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer,Interpreter
from rasa_nlu import config

training_data=load_data('./data/data.json')
trainer=Trainer(config.load('config.json'))
trainer.train(training_data)
model_directory=trainer.persist('./models/nlu',fixed_model_name='Practice')
interpreter=Interpreter.load(model_directory)
print(interpreter.parse(u'what is the summary of the issue'))