from transformers import GPTNeoForCausalLM, GPT2TokenizerFast
import torch


class TextGenerator():
    model = GPTNeoForCausalLM.from_pretrained("NlpHUST/gpt-neo-vi-small")
    tokenizer = GPT2TokenizerFast.from_pretrained("NlpHUST/gpt-neo-vi-small") 
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def __init__(self) -> None:
        TextGenerator.model.to(TextGenerator.device)
        pass


    def genText(self, prompt):
        input_ids = TextGenerator.tokenizer(prompt, return_tensors="pt")['input_ids'].to(TextGenerator.device)
        choices = 5


        gen_tokens = TextGenerator.model.generate(
            input_ids,
            max_length=20,
            do_sample=True,
            temperature=0.9,
            top_k=20,
            repetition_penalty=10.0,
            num_return_sequences=choices
        )
        print(TextGenerator.tokenizer.decode(gen_tokens[0],skip_special_tokens = True).encode('utf-8').hex())
        result = map(lambda token:TextGenerator.tokenizer.decode(token,skip_special_tokens = True).split(' '), gen_tokens)
        return list(result)
        pass


