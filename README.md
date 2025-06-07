# 🧩 Projeto: Exemplos de Padrões de Projeto (Design Patterns)

Este repositório contém implementações práticas de alguns dos principais **padrões de projeto** utilizados em desenvolvimento de software, com foco em exemplos simples e funcionais em **Python** e **Java**.

## 📦 Padrões Implementados

### 🔁 Observer (Python)

> Arquivo: `Main.py`

Implementa o padrão **Observer**, onde múltiplos observadores são notificados sempre que o objeto observado sofre alguma alteração.

**Características:**
- Usa `abc.ABC` para definir a interface dos observadores.
- Observadores podem ser adicionados/removidos dinamicamente.
- Demonstra envio de mensagem para múltiplos observadores.

---

### 🔧 Adapter (Python)

> Arquivos: `CEPAdapter.py` e `main.py`

Implementa o padrão **Adapter**, integrando um sistema local com a API pública **ViaCEP**, para consulta de endereços a partir do CEP.

**Características:**
- Adapta a resposta da API ao modelo local (`Endereco`).
- Encapsula a lógica de acesso e transformação dos dados da API.
- Exemplo funcional com entrada via terminal.

---

### 🔒 Singleton (Java)

> Arquivo: `Singleton.java`

Implementação clássica do padrão **Singleton**, que garante que uma classe tenha **apenas uma instância** ao longo de toda a aplicação.

**Características:**
- Controle de instância via atributo estático privado.
- Construtor privado para impedir múltiplas instâncias.
- Método estático `getInstance()` para acesso controlado.
