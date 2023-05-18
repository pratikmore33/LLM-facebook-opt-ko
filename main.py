from fastapi import FastAPI
import uvicorn
# from model import generate_text

from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import pipeline
from translate import Translator
# lets import tokenizer from pretrained model 
tokenizer = AutoTokenizer.from_pretrained("facebook/opt-125m")
# load pretrained model 
checkpoint = "facebook/opt-125m"
# device_map["gpt_neox.layers.31"] = "cpu"
model = AutoModelForCausalLM.from_pretrained(
    checkpoint, device_map='auto', offload_folder="offload", offload_state_dict = True)
# define pipeline for the text generation 
text_generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

def generate_text(text):
    # transalate korean text
    translator = Translator(from_lang="ko", to_lang="en")
    translated_text_en = translator.translate(text)
    # generate response from text generation model 
    prompt = translated_text_en
    # inputs = tokenizer(prompt, return_tensors="pt")
    # output = model.generate(inputs["input_ids"],max_new_tokens=20)
    generated_text = text_generator(prompt, max_length=20)[0]['generated_text']
    
    # generated_text = tokenizer.decode(output[0].tolist())
    # lets convert back generated text to korean 
    translator = Translator(to_lang="ko")
    translated_text_ko = translator.translate(generated_text)
    return translated_text_ko

app = FastAPI()

@app.get('/')
async def welcome():
    return {'message':'welcome to nexsol'}

@app.get('/opt')
async def generator(text):
    response = generate_text(text)
    return response

# if __name__ == '__main__':
#     uvicorn.run(app)
