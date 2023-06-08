#!/bin/python3
import openai,os,signal,time


openai.api_key = "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"

def ctrl_c(sig,frame):
    print("exiting ...")
    sys.exit(0)

signal.signal(signal.SIGINT,ctrl_c)

question = ""
while True:
    while not question.strip():
        question = input(" : ")

    try:
        answer = openai.Completion.create(engine="text-davinci-003",
                                                prompt=question,
                                                max_tokens=2048).choices[0].text
        print(answer)
        break
    except IndexError:
        print(" : ")
        question = input(" : ")


    



