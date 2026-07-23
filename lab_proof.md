
1. creating chunks after hours:
Fixed-size character chunking with newline separators performed poorly on the podcast transcript because the Whisper output was a continuous text block without paragraph boundaries. The splitter returned the entire transcript as one chunk instead of respecting the target size.
-> sing spaces as separators allowed the splitter to create smaller chunks, but this risks cutting sentences and semantic units. Recursive chunking is expected to handle podcast transcripts better.

PDF - fixed-size chunking cuts through sentences -> try RecursiveCharacterTextSplitter
_______________________________
Does fixed-size chunking break sentences in the middle?
Yes, fixed-size chunking often breaks sentences because it splits based on character count rather than meaning or sentence structure.
How does it handle paragraph boundaries?
It only respects paragraph boundaries if the chosen separator exists; otherwise, it may split text arbitrarily across paragraphs.
Which content type handles fixed-size chunking better?
The PDF handled fixed-size chunking slightly better because it had more natural text boundaries, while the podcast transcript was a continuous conversational text with fewer structural markers.


python chunking_experiment.py
/Users/nevena/Ironhack_Labs/week3/LAB9_Slice-docs/chunking_experiment.py:11: DeprecationWarning: `langchain-community` is being sunset and is no longer actively maintained. See https://github.com/langchain-ai/langchain-community/issues/674 for details and migration guidance toward standalone integration packages.
  from langchain_community.document_loaders import PyPDFLoader
Loaded documents
================
Podcast characters: 17073
PDF characters: 22100

Podcast chunks
--------------
Number of chunks: 85
Average size: 296.4 characters
Smallest chunk: 288 characters
Largest chunk: 300 characters

PDF chunks
----------
Number of chunks: 56
Average size: 472.9 characters
Smallest chunk: 153 characters
Largest chunk: 499 characters

Sentence boundary check
======================
Podcast clean endings: 8.2%
PDF clean endings: 8.9%

First podcast chunk
==================
Welcome back to the Deep Dive. Today, we aren't just reading the news. We are looking at, well, the rulebook for the next century of human history. That sounds a little hyperbolic. I know it sounds hyperbolic, but looking at this stack of documents, I really don't think it is. We are tackling

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

Chunk endings inspection
=======================

Podcast last characters:
unds hyperbolic, but looking at this stack of documents, I really don't think it is. We are tackling

PDF last characters:
in Open Access under the Attribution-
NonCommercial-ShareAlike 3.0 IGO (CC-BY-NC-SA 3.0 IGO) license





not a proof, saving it for my own overview
audio file is too large for the Whisper API upload limit

413: Maximum content size limit (26214400) exceeded
(26430246 bytes read)

-> compress

ffmpeg -i data/Red_Lines_and_Risks_in_the_AI_Act.m4a \
-b:a 64k \
data/Red_Lines_and_Risks_in_the_AI_Act_small.m4a