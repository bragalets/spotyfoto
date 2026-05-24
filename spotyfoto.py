import os
from google import genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

secret_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=secret_key)

print("Analisando a foto...")

try:
    foto = Image.open('C:/spotyfoto/received_image.jpg')


    prompt = """
        Você é um DJ e curador musical especialista em sinestesia (transformar imagens em som).
        Sua missão é criar a trilha sonora perfeita para a imagem enviada.
        
        PASSO A PASSO DA SUA ANÁLISE INVISÍVEL:
        1. Observe as cores dominantes e a iluminação (ex: escuro/neon = eletrônica; claro/sol = reggae/pop).
        2. Identifique os elementos principais (pessoas, animais, natureza, cidades, objetos românticos ou de festa).
        3. Capte a emoção central da cena (melancolia, alegria, romance, adrenalina, paz).
        
        SUA TAREFA:
        Com base nessa análise, defina a 'vibe' da foto usando EXATAMENTE 3 gêneros ou subgêneros musicais.
        
        REGRAS DE SAÍDA (ESTRITAMENTE OBRIGATÓRIO):
        - Responda APENAS com os 3 gêneros separados por vírgula.
        - NÃO escreva nenhuma palavra extra, nem antes nem depois.
        - NÃO use emojis.
        - Mantenha os nomes dos gêneros em inglês.
        """
    
    resposta = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=[prompt, foto]
    )
    
    print(resposta.text)

except FileNotFoundError:
    print("Erro: Eu não achei a foto. A foto foi salva corretamente?")
except Exception as e:
    print(f"Ops, deu algum erro: {e}")