
1. created chunks after hours. swiching from notebook to .py, and the restructuring completely. deleted all evidences, new will come

LAB9_Slice-docs/
│
├── config.py.  
├── transcription.py
├── transcribe_audio.py
├── pdf_loader.py
├── transcript_loader.py
├── chunking.py
├── evaluation.py
├── run_fixed_chunking.py
├── run_recursive_chunking.py
├── run_token_chunking.py
├── compare_chunking.py
│
├── data/
├── transcripts/
├── outputs/
│
├── chunking_strategies.ipynb
├── requirements.txt
├── .env
├── .gitignore
└── lab_proof.md

python run_token_chunking.py

Podcast token chunks
--------------------
Number of chunks: 25
Average size: 906.9 characters
Smallest chunk: 263 characters
Largest chunk: 1012 characters

PDF token chunks
----------------
Number of chunks: 23
Average size: 1147.4 characters
Smallest chunk: 553 characters
Largest chunk: 1359 characters

Sentence boundary check
======================
Podcast clean endings: 12.0%
PDF clean endings: 0.0%

First podcast chunk
==================
Welcome back to the Deep Dive. Today, we aren't just reading the news. We are looking at, well, the rulebook for the next century of human history. That sounds a little hyperbolic. I know it sounds hyperbolic, but looking at this stack of documents, I really don't think it is. We are tackling Regulation EU 2024 1689. Or as your friends in the tech industry probably call it, with a mix of fear and respect, the AI Act. Right, the AI Act. Yeah. It's huge, it's dense, and it is officially the world's first comprehensive legal framework for artificial intelligence. But here's my worry right off the bat. When we talk about regulation, people tend to picture, you know, dusty binders and bureaucrats stamping forms. Sure. But this is about whether a robot can decide if you go to jail, or if you get that loan for your house, or if your boss can track your facial expressions

First PDF chunk
================
Adopted on 23 November 2021
Key facts
UNESCO’s
 Recommendation on 
 the Ethics
 of Artificial
Intelligence
Supported by:
2
Published in 2023 by the United Nations Educational, Scientific and 
Cultural Organization, 7, place de Fontenoy, 75352 Paris 07 SP , France
 
© UNESCO 2023
SHS/2023/PI/H/1
 
All rights reserved.
This publication is available in Open Access under the Attribution-
NonCommercial-ShareAlike 3.0 IGO (CC-BY-NC-SA 3.0 IGO) license 
(http://creativecommons.org/licenses/by-nc-sa/3.0/igo/). By using 
the content of this publication, the users accept to be bound by the 
terms of use of the UNESCO Open Access Repository (www.unesco.
org/open-access/terms-use-ccbyncsa-en).
Cover photo: metamorworks / Shutterstock.com
Graphic design (Cover & Layout): Sara Rienda de la Mota 
Printed by UNESCO 
Printed in France
32
Table of Contents
08
2A Human Rights Approach to AI· Ten core principles lay out a Human Rights-centred 
Approach to the Ethics of AI
·
Message from Gabri

___________________________________________________________________
not a proof, saving it for my own overview
audio file is too large for the Whisper API upload limit

413: Maximum content size limit (26214400) exceeded
(26430246 bytes read)

-> compress

ffmpeg -i data/Red_Lines_and_Risks_in_the_AI_Act.m4a \
-b:a 64k \
data/Red_Lines_and_Risks_in_the_AI_Act_small.m4a