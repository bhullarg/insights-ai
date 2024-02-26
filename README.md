## Project Template

## 1. Project Description  [To be Updated]

### QuizLLMs: A Model for generating flash cards from text

Develop an app that utilizes LLMs to parse a long text of a specific topic and generate interactive flashcards for effective learning for people.

#### Control Flow
Here we specify the control flow from end-to-end

**Expected Input:** The user provides a path to a text file containing information about a certain topic
**Expected Pipeline:** A model will parse that text and outputs   
**Output:** The ooutput is a question to the user that represents facts about the provided text and a set of 4 answers to chooose from.


#### Experimental Setup 
Here we specify what we need to have our project code running.

**Dataset:** The wikipedia dataset (https://paperswithcode.com/dataset/wiki-en)
**Models to be used**: GPT-4/GPT-3.5, Llama, or Mistral
**Evaluation Metric:** Human Evaluation, or G-Eval (https://arxiv.org/abs/2303.16634)


### Related Work [To be Updated]

Here we keep track of any relevant works to this project

- Chain of Thought prompting (https://arxiv.org/abs/2201.11903)
- Text summarization with pretrained encoders (https://arxiv.org/pdf/1908.08345.pdf)

## 2 Quick start [To be Ran]

### Pre-requisites

Install the libraries

```
pip install -r requirements.txt
```

### Run 

```
python main.py -e basic
```

### Code Structure [To be Updated]

- `data` contains anything related to data
- `scripts` contains all kinds of standalone python and notebook scripts including visualizatin scripts 
- `results` contains results that were saved from the experiments
- `exp_configs` contains the hyperparameters (or arguments) of the experiment.
- `src` contains the functions/objects needed to run the main experiments.

- 

## Figure Pipeline [To Be Updated]

This defines how the control flow works for the project, and this is expected to be refined as the prooject goes on.

![pipeline](docs/pipeline.png)

## Table of Results [To Be Updated]

### Quantitive Results

Here we compare different methods based on the G-Eval metric scores.

|          | Dataset 1 | Dataset 2 |
|----------|-----------|-----------|
| Method 1 |    10     |    20     |
| Method 2 |    15     |    25     |
| Method 3 |    12     |    18     |


### Qualitative Results

Here we compare different methods based on where they get things right, and wronge

|            | Good Cases                    |           Failure Cases               |
|------------------------------------------|--------------------------------------|
| Method 1  | "Who is santa clause? Nicolas" | "Who is santa clause? Michael Jackson" |
| Method 2  |              x                  |                  x                       |
| Method 3  |              x                  |                  x                       |



## Next TODO Items [To be Updated]

**Week 2**
- [] Replace the current summarization method with one that uses GPT-3.5
- [] Create a script to visualize the results for multiple experiments


## Contributers [To be Updated]
| Name            | Role                                   | What to work on?                                                |
|-----------------|----------------------------------------|------------------------------------------------------------------|
| Issam Laradji  | A Facilitator and a Coder               | working on defining relevant templates and related script examples|

