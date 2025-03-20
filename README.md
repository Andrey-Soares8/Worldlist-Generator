# 🔑 Gerador de Wordlists Profissional

> 🛠️ Uma ferramenta moderna e eficiente para geração de wordlists com interface gráfica

## ✨ Características

- 🖥️ Interface gráfica moderna e intuitiva
- 🚀 Geração rápida e eficiente
- 📊 Barra de progresso em tempo real
- 🛑 Possibilidade de interromper a geração
- 💡 Tooltips informativos
- 🔄 Processamento em thread separada
- 📝 Logging profissional
- ⚠️ Validações e avisos de segurança

## 🔧 Requisitos

- Python 3.7+
- tkinter (geralmente já vem com Python)
- Sistema Operacional: Windows, Linux ou macOS

## 📦 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/gerador-wordlist.git
cd gerador-wordlist
```

2. (Opcional) Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Execute o programa:
```bash
python worldlist.py
```

## 🎯 Como Usar

1. 📝 Digite os caracteres que deseja usar na geração
   - Por padrão, usa letras e números
   - Você pode personalizar com qualquer conjunto de caracteres

2. 🔢 Defina os comprimentos mínimo e máximo
   - Mínimo: menor tamanho de palavra a ser gerada
   - Máximo: maior tamanho de palavra a ser gerada

3. 🚀 Clique em "Gerar Wordlist"
   - Escolha onde salvar o arquivo
   - Acompanhe o progresso pela barra
   - Use o botão "Parar" se precisar interromper

## ⚠️ Avisos

- ⚡ Comprimentos grandes podem gerar arquivos muito extensos
- 💾 Certifique-se de ter espaço em disco suficiente
- 🕒 O tempo de geração aumenta exponencialmente com o tamanho

## 🔍 Exemplo de Uso

```python
# Valores padrão
Caracteres: abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
Comprimento Mínimo: 1
Comprimento Máximo: 4
```

Este exemplo gerará todas as combinações possíveis de 1 a 4 caracteres usando letras e números.

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

- 🐛 Reportar bugs
- 💡 Sugerir novas funcionalidades
- 📝 Melhorar a documentação
- 🔧 Enviar pull requests

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## 👨‍💻 Autor

Desenvolvido por Andrey Soares.
---

⭐ Se este projeto foi útil para você, considere dar uma estrela! 