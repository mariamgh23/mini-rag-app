# Mini RAG App

This is a minimal implementation of a Retrieval-Augmented Generation (RAG) application for question answering.

## Requirements

- Python 3.11 or later
- Miniconda
- Git

## Install Python using Miniconda

### 1. Download and install Miniconda

Download Miniconda from:
https://docs.anaconda.com/miniconda/

### 2. Create a new environment

```bash
conda create -n mini-rag-app python=3.11
```

### 3. Activate the environment

```bash
conda activate mini-rag-app
```

### 4. Clone the repository

```bash
git clone https://github.com/mariamgh23/mini-rag-app.git
cd mini-rag-app
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### set up envirnment variables

```bash
$ cp .env.example  .env
```

### 6. Run the application

```bash
python main.py
```

## Project Structure

```
mini-rag-app/
│
├── data/
├── src/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## License

This project is licensed under the Apache License 2.0.
See the `LICENSE` file for more information.