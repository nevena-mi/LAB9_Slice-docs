## Chunking Strategy Recommendations

### For PDF Documents

**Recommended Strategy:** Recursive Character Chunking

**Reasoning:**
- Preserves paragraph and section boundaries better than fixed-size chunking.
- Produces consistent chunk sizes while maintaining document structure.
- Works well with long structured documents.

**Recommended parameters:**
- Chunk size: 500
- Chunk overlap: 100
(not really as I did not played with it yet)


### For Podcast Transcripts

**Recommended Strategy:** Recursive Character Chunking

**Reasoning:**
- Better preserves conversational flow and sentence boundaries.
- Reduces the chance of splitting ideas in the middle.
- Produces more coherent chunks for downstream retrieval.

**Recommended parameters:**
- Chunk size: 500
- Chunk overlap: 100
(not really as I did not played with it yet)


## Trade-offs Summary

| Strategy | Pros | Cons | Best For |
|-----------|------|------|----------|
| Fixed Character | Simple, fast, predictable | Can split sentences or paragraphs | Simple or uniformly structured text |
| Recursive Character | Preserves natural document structure | Slightly more complex configuration | PDFs, articles, transcripts |
| Token-Based | Controls LLM context size accurately | Ignores semantic boundaries | LLM applications with token limits |
| Semantic | Preserves meaning between chunks | Computationally expensive and requires embeddings | High-quality RAG and semantic search |


## Overall Conclusion

Recursive character chunking provided the best balance between chunk size consistency and preservation of document structure. Token-based chunking is valuable when working with LLM context windows, while fixed-size chunking is useful for simple baselines because it is easy to implement and computationally efficient.

________________________________________________________________




Recursive chunking generally preserves context better because it tries to split at meaningful boundaries such as paragraphs and sentences before falling back to smaller units. Fixed-size chunking is simpler but can break sentences or semantic units, while token-based chunking is useful for controlling LLM context size but does not prioritize natural language boundaries.

The podcast transcript benefits most from recursive chunking because it is conversational and has long continuous text. The PDF shows less improvement because PDF extraction already disrupts formatting and section boundaries, limiting how well any text splitter can preserve the original structure.


Podcast
=======
Strategy    Avg       Min       Max       Chunks    Ends %
Fixed       491.0     217       500       43        11.6
Recursive   453.3     363       500       43        2.3
Token       2307.7    2187      2468      9         11.1

PDF
===
Strategy    Avg       Min       Max       Chunks    Ends %
Fixed       488.5     160       500       56        1.8
Recursive   477.7     405       499       55        5.5
Token       1953.1    1736      2169      14        0.0



_____________________________________________________________


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