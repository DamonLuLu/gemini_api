# -*- coding: utf-8 -*-
# @Author   : Eurkon
# @Date     : 2022/3/8 14:17

import settings
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from scrapy.utils.project import get_project_settings

import google.generativeai as genai
import json

app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_credentials=True,
                   allow_origins=["*"],
                   allow_methods=["*"],
                   allow_headers=["*"]
                   )

settings = get_project_settings()


@app.post("/gemini/chat", tags=["API"], summary="GEMINI")
def gemini_chat(data: dict):
    print('chat data:',data)
    json_post = json.dumps(data)
    json_post_list = json.loads(json_post)
    prompt = json_post_list.get('prompt')

    genai.configure(api_key="AIzaSyDO6L-EuN0Nkd2XlhEMTp9O3ERUSQ2vWNg")
    model = genai.GenerativeModel('gemini-pro')
    chat = model.start_chat(history=[])
    response = chat.send_message(prompt)
    text=response.text
    print(text)
    return text




async def request(session, url):
    async with session.get(url) as response:
        return await response.text()


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1")
