# Emotion Classification Using EEG Data

The project is an application which is able to interpret 62-channel raw EEG data. It displays visual representations of the data: a heatmap of the brain activity and plots for each sensor on the brain. A pre-trained classification model then predicts the patient's emotion based on differential entropy features extracted from the data.

## Important Links

| [Timesheet](https://1sfu-my.sharepoint.com/:x:/g/personal/hamarneh_sfu_ca/Ef_s4WY7UVxPpZngZ5eVljkByHTSBahuE1fXw5A8XSuf0A?e=AVYG3B) | [Slack channel](https://app.slack.com/client/T06AP91EYG6/C06DYV7JFDH) | [Project report](https://www.overleaf.com/project/65a57e5afb3c02bb10233144) |
|-----------|---------------|-------------------------|


## Table of Contents
1. [Video Description and Demonstration](#demo)

2. [Installation](#installation)

3. [Reproducing this project](#repro)

4. [Guidance](#guide)


<a name="demo"></a>
## 1. Video Description and Demonstration



https://github.com/sfu-cmpt340/2024_1_project_17/assets/115741743/9740200b-e547-4092-a347-0f3dee0b3af9



### File Information

```bash
repository
├── src                          ## App source code (Python)
    ├── images                   ## Images for UX enhancement (work in progress)
    ├── important                ## Non-code files critical for the app's function
    ├── App.py                   ## Runs the app
    ├── de_psd_calculation.py    ## Extracts DE and PSD features from raw EEG data
    ├── feature_extraction.py    ## Extracts DE and PSD features with specific parameters
    ├── file_read.py             ## A collection of functions to read .mat and .npz files
    ├── graphing.py              ## Creates graphs of the EEG data
    ├── model.pkl                ## Trained model for prediction
    ├── predict.py               ## Predicts an emotion from raw EEG input data
    ├── test_model.py            ## Loads and tests a model
    ├── train_model.py           ## Loads DE features and trains a model
    ├── ui.py                    ## Displays the UI of the app
    ├── visualization.py         ## Creates the image that visualizes the sensors on the brain
├── LISCENSE                     ## Liscensing   
├── README.md                    ## You are here
├── report.tex                   ## Project report
├── requirements.txt             ## Requirements for running the app
```

<a name="installation"></a>

## 2. Installation

Provide sufficient instructions to reproduce and install your project. 
Provide _exact_ versions, test on CSIL or reference workstations.

```bash
git clone $THISREPO
cd $THISREPO
conda env create -f requirements.yml
conda activate amazing
```

<a name="repro"></a>
## 3. Reproduction
Demonstrate how your work can be reproduced, e.g. the results in your report.
```bash
mkdir tmp && cd tmp
wget https://yourstorageisourbusiness.com/dataset.zip
unzip dataset.zip
conda activate amazing
python evaluate.py --epochs=10 --data=/in/put/dir
```
Data can be found at ...
Output will be saved in ...

<a name="guide"></a>
## 4. Guidance

- Use [git](https://git-scm.com/book/en/v2)
    - Do NOT use history re-editing (rebase)
    - Commit messages should be informative:
        - No: 'this should fix it', 'bump' commit messages
        - Yes: 'Resolve invalid API call in updating X'
    - Do NOT include IDE folders (.idea), or hidden files. Update your .gitignore where needed.
    - Do NOT use the repository to upload data
- Use [VSCode](https://code.visualstudio.com/) or a similarly powerful IDE
- Use [Copilot for free](https://dev.to/twizelissa/how-to-enable-github-copilot-for-free-as-student-4kal)
- Sign up for [GitHub Education](https://education.github.com/) 
