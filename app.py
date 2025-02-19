import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the fine-tuned model
model = T5ForConditionalGeneration.from_pretrained("t5_finetuned_model")
tokenizer = T5Tokenizer.from_pretrained("t5_finetuned_model")


def generate_code(query):
    query = query.lower()
    input_text = "generate code: " + query
    input_ids = tokenizer.encode(input_text,  max_length=128, truncation=True, padding="max_length", return_tensors="pt")
    outputs = model.generate(input_ids, max_length=128, num_beams=4, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


st.title('Code Generation Using Fine-Tuned T5 Model')

query = st.text_input("Enter your query to generate code:")

if st.button("Generate Code"):
    if query:
        code = generate_code(query)
        st.subheader("Generated Code:")
        st.code(code, language="python")
    else:
        st.warning("Please enter a query to generate code.")