from transformers import AutoModelForCausalLM, AutoTokenizer

# Escolha um modelo (exemplo: GPT-2)
model_name = "gpt2"

# Carregar o modelo e o tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Texto inicial (prompt)
prompt = "Era uma vez"

# Tokenizar o texto
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# Gerar texto
output = model.generate(
    input_ids,
    max_length=50,  # Máximo de tokens na saída
    num_return_sequences=1,  # Quantidade de textos gerados
    temperature=0.7,  # Controla a aleatoriedade
    top_p=0.9,  # Nucleus sampling
    do_sample=True  # Ativa amostragem para mais variação
)

# Decodificar e exibir o texto gerado
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
