import sys
sys.path.append("../")
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import os
from dotenv import load_dotenv
import config
load_dotenv("../../.env")

def get_model():
      checkpoint = "zeeshanakram992/news-suumarization-t5"
      device = "cuda" if torch.cuda.is_available() else "cpu"
      tokenizer = AutoTokenizer.from_pretrained(checkpoint, token=os.getenv("access_token"))
      model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint, token=os.getenv("access_token")).to(device)
      return tokenizer, model

def summarize_article(article):
      tokenizer, model = get_model()
      inputs = tokenizer.encode("summarize: " + article, return_tensors="pt", max_length=config.max_input_length, truncation=True)
      summary_ids = model.generate(inputs, max_length=config.max_target_length, min_length=30, length_penalty=2.0, num_beams=4, early_stopping=True)
      summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
      return summary