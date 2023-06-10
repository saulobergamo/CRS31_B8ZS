# <center>Universidade Tecnológica Federal do Paraná
## <center>Bacharelado em Sistemas de Informação
### <center>Comunicação de dados - CSR31
___


Trabalho apresentado à disciplina de Comunicação de Dados dos cursos de graduação de Bacharelado em Sistemas de Informação e Engenharia de Computação da Universidade Tecnológica Federal do Paraná.

Comunicação entre dois computadores através da rede. O programa deve ser capaz de:
> Host A (envio): digitar o texto; aplicar o algoritmo de criptografia; transformação em binário; aplicar o princípio do algoritmo de codificação de linha; apresentação do gráfico; envio para o outro lado.

> Host B (recepção): recepção; apresentar o gráfico; aplicar o algoritmo de codificação de linha de modo inverso; transformação de binário para ASCII; aplicar o algoritmo de criptografia inverso; mostra a mensagem.

___
📌 **IMPORTANTE** 📌
- Interface gráfica (deverá mostrar: msg escrita,msg criptografada,msg em binário, msg aplicado o algoritmo e o gráfico 1,0pts;
- A forma de onda deve ser mostrada na forma de gráfico após a transformação com a sequência aplicada no algoritmo 2,0pts(forma de onda deverá ser mostrado em ambos oslados. De um lado o processo de montagem e do outro o processo inverso);
- Comunicação: entre dois ou mais computadores 1,0pts•Criptografia utilizada 1,5 pts;
- Mensagem dever ser transformada em binário utilizando a tabela ASCII estendido para dar correspondência (levar em consideração letras especiais e com acento), 0,5pt;
- Depois de transformada, deve-se aplicar o princípio do algoritmo escolhido para transformar a mensagem 2,0pt;
- A mensagem dever ser enviada para o outro lado pela rede1,0pt;•O outro lado deve ser capaz de realizar o processo inverso e desmontar todo o bloco até reconhecer a msg 1,0pt


***
---
___
# <CENTER>ENGLISH
Paper presented to the Data Communication discipline of the Bachelor's Degree in Information Systems and Computer Engineering at the Federal Technological University of Paraná.

Communication between two computers over the network. The program must be able to:
> Host A (sending): enter the text; apply the encryption algorithm; binary transformation; apply the principle of line coding algorithm; graph presentation; send to the other side.

> Host B (reception): reception; display the graph; apply the line encoding algorithm inversely; Binary to ASCII transformation; apply the inverse encryption algorithm; shows the message.

___
📌 **IMPORTANT** 📌
- Graphic interface (should show: written msg, encrypted msg, binary msg, msg applied algorithm and graph 1.0pts;
- The waveform must be shown in graphic form after the transformation with the sequence applied in the 2.0pts algorithm (the waveform must be shown on both sides. On one side the assembly process and on the other the inverse process);
- Communication: between two or more computers 1.0pts•Cryptography used 1.5pts;
- Message must be transformed into binary using the extended ASCII table to match (take into account special letters with accents), 0.5pt;
- After being transformed, the principle of the chosen algorithm must be applied to transform the 2.0pt message;
- The message must be sent to the other side over the 1.0pt network; • The other side must be able to carry out the inverse process and dismantle the entire block until it recognizes the 1.0pt message

***
---
___

***
---
___

### Pré-requisitos

O que será necessário instalar para que funcione corretamente

- VSCode
- Git
- Python (versão utilizada: 3.8.10)
- Matplot lib (pip install matplotlib)


### Instalação


- Realizar o clone do projeto:

  Comando: ```git clone git@github.com:saulobergamo/CSR31_B8ZS.git```

- Acessar a pasta do projeto:

  - Executar na máquina do cliente:

    Comando: ```python3 message_sender.py```

  - Executar na máquina do servidor:

    Comando: ```python3 message_receiver.py```


