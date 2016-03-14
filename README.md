# Computacao_Distribuida
Repositório destinado a trabalhos desenvolvidos na disciplina de computação distribuída.

Os exemplos estao escritos usando python, o framework web bottle e o pacote requests.

Rodando:

Para rodar os exemplos e' necessario o python3, o pacote bottle, o pacote json e o pacote requests. Todos os pacotes estao disponiveis atraves do pip.

(como root) $ pip3 install bottle requests
Apos, basta entrar na pasta do exemplo e roda'-los:

$ cd t2
$ python3 dht.py
Para testar, pode ser usado o browser ou entao a ferramenta de linha de comando curl

$ curl -w "\n" -X GET "http://localhost:8080/dht/abcd1234"
$ curl -w "\n" -X PUT "http://localhost:8080/dht/abcd1234/1234"
$ curl -w "\n" -X GET "http://localhost:8080/dht/abcd1234"
