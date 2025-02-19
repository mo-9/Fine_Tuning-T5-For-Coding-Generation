# Fine_Tuning-T5-For-Coding-Generation
Project: Fine-Tuning T5 for Code Generation
This project focuses on fine-tuning the T5 (Text-to-Text Transfer Transformer) model using PyTorch to generate code from natural language descriptions. The trained model is then deployed using Streamlit for an interactive web interface.



Key Components:
✅ T5 Model – A transformer-based model fine-tuned on code datasets.
✅ PyTorch – Used for training and optimizing the model.
✅ Dataset – A collection of programming prompts and corresponding code snippets.
✅ Training Process – Fine-tuning T5 for code generation using a pre-trained checkpoint.
✅ Streamlit App – A simple web interface where users enter a description, and the model generates corresponding code.



This code fine-tunes the T5 model (t5-small) for conditional generation using the Hugging Face Transformers library and PyTorch. It sets up a Trainer with customized TrainingArguments, including learning rate, batch size, and number of epochs. The model is trained using a dataset (train_dataset and eval_dataset), optimizing with mixed-precision (fp16=True) for faster performance. The best model is saved automatically at the end of training. This setup enables T5 to generate high-quality text outputs based on input sequences, making it suitable for tasks like code generation, text summarization, and translation. 

Outcome:
A lightweight and efficient code-generation tool, capable of assisting developers by converting text-based prompts into Python (or other) code snippets. 
![Screenshot 2025-02-19 160340](https://github.com/user-attachments/assets/d5a94e11-4710-4fb5-9f28-ce2672d63d6b)
